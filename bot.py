import telebot
from bs4 import BeautifulSoup
import requests
from pprint import pprint

bot=telebot.TeleBot(ENTER YOUR BOT TOKEN HERE)

@bot.message_handler(commands=['getscore','start'])
def greeting_message(message):
    bot.reply_to(message, "Here u can get the live cricket matches score updates\n\nType /score to get current match score updates")

@bot.message_handler(commands=['score'])
def send_score(message):
    l=[]
    url='http://static.cricinfo.com/rss/livescores.xml'
    page=requests.get(url)
    soup=BeautifulSoup(page.text, 'html.parser')
    pprint(soup)
    result=soup.find_all('description')
    for match in result:
        bot.reply_to(message, match)
    
@bot.message_handler(func=lambda message:True)
def send_default(message):
    bot.reply_to(message, 'please enter the correct command')

bot.polling()


