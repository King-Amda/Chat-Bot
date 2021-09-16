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

START_IMG = "https://telegra.ph/file/66623ce5d08ec0323ce40.jpg"

START_TEXT = """
𝐃𝐚𝐫𝐤 𝐒𝐡𝐚𝐫𝐤 ගෙ 𝐏𝐌 𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 එකෙන් ඔයාට 𝐃𝐚𝐫𝐤 𝐒𝐡𝐚𝐫𝐤 ට 𝐌𝐬𝐠 දාන්න දෙන්නෙ නෑ ..

ඒකට විකල්පයක් විදියට තමයි 𝐊𝐢𝐧𝐠 𝐀𝐦𝐝𝐚 𝐁𝐨𝐭 ව හැදුවෙ..

ඔයාලට මේකෙන් 𝐃𝐚𝐫𝐤 𝐒𝐡𝐚𝐫𝐤 ව සම්බන්ධ කරගන්න පුලුවන්.

ගොඩ දෙනෙක් අහන ප්‍රශ්න යට බටන් වල තියෙනවා..
ඔයාට ඕන ඒවා තියෙනම් එතනින් ගන්න පුලුවන්.. 
යටම තීන 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐃𝐚𝐫𝐤 𝐒𝐡𝐚𝐫𝐤 බටන් එකෙන් ඔයාට 𝐃𝐚𝐫𝐤 𝐒𝐡𝐚𝐫𝐤 ව සම්බන්ධ කර ගන්න පුලුවන්.
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('King Amda Telegram',url='https://t.me/......'),
        InlineKeyboardButton('King Amda Whatsap',url='https://wa.me/94783752040')
        ],
        [
        InlineKeyboardButton('Our Main Bot(Anki Cozmo)',url='https://t.me/TheAnkiCozmoBot'),
        InlineKeyboardButton('GitHub',url='https://github.com/King-Amda')
        ],
        [InlineKeyboardButton('Apply For Anki Cozmo Devs', url='https://forms.gle/zvspqb7Nn2MvWmbu8')
        ]]
)

@KINGAMDA.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(
        START_IMG,
        caption=PM_START_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=ParseMode.MARKDOWN,
        quote=True
)
    
KINGAMDA.run()        
