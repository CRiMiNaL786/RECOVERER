from datetime import datetime
from pyrogram import Client
from pyrogram import filters, __version__
from sys import version_info
from main import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

#ALiVE

StartTime = datetime.now()

@Client.on_message(filters.command(["alive", "al"], [".", "!"]) & filters.me)
@Client.on_message(filters.command(["alive", "al"], [".", "!"]) & filters.user(SUDOERS))
async def alive(c: Client, message: Message):
    await message.delete()
    text="**RECOVERER**\n"
    text += f"\nPython Version: `{version_info[0]}.{version_info[1]}.{version_info[2]}`"
    text += f"\nPyrogram Version: `{__version__}`"
    text += f"\nCurrent Uptime: `{str(datetime.now() - StartTime).split('.')[0]}`"
    
    await c.send_message(text)


#PiNG 

@Client.on_message(filters.command(["ping", "Ping"], [".", "!"]) & filters.me)
@Client.on_message(filters.command(["ping", "Ping"], [".", "!"]) & filters.user(SUDOERS))
async def ping(_, message: Message):
    start = datetime.now()
    end = datetime.now()
    m_s = (end - start).microseconds / 1000 
    await message.reply_text(f"**🏓PoNG!**\n`{m_s} ms`")


 
