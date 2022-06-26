from pyrogram import Client , filters
import asyncio
from pyrogram.types import Message

@amaan.on_message(filters.command("pmto", HANDLER) & filters.me)
@amaan.on_message(filters.command("pmto", HANDLER) & filters.user(SUDOERS))
async def pmto(c: Client, m: Message):
    a = message.pattern_match.group(1)
    b = a.split(" ")
    chat_id = b[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    msg = ""
    for i in b[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await client.send_message(chat_id, msg)
        await message.edit_text("Message sent!")
    except BaseException:
        await message.edit_text("Something went wrong.")
