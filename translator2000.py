from googletrans import Translator
import telebot

def translate_now(text,lenguage):
    try:
        translate = Translator()
        return translate.translate(text,lenguage).text
    except:
        return 'Error'



lenguages ={'chinese': 'zh', 'english': 'en', 'french': 'fr', 'german': 'de', 'italian': 'it', 'japanese': 'ja', 'kazakh': 'kk', 'korean': 'ko', 'polish': 'pl', 'russian': 'ru', 'ukrainian': 'uk' }
bot = telebot.TeleBot('943596929:AAGTUO2fHKAWX1dR3nURb2alQEMRmRvl0s0')
temp = str()
last_lenguage = 'ru'
x = False


@bot.message_handler(commands = ['swlen'])
def swlen_command(message):
    global x
    x = True
    bot.send_message(message.chat.id,'Enter lenguage')


@bot.message_handler(commands = ['lenguages'])
def show_leguages(message):
    bot.send_message(message.chat.id, '''You can translate to this lenguges:
    ------------------
    Chinese     🇨🇳
    English     🇬🇧
    Frunch      🇫🇷
    German      🇩🇪
    Italian     🇮🇹
    Japanese    🇯🇵
    Kazakh      🇰🇿
    Korean      🇰🇷
    Polish      🇵🇱
    Russian     🇷🇺
    Ukrainian   🇺🇦
    ----------------''')
    bot.send_message(message.chat.id, 'To translate into another language send me command /swlen and then send 1 lenguage from this list 👆')

@bot.message_handler(content_types = 'text')
def translate(message):
    global last_lenguage,x
    if x:
        print (123)
        if not message.text.lower().strip() in lenguages:
            bot.send_message(message.chat.id, 'Lenguage EROR!!!')
        else:
            last_lenguage = lenguages[message.text.lower().strip()] 
            bot.send_message(message.chat.id, 'Lenguage was ' + message.text.lower().strip() + ' 😄')
            x = False
    else:
        try:
            print(x)
            bot.send_message(message.chat.id, translate_now(message.text,last_lenguage))
        except:
            bot.send_message(message.chat.id, 'Error')

            
       


bot.polling()

