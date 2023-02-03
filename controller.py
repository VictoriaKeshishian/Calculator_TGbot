import telebot 

bot = telebot.TeleBot('6155388103:AAHyyXy5hr6Hael0YuerDys2Mww9Q7RmF1Q')

value = ''
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('c', callback_data='c'),
                telebot.types.InlineKeyboardButton('<=', callback_data='<='),
                telebot.types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(   telebot.types.InlineKeyboardButton('7', callback_data='7'),
                telebot.types.InlineKeyboardButton('8', callback_data='8'),
                telebot.types.InlineKeyboardButton('9', callback_data='9'),
                telebot.types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(   telebot.types.InlineKeyboardButton('4', callback_data='4'),
                telebot.types.InlineKeyboardButton('5', callback_data='5'),
                telebot.types.InlineKeyboardButton('6', callback_data='6'),
                telebot.types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(   telebot.types.InlineKeyboardButton('1', callback_data='1'),
                telebot.types.InlineKeyboardButton('2', callback_data='2'),
                telebot.types.InlineKeyboardButton('3', callback_data='3'),
                telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(   telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('0', callback_data='0'),
                telebot.types.InlineKeyboardButton(',', callback_data='.'),
                telebot.types.InlineKeyboardButton('=', callback_data='='))

keyboard.row(   telebot.types.InlineKeyboardButton('complex', callback_data='complex'))
keyboard.row(   telebot.types.InlineKeyboardButton('j', callback_data='j'))

@bot.message_handler(commands=['start','calculate',])
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)

@bot.message_handler(commands=['instruction'])
def instruction(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}, для работы в данном калькуляторе с комплексными числами введи выражение по типу 1 + 5j + 2 + 3j в строку калькулятора, затем нажми complex") 

@bot.callback_query_handler(func=lambda call: True)
def callback(query):
    global value, old_value
    data = query.data

    if data == 'no':
        pass
    elif data == 'c':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Ошибка'
    elif data == 'complex':
        try:
            value = complex(eval(value))
        except:
            value = 'Ошибка'
    else:
        value += data
    
    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id,message_id = query.message.message_id, text='0', reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id, text=value, reply_markup=keyboard)
            old_value = value
            
    old_value = value
    if value == 'Ошибка': value = ''




bot.polling(non_stop=False, interval=0)

