from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from MukeshRobot import OWNER_ID, dispatcher
from MukeshRobot import pbot as client

Mukesh = "https://telegra.ph/file/c5a5b99f4d405796fab55.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Mukesh,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

╔═════ஜ۩۞۩ஜ════╗

 ❁❁𝗠𝗔𝗗𝗘 𝗕𝗬[𝗠𝗔𝗗𝗔𝗥𝗔](https://t.me/ULTRA_BOT_UPDATES)❁❁
  
╚═════ஜ۩۞۩ஜ════╝

**[𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗥𝗢𝗕𝗢𝗧](t.me/{dispatcher.bot.username}) sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❁ᴏᴡɴᴇʀ❁",f"tg://user?id={OWNER_ID}"
                    ),
                    InlineKeyboardButton(
                        "❁ʀᴇᴘᴏ❁",
                        url="https://telegra.ph/file/2b7ec040e2929b335736f.mp4",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "✯Rᴇᴩᴏ✯"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
