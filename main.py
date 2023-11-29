import telebot
bot = telebot.TeleBot("6647202001:AAHrSDTHweqSigmFbsVZBi9lbC_4AAoMIYI")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'хочешь студенческий анекдот?', parse_mode='Markdown')

bot.infinity_polling()