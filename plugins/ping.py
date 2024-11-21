import time
from telethon.tl.functions.users import GetFullUserRequest

async def ping(event):
    start_time = time.time()

    sender_id = event.sender_id  
    sender_full = await event.client(GetFullUserRequest(sender_id))  
    sender_user = sender_full.users[0] 
    username = sender_user.username if sender_user.username else "Unknown"

    message = await event.reply("Checking...")
    end_time = time.time()
    ping_time = int((end_time - start_time) * 1000)

    response_message = (
        f"🏓〄—ᴘᴏɴɢ : {ping_time}ms\n"
        f"🙍‍♂️ Owner: @{username}\n"  
        f"🤖 Bot Name : Zenn Bot"
    )

    await message.edit(response_message)
