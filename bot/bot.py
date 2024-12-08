import telebot
from telebot import types
from time import sleep
import datetime
from ..api_app.backend.backend import seve_data_db, get_data_db_period

                    
    


bot = telebot.TeleBot('6105146346:AAFcm1CVVly8GllMD_KXDBw0iF20x6RiW8g')

sales:dict = {}


@bot.message_handler(commands=['start'])
def start(message):
    print(f'Enter User\n{datetime.datetime.now()}')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton("Внести данные о продажах"))
    keyboard.add(types.KeyboardButton("Получить отчет о продажах за период"))

    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}! \nВыбери действие: ', reply_markup=keyboard) 
    sleep(5*60)
    start(message)


@bot.message_handler(content_types='text')

def choose(message):

    if message.text == 'Внести данные о продажах':
        bot.send_message(message.chat.id, 'Введите название товара/Цена товара: ')
        bot.register_next_step_handler(message, add_title_price)

    if message.text == 'Сохранить':
        title:str = sales['title']
        price:float = sales['price']
        seve_data_db(title, price)
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
    file = get_data_db_period(start_period, end_period)
            
    bot.send_message(message.chat.id, 'Данные выгружены.')
    bot.send_message(chat_id, f'Выбранный период:\n{start_period}\n{end_period}')
    bot.send_document(message.chat.id, file['file'])
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
    bot.polling(non_stop=True)
    print('Stop bot . . .')