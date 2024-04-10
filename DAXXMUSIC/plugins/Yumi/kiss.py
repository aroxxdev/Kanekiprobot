
import requests
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
from DAXXMUSIC import app

@app.on_message(filters.command("kiss"))
async def es_img(_, message):
    url = "https://api.waifu.pics/sfw/kiss"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image = data["image"]
        await message.reply_video(
            image,
            caption="BY @Anya_Forger_ProBot",  # Add spoiler caption
            parse_mode=ParseMode.MARKDOWN # Enable Markdown parsing
        )
    else:
        await message.reply_text("Website gyi")
