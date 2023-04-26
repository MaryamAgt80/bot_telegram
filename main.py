import telebot
import mysql.connector
# import os

connection = mysql.connector.connect(
    user='root',
    password='',
    host='127.0.0.1',  # localhost
        database='filesupload'
)
cursor = connection.cursor()

query = """
       SELECT * FROM filename;
    """
cv=cursor.execute(query)
result = []
for id, name, address in cursor:
      data = {id: {'name': name, 'address': address}}
      result.append(data)
print(result)


bot=telebot.TeleBot('YOUR TOKEN',parse_mode=None)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
	bot.reply_to(message, "Hello enter your file name")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    matn=message.text
    try:
         pdf= open('./file_contentn/'+matn+'.pdf', 'rb')
         bot.send_document(message.chat.id, pdf)
    except:
        bot.reply_to(message, 'not found your file.')



bot.infinity_polling()