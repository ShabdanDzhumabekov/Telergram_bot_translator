import telebot
import requests

def get_translation(text,lang):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    KEY = 'trnsl.1.1.20191025T140958Z.6f479863fb548c75.9e2d23313a811d32763b5cca07aad4df34069e3c'
    TEXT = text
    LANG = lang

    r = requests.post(URL,data={'key':KEY,'text':TEXT,'lang':LANG})
    return eval(r.text)

Token = '1015658880:AAHtyOl1ch2H8Wd6Ck8oEMMcTVRFU9UycCs'
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, я,переводчик. Перевожу с английского на татарский и наоборот. Если вы напишите на других языках, то буду переводить на кыргызский язык')

@bot.message_handler(content_types=['text'])
def send_text(message):
    lang = str(get_translation(message.text,'tt')['lang'])
    lang = lang[0]+lang[1]

    if lang=='en':
        text=str(*get_translation(message.text,'tt')['text'])
        bot.send_message(message.chat.id,text + '\n «Переведено сервисом «Яндекс.Переводчик»  http://translate.yandex.ru в целях обучения')
    elif lang=='tt':
        text = str(*get_translation(message.text, 'en')['text'])
        bot.send_message(message.chat.id,
                         text + '\n «Переведено сервисом «Яндекс.Переводчик»  http://translate.yandex.ru в целях обучения')
    else:
        text = str(*get_translation(message.text, 'ky')['text'])
        bot.send_message(message.chat.id,
                         text + '\n «Переведено сервисом «Яндекс.Переводчик»  http://translate.yandex.ru в целях обучения')

bot.polling(none_stop=True, interval=0)
