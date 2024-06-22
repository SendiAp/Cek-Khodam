from pyrogram.enums import ParseMode
from pyrogram import Client, filters
from pyrogram.types import *
from config import *
from picture import *
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

PendampingParaRaja = "https://telegra.ph//file/6d9664766fbdb75a2ccca.jpg"
PendampingParaRatu = "https://telegra.ph//file/1c4bf541590a66901b665.jpg"
Naga = "https://telegra.ph//file/f05e380481daee9738cd9.jpg"
HarimauPutih = "https://telegra.ph//file/75459598178c8d51edaa0.jpg"
BuayaPutih = "https://telegra.ph//file/19d24fd99e97cb88898d4.jpg"
MacanTutul = "https://telegra.ph//file/d47160bf296bfe024ea0c.jpg"
RatuUlar = "https://telegra.ph//file/202778df13e12cb652ce1.jpg"
StoplesKaca = "https://telegra.ph//file/6a0a6100cab573248ecac.jpg"
HondaVerza = "https://telegra.ph//file/86571ce13c3a8a1eaeb0a.jpg"
CerminRetak = "https://telegra.ph//file/d886549e633148b515a1e.jpg"

@bot.on_message(filters.command("cekKhodam"))
async def cekkhodam(bot : Client, message : Message):
    khodam = f"{random.choice(Pasukan)}"
    chat_id = message.chat.id
    gambar = f"{khodam}"
    picture = f"{gambar}"
    msg = get_arg(message)
    if message.reply_to_message:
        msg = message.reply_to_message

    text = f"➡️ Khodam {msg}: **{khodam}**"
    if not msg:
        return await message.reply(text="❌ Berikan Saya Pesan / Reply Sebuah Pesan/nama.")

    xx = await message.reply_text(f"🔍 Sedang Melihat Khodam {msg} ....")
    
    try: 
        await bot.send_photo(chat_id, picture, text)
        await xx.delete()
    except BaseException as e:
        return await message.reply_text(f"`{e}`")


print('🔥 [BOT BERHASIL DIAKTIFKAN] 🔥')

bot.run()
