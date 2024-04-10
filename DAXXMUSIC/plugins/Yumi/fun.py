from requtest import get
from pyrogram import filters
from pyrogram.types import Message
from DAXXMUSIC import app

@app.on_message(filters.command("kiss"))
async def es_url(_, message):
    try:
        api = "https://api.waifu.pics/sfw/kiss"
        get_kiss = get(api)
        get_json = get_kiss.json()
        get_gif_url = get_json["url"]
        await message.reply_video(get_gif_url, caption="BY @Anya_forger_probot")
    except:
        pass
