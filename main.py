import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH, SESSION_NAME
import handler 

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
self_chatId = None

# Start bot
async def main():
    global self_chatId
    print("Starting bot...")
    await client.start()
    me = await client.get_me()
    self_chatId = me.id
    print(f"Bot is running as {me.username or me.first_name}")
    print(f"Logged in user ID: {self_chatId}")
    handler.setup_handlers(client, self_chatId)
    print("Bot is Running ✅")

    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
