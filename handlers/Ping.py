from datetime import datetime
from pyrogram import Client
from pyrogram import filters
from main import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message




@Client.on_message(filters.command(["ping", "Ping"], [".", "!"]) & filters.me)
@Client.on_message(filters.command(["ping", "Ping"], [".", "!"]) & filters.user(SUDOERS))
async def ping(_, message: Message):
    start = datetime.now()
    end = datetime.now()
    m_s = (end - start).microseconds / 1000 
    await message.reply_text(f"**🏓PoNG!**\n`{m_s} ms`")


 
