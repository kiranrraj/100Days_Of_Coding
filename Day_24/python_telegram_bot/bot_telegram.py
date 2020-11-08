from telegram.ext import Updater, CommandHandler
import requests
import re



def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']
    return image_url
