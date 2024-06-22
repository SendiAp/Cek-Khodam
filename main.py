from pyrogram.enums import ParseMode
from pyrogram import Client, filters
from pyrogram.types import *
from config import *
from khodam import *
import random
import os

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

START_TEXT = """
Halo {} , Cek Khodammu Sekarang🤜🤛 Sebelum Terlambat 

Gunakan Perintah:
/cekKhodam - (nama kamu)

Jangan lupa dishare ketemanmu🤜
"""

@bot.on_message(filters.command("start") & filters.private)
async def start(bot : Client, message : Message):
    name = message.from_user.first_name
    await message.reply(START_TEXT.format(name))
    
@bot.on_message(filters.command("cekKhodam"))
async def cekkhodam(bot : Client, message : Message):
    khodam = random.choice(Pasukan)
    chat_id = message.chat.id
    msg = get_arg(message)
    if message.reply_to_message:
        msg = message.reply_to_message

    text = f"➡️ Khodam {msg}: **{khodam}**"
    if not msg:
        return await message.reply(text="❌ Berikan Saya Pesan / Reply Sebuah Pesan/nama.")

    xx = await message.reply(f"🔍 Sedang Melihat Khodam {msg} ....")
    
    try: 
        await bot.send_photo(chat_id, f"photo/{khodam}.jpg", caption=text)
        await xx.delete()
    except BaseException as e:
        return await message.reply(f"`{e}`")


print('🔥 [BOT BERHASIL DIAKTIFKAN] 🔥')

bot.run()
