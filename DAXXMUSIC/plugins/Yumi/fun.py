from pyrogram import Client, filters
import requests
import random
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  
from DAXXMUSIC import app

regex_gif = ["slap"]
pht = random.choice(regex_gif)
url = f"https://api.waifu.pics/sfw/{pht}"

@app.on_message(filters.command("slap"))
def get_waifu(client, message):
    response = requests.get(url).json()
    up = response['url']
    if up:
        message.reply_video(up,caption="BY @Anya_forger_probot",
    else:
        message.reply("Request failed try /again")

regex_gif = ["kiss"]
pht = random.choice(regex_gif)
url = f"https://api.waifu.pics/sfw/kiss"

@app.on_message(filters.command("kiss"))
def get_waifu(client, message):
    response = requests.get(url).json()
    up = response['url']
    if up:
        message.reply_video(up,caption="BY @Anya_forger_probot",
    else:
        message.reply("Request failed try /again")

regex_gif = ["hug"]
pht = random.choice(regex_gif)
url = f"https://api.waifu.pics/sfw/hug"

@app.on_message(filters.command("hug"))
def get_waifu(client, message):
    response = requests.get(url).json()
    up = response['url']
    if up:
        message.reply_video(up,caption="BY @anya_forger_probot",
    else:
        message.reply("Request failed try /again")
      

regex_gif = ["pat"]
pht = random.choice(regex_gif)
url = f"https://api.waifu.pics/sfw/pat"

@app.on_message(filters.command("pat"))
def get_waifu(client, message):
    response = requests.get(url).json()
    up = response['url']
    if up:
        message.reply_video(up,caption="BY @Anya_Forger_probot",
    else:
        message.reply("Request failed try /again")
      

regex_gif = ["bite"]
pht = random.choice(regex_gif)
url = f"https://api.waifu.pics/sfw/bite"

@app.on_message(filters.command("bite"))
def get_waifu(client, message):
    response = requests.get(url).json()
    up = response['url']
    if up:
        message.reply_video(up,caption="BY @Anya_Forger_probot",
    else:
        message.reply("Request failed try /again")


  regex_gif = ["kick"]
pht = random.choice(regex_gif)
url = f"https://api.waifu.pics/sfw/kick"

@app.on_message(filters.command("kick"))
def get_waifu(client, message):
    response = requests.get(url).json()
    up = response['url']
    if up:
        message.reply_video(up,caption="BY @Anya_Forger_probot",
    else:
        message.reply("Request failed try /again")


  regex_gif = ["kick"]
pht = random.choice(regex_gif)
url = f"https://api.waifu.pics/sfw/kick"

@app.on_message(filters.command("kick"))
def get_waifu(client, message):
    response = requests.get(url).json()
    up = response['url']
    if up:
        message.reply_video(up,caption="BY @Anya_Forger_probot",
    else:
        message.reply("Request failed try /again")
