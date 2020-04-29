import telebot
import sqlite3

conn = sqlite3.connect('patients.db', check_same_thread=False)

bot = telebot.TeleBot('1080190983:AAFVWiuunibNKicCwmpjH3CJEaxh_ZY3B78')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ассалаумағалейкум, че там кiм керек? Паспорт номерiн жазып жiбер.')


@bot.message_handler(content_types=['text'])
def find_patient(message):
    c = conn.cursor()
    c.execute('SELECT * FROM patients WHERE passport_num=?', (message.text,))

    row = c.fetchone()

    if row is not None:
        full_name = ''
        birth_date = ''
        diagnosis = ''

        while row is not None:
            print(row)
            full_name = row[1]
            birth_date = row[2]
            diagnosis = row[3]
            row = c.fetchone()
            response = "Аты-жөні: " + full_name + ".\nТуған Күнi: " + birth_date + ".\nДиагноз: " + diagnosis + ".\n\nТағы кiм керек?"
    
    else:
        response = "Бундай номер жок! Тагы жазып көр."

    bot.send_message(message.chat.id, response)
    c.close()

bot.polling()