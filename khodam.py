from pyrogram.enums import ParseMode
from pyrogram import Client, filters
from random import choice
from config import *
from string import *
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

@bot.on_message(filters.command("cekKhodam"))
async def cekkhodam(bot : Client, message : Message):
    khodam = choice(Khodam)
    msg = get_arg(message)
    if message.reply_to_message:
        msg = message.reply_to_message

    if not msg:
        return await message.reply(text="❌ Berikan Saya Pesan / Reply Sebuah Pesan/nama.")

    xx = await message.reply(f"🔍 Sedang Melihat Khodam {msg} ....")
    
    try: 
        Cek-Khodam = "➡️ <b>Khodam {msg}:</b> {khodam}"
        await bot.send_photo(chat_id, khodam, (' > {Cek-Khodam}'), parse_mode=ParseMode.MARKDOWN)
        await xx.delete()
    except BaseException as e:
        return message.reply(f"`{e}`")


print('🔥 [BOT BERHASIL DIAKTIFKAN] 🔥')

bot.run()
