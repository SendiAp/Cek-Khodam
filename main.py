from pyrogram.enums import ParseMode
from pyrogram import Client, filters
from pyrogram.types import *
from db import *
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

ADMINS = [6847847442]

EMOJIS = [
        "👍", "👎", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "🤬", "😢",
        "🎉", "🤩", "🤮", "💩",
        "🙏", "👌", "🕊", "🤡",
        "🥱", "🥴", "😍", "🐳",
        "❤‍🔥", "🌚", "🌭", "💯",
        "🤣", "⚡", "🍌", "🏆",
        "💔", "🤨", "😐", "🍓",
        "🍾", "💋", "🖕", "😈",
        "😴", "😭", "🤓", "👻",
        "👨‍💻", "👀", "🎃", "🙈",
        "😇", "😨", "🤝", "✍",
        "🤗", "🫡", "🎅", "🎄",
        "☃", "💅", "🤪", "🗿",
        "🆒", "💘", "🙉", "🦄",
        "😘", "💊", "🙊", "😎",
        "👾", "🤷‍♂", "🤷", "🤷‍♀",
        "😡"
]

def admins(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        if user_id not in ADMINS:
            p = await message.reply_text(f"❌ <b>Hanya Admins!</b>")
            await p.delete()
            return 
        await func(client, message)
    return wrapper
    
def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

START_TEXT = """
Halo {} , Saya akan membantu🤜🤛 Melihat Khodam/Pendamping mu

Gunakan Perintah:
/cekKhodam - (nama kamu)

👉 Saya juga bisa dimainkan digrub
Jangan lupa dishare ketemanmu🤜
"""

def broadcast(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        broadcast = await get_gcast()
        if user_id not in broadcast:
            await add_gcast(user_id)
        await func(client, message)
    return wrapper

def gcast(func):
    async def wrapper(client, message):
        chat_id = message.chat.id
        broadcast = await get_actived_chats()
        if chat_id not in broadcast:
            await add_actived_chat(chat_id)
        await func(client, message)
    return wrapper
    
@bot.on_message(filters.command("start") & filters.private)
@broadcast
async def start(bot : Client, message : Message):
    name = message.from_user.first_name
    await message.reply(START_TEXT.format(name))
    
@bot.on_message(filters.command("cekKhodam") & filters.private)
async def cekkhodam(bot : Client, message : Message):
    khodam = random.choice(Pasukan)
    kosong = ["Kosong"]
    chat_id = message.chat.id
    msg = get_arg(message)

    text = f"{random.choice(EMOJIS)} {msg} Memiliki Khodam **{khodam}**"
    txt = f"{random.choice(EMOJIS)} Saya Tidak Melihat Khodam {msg} - Artinya Khodam {msg} <b>Kosong</b>"
    if not msg:
        return await message.reply(text="❌ Berikan Saya Sebuah Nama - Contoh /cekKhodam Sabrina")

    xx = await message.reply(f"🔍 Sedang Melihat Khodam {msg} ....")

    if khodam in kosong:
        return await bot.send_photo(chat_id, f"photo/{khodam}.jpg", caption=txt)

    await xx.edit(f"🔍 Sedang Melihat Khodam {msg} ....")
    
    try: 
        await bot.send_photo(chat_id, f"photo/{khodam}.jpg", caption=text)
        await xx.delete()
    except BaseException as e:
        return await message.reply(f"`{e}`")

@bot.on_message(filters.command("cekKhodam") & filters.group)
@gcast
async def cekkhodam(bot : Client, message : Message):
    khodam = random.choice(Pasukan)
    kosong = ["Kosong"]
    chat_id = message.chat.id
    msg = get_arg(message)

    text = f"{random.choice(EMOJIS)} {msg} Memiliki Khodam **{khodam}**"
    txt = f"{random.choice(EMOJIS)} Saya Tidak Melihat Khodam {msg} - Artinya Khodam {msg} <b>Kosong</b>"
    if not msg:
        return await message.reply(text="❌ Berikan Saya Sebuah Nama - Contoh /cekKhodam Sabrina")

    xx = await message.reply(f"🔍 Sedang Melihat Khodam {msg} ....")

    if khodam in kosong:
        return await bot.send_photo(chat_id, f"photo/{khodam}.jpg", caption=txt)

    await xx.edit(f"🔍 Sedang Melihat Khodam {msg} ....")
    
    try: 
        await bot.send_photo(chat_id, f"photo/{khodam}.jpg", caption=text)
        await xx.delete()
    except BaseException as e:
        return await message.reply(f"`{e}`")
        
async def send_msg(chat_id, message: Message):
    try:
        if BROADCAST_AS_COPY is False:
            await message.forward(chat_id=chat_id)
        elif BROADCAST_AS_COPY is True:
            await message.copy(chat_id=chat_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(int(e.value))
        return send_msg(chat_id, message)

@smk.on_message(filters.command("gucast"))
@admins
async def SMProjectUser(bot : Client, message : Message):
    users = await get_gcast()
    msg = get_arg(message)
    if message.reply_to_message:
        msg = message.reply_to_message

    if not msg:
        await message.reply(text="**Reply atau berikan saya sebuah pesan!**")
        return
    
    out = await message.reply(text="**Memulai Broadcast...**")
    
    if not users:
        await out.edit(text="**Maaf, Broadcast Gagal Karena Belum Ada user**")
        return
    
    done = 0
    failed = 0
    for user in users:
        try:
            await send_msg(user, message=msg)
            done += 1
        except:
            failed += 1
    await out.edit(f"✅ **Berhasil Mengirim Pesan Ke {done} User.**\n❌ **Gagal Mengirim Pesan Ke {failed} User.**")

@bot.on_message(filters.command("gcast"))
@admins
async def SMProjectChat(bot : Client, message : Message):
    users = await get_actived_chats()
    msg = get_arg(message)
    if message.reply_to_message:
        msg = message.reply_to_message

    if not msg:
        await message.reply(text="**Reply atau berikan saya sebuah pesan!**")
        return
    
    out = await message.reply(text="**Memulai Broadcast...**")
    
    if not users:
        await out.edit(text="**Maaf, Broadcast Gagal Karena Belum Ada user**")
        return
    
    done = 0
    failed = 0
    for user in users:
        try:
            await send_msg(user, message=msg)
            done += 1
        except:
            failed += 1
    await out.edit(f"✅ **Berhasil Mengirim Pesan Ke {done} User.**\n❌ **Gagal Mengirim Pesan Ke {failed} User.**")
    
print('🔥 [BOT BERHASIL DIAKTIFKAN] 🔥')

bot.run()
