from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MahakMusic import app
from config import BOT_USERNAME

start_txt = """
❖ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ.

● ɪ ᴀᴍ ➥ ๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐ ᴍᴜsɪᴄ ʙᴏᴛ.

❖ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐ ᴍᴜsɪᴄ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
"""




@app.on_message(filters.command("repourl"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Silent_Smile_04"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/Silentsmile29/musicnode")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/e7464ffc455b4e8dbb477.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
