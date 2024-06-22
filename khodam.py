from pyrogram import Client, filters
from config import *
from string import *
import random
import os

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
khodam = random.choice(Khodam)

@bot.on_message(filters.command("cekKhodam"))
async def cekkhodam(bot : Client, message : Message):
    msg = get_arg(message)
    if message.reply_to_message:
        msg = message.reply_to_message

    if not msg:
        return await message.reply(text="❌ Berikan Saya Pesan / Reply Sebuah Pesan/nama.")

    xx = await message.reply(f"🔍 Sedang Melihat Khodam {msg} ....")
    try: 
        Cek-Khodam = "➡️ <b>Khodam {msg}:</b> {khodam}"
        await bot.send_photo(chat_id, khodam, (' > {Cek-Khodam}'))
