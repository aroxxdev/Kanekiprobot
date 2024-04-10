import requests
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
from DAXXMUSIC import app

@app.on_message(filters.command("kiss"))
async def es_url(_, message):
    url = "https://api.waifu.pics/sfw/kiss"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image = data["url"]
        await message.reply_video(
            gif,
            caption="BY @Anya_forger_probot",  # Add spoiler caption
            parse_mode=ParseMode.MARKDOWN # Enable Markdown parsing
        )
    else:
        await message.reply_text("Website gyi")
