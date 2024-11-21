import asyncio
from config import GOMBAL_TEXTS


async def gombal(event):
    message = await event.reply("Sebentar ya, aku mikir dulu...")
    
    for text in GOMBAL_TEXTS:
        await asyncio.sleep(1)
        await message.edit(text)

    await asyncio.sleep(1)
    await message.edit("Tapi Boong")