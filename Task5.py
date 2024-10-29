# Завдання №5. На основі Telegram Bot API створити бота, що підтримує команди menu, whisper, scream

import telebot

TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['menu'])
def handle_menu(message):
    response = (
        'Доступні команди:\n'
        '/menu - Показати всі команди\n'
        '/whisper - Написати повідомлення маленькими літерами\n'
        '/scream - Написати повідомлення великими літерами'
    )
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['whisper'])
def handle_whisper(message):
    msg = bot.reply_to(message, "Введіть повідомлення, яке потрібно перетворити в нижній регістр:")
    bot.register_next_step_handler(msg, whisper_text)

def whisper_text(message):
    response = message.text.lower()
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['scream'])
def handle_scream(message):
    msg = bot.reply_to(message, "Введіть повідомлення, яке потрібно перетворити у верхній регістр:")
    bot.register_next_step_handler(msg, scream_text)

def scream_text(message):
    response = message.text.upper()
    bot.send_message(message.chat.id, response)

if __name__ == '__main__':
    print('Бот запущений...')
    bot.polling(none_stop=True)
