import requests
from bs4 import BeautifulSoup
import pyjokes
import datetime
from telegram.ext import Updater, CommandHandler

# Replace YOUR_TOKEN_KEY with your token string
# To get your token, look at the README.md file or issue #1
updater = Updater(
    token='YOUR_TOKEN_KEY', use_context=True)
dispatcher = updater.dispatcher


def start(update):
    update.message.reply_text(
        """
        Hello, Please write\n/help to see the commands available.
        """
    )


def help(update):
    update.message.reply_text(
        """
        I can help you with the following commands:
        \n/start - Start the bot\n/help - Get help\n/joke - Get a random joke\n/quote - Get a quote of the day\n/date - Get the current date\n/time - Get the current time
        """
    )


def joke(update):
    update.message.reply_text(pyjokes.get_joke())


def quote(update):
    update.message.reply_text(
        """
        Quote of the day:
        """
    )
    res = requests.get('https://www.brainyquote.com/quote_of_the_day')
    soup = BeautifulSoup(res.text, 'lxml')

    quote = soup.find(
        'img', {'class': 'p-qotd bqPhotoDefault img-responsive'})
    update.message.reply_text(quote['alt'])


def date(update):
    update.message.reply_text(
        """
        Date:
        """
    )
    date = datetime.datetime.now()
    update.message.reply_text(date.strftime("%m/%d/%Y"))


def time(update):
    update.message.reply_text(
        """
        Time:
        """
    )
    time = datetime.datetime.now()
    update.message.reply_text(time.strftime("%H:%M"))


def bitcoin(update):
    update.message.reply_text(
        """
        Bitcoin Price:
        """
    )
    res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = res.json()
    update.message.reply_text(data['bpi']['USD']['rate'])


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('joke', joke))
dispatcher.add_handler(CommandHandler('quote', quote))
dispatcher.add_handler(CommandHandler('date', date))
dispatcher.add_handler(CommandHandler('time', time))
dispatcher.add_handler(CommandHandler('bitcoin', bitcoin))
updater.start_polling()
