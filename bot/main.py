import telebot
from telebot import types
import datetime
import requests

                    
bot = telebot.TeleBot('6105146346:AAFcm1CVVly8GllMD_KXDBw0iF20x6RiW8g')

sales:dict = {}


@bot.message_handler(commands=['start'])
def start(message):
    print(f'Enter User\n{datetime.datetime.now()}')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton("Внести данные о продажах"))
    keyboard.add(types.KeyboardButton("Получить отчет о продажах за период"))
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}! \nВыбери действие: ', reply_markup=keyboard) 


@bot.message_handler(content_types='text')

def choose(message):

    if message.text == 'Внести данные о продажах':
        bot.send_message(message.chat.id, 'Введите название товара/Цена товара: ')
        bot.register_next_step_handler(message, add_title_price)

    if message.text == 'Сохранить':
        title:str = sales['title']
        price:float = sales['price']
        api = 'http://api/add/'
        responce = requests.post(url = api, json={'title' : title, 'price' : price})
        if responce.status_code == 200:
            print(responce)
            bot.send_message(message.chat.id, 'Позиция добавлена')
        start(message) 

    if message.text == 'Отмена':
        start(message)  

    if message.text == 'Получить отчет о продажах за период':
        bot.send_message(message.chat.id, 'Введите начальный период и конец периода \nВ формате: "день-месяц-год, часы:минуты/день-месяц-год, часы:минуты": ')
        bot.register_next_step_handler(message, get_and_send_data)

 

    

def get_and_send_data(message):
    chat_id: int = message.chat.id
    start_end:str = (message.text).split('/') 
    start_period = start_end[0]
    end_period = start_end[1]
    api = 'http://api/sales/'
    responce = requests.post(url=api, json={"start": start_period, "end": end_period})
    if responce.status_code == 200:
        file = open('result.xlsx', 'rb')
    bot.send_message(message.chat.id, 'Данные выгружены.')
    bot.send_message(chat_id, f'Выбранный период:\n{start_period}\n{end_period}')
    bot.send_document(message.chat.id, file)
    start(message) 


            
    


def add_title_price(message):
    chat_id:int = message.chat.id
    title_price:str = (message.text).split('/')

    sales['title'] = title_price[0]
    sales['price'] = title_price[1]  

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [
                types.KeyboardButton("Сохранить"),
                types.KeyboardButton("Отмена")
            ]        
    keyboard.add(*buttons)
    bot.send_message(chat_id, f'title:   {sales["title"]}\nprice:   {sales["price"]} ', reply_markup=keyboard)





if __name__ == '__main__':
    print('Start bot . . .')
    bot.polling(non_stop=True, timeout=60)
    print('Stop bot . . .')