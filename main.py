import os
from os import error
import logging
import pyrogram
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

KINGAMDA = Client(
    "king-amda",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_STICKER = "CAACAgEAAxkBAAEGuU5h3v5XAAFBZBNscH9lJfI8s5qmm5MAAsUBAAJKYnlFMGvOnsDF3wEjBA"

START_TEXT = """
Hi Friend ..
How Are Your.

I Am Nipun's Assistant.
Put Down What You Want Nipun To Say With Your Username. He Will Look And Reply To You.
The Important Thing Is To Come To The @NiupunDinujaya Inbox.

Thank You.
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Telegram',url='https://t.me/NiupunDinujaya'),
        InlineKeyboardButton('Github',url='https://github.com/King-Amda')
        ],
        [
        InlineKeyboardButton('Website',url='https://telegra.ph/file/7d5ce36a275474f38c418.jpg'),
        InlineKeyboardButton('Help',url='https://telegra.ph/file/7d5ce36a275474f38c418.jpg')
        ]]
)

@KINGAMDA.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(
        START_STICKER,
        caption=PM_START_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=ParseMode.MARKDOWN,
        quote=True
)
    
KINGAMDA.run()        
