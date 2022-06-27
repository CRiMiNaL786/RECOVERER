from pyrogram.types import ChatPermissions
from pyrogram.raw.functions.channels import GetAdminedPublicChannels
from pyrogram import Client , filters
import asyncio
from pyrogram.types import Message
from main import SUDOERS

@Client.on_message(filters.command(["listmyusernames", "lmun"], [".", "!"]) & filters.me)
@Client.on_message(filters.command(["listmyusernames", "lmun"], [".", "!"]) & filters.user(SUDOERS))
async def listmun(c: Client, m: Message):
    result = await Client.send(GetAdminedPublicChannels())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await message.edit_text(output_str)
