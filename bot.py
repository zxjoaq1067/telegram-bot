from dotenv import load_dotenv
from os import getenv
import logging
import datetime
from telegram.ext import Updater, CommandHandler

from commands.contract import contract
from commands.tutorial_metamask import metamask 
from commands.tutorial_trustwallet import trust 
from commands.price import price
from commands.help import safemoon_help
from commands.site import site
from commands.tokenomics import tokenomics
from commands.graph import graph
from commands.video import video
from commands.news import news
from commands.discord import discord 
from commands.store import store
from commands.instagram import instagram
from commands.twitter import twitter

# get bot api token from .env
load_dotenv('.env')
BOTAPI = getenv('BOTAPITOKEN')

# Set logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# create updater object
updater = Updater(token=BOTAPI, use_context=True)

# set dispatcher locally for quick access
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou o bot dos sonegadores de impostos. Use o comando /help para exibir os comandos disponíveis.")


# set command handler
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', safemoon_help)
contract_handler = CommandHandler('contract', contract)
price_handler = CommandHandler('price', price)

tut_metamask_handler = CommandHandler('metamask', metamask)
tut_trust_handler = CommandHandler('trust', trust)
site_safemoon_handler = CommandHandler('site', site)
tokenomics_safemoon_handler = CommandHandler('tokenomics', tokenomics)
graph_safemoon_handler = CommandHandler('graph', graph)
video_safemoon_handler = CommandHandler('video', video)
news_safemoon_handler = CommandHandler('news', news)
discord_safemoon_handler = CommandHandler('discord', discord)
store_safemoon_handler = CommandHandler('store', store)
instagram_safemoon_handler = CommandHandler('instagram', instagram)
twitter_safemoon_handler = CommandHandler('twitter', twitter)

# add handlers to dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(contract_handler)
dispatcher.add_handler(tut_metamask_handler)
dispatcher.add_handler(tut_trust_handler)
dispatcher.add_handler(price_handler)
dispatcher.add_handler(site_safemoon_handler)
dispatcher.add_handler(tokenomics_safemoon_handler)
dispatcher.add_handler(graph_safemoon_handler)
dispatcher.add_handler(video_safemoon_handler)
dispatcher.add_handler(news_safemoon_handler)
dispatcher.add_handler(discord_safemoon_handler)
dispatcher.add_handler(store_safemoon_handler)
dispatcher.add_handler(instagram_safemoon_handler)
dispatcher.add_handler(twitter_safemoon_handler)

# start bot
updater.start_polling()
