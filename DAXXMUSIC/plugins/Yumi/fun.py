import requests
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
from DAXXMUSIC import app

@app.on_message(filters.command("kiss"))
async def es_url(_, message):
    ai = "https://api.waifu.pics/sfw/kiss"
    get_kiss = get(ai)
    ai_kiss = get_kiss.json()
    get_gif_url = ai_kiss["url"]
    await message.reply_video(
            get_gif_url,
            caption="BY @Anya_forger_probot",  # Add spoiler caption
            parse_mode=ParseMode.MARKDOWN # Enable Markdown parsing
        )
    else:
        await message.reply_text("Website ke mayya chod dala")
