async def userinfo(event):
    user = await event.get_sender()
    await event.reply(f"User Info:\nName: {user.first_name}\nID: {user.id}\nUsername: {user.username}")