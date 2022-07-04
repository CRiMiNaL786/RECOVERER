from datetime import datetime
from pyrogram import Client
from pyrogram import filters
from main import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



    await message.delete()
    text="**RECOVERER**\n"
    text += f"\nPython Version: `{version_info[0]}.{version_info[1]}.{version_info[2]}`"
    text += f"\nPyrogram Version: `{__version__}`"
    text += f"\nCurrent Uptime: `{str(datetime.now() - StartTime).split('.')[0]}`"
    
    await c.send_message(chat.id, text)


@Client.on_message(filters.command(["ping", "Ping"], [".", "!"]) & filters.me)
@Client.on_message(filters.command(["ping", "Ping"], [".", "!"]) & filters.user(SUDOERS))
async def ping(_, message: Message):
    start = datetime.now()
    end = datetime.now()
    m_s = (end - start).microseconds / 1000 
    await message.reply_text(f"**🏓PoNG!**\n`{m_s} ms`")


 
