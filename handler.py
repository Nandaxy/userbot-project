from telethon import events
from plugins.ping import ping
from plugins.gombal import gombal
from plugins.helikopter import helikopter
from plugins.afk import set_afk, remove_afk, afk_reply
from plugins.brat import brat
from plugins.userinfo import userinfo

def is_self_user(event, self_chatId):
    return event.sender_id == self_chatId

def setup_handlers(client, self_chatId):
    @client.on(events.NewMessage(pattern=r'\.ping'))
    async def ping_event(event):
        if not is_self_user(event, self_chatId):
            return
        await ping(event)

    @client.on(events.NewMessage(pattern=r'\.gombal'))
    async def gombal_event(event):
        if not is_self_user(event, self_chatId):
            return
        await gombal(event)

    @client.on(events.NewMessage(pattern=r'\.helikopter'))
    async def helikopter_event(event):
        if not is_self_user(event, self_chatId):
            return
        await helikopter(event)
      

    @client.on(events.NewMessage(pattern=r'\.afk (.*)'))
    async def afk_event(event):
        if not is_self_user(event, self_chatId):
            return
        args = event.pattern_match.group(1).strip()
        if '|' in args:
            reason, duration = args.split('|', 1)
        else:
            reason = args
            duration = None  
        await set_afk(event, reason, duration)

    @client.on(events.NewMessage(pattern=r'\.back'))
    async def back_event(event):
        if not is_self_user(event, self_chatId):
            return
        await remove_afk(event, notify=True)

    @client.on(events.NewMessage(incoming=True))
    async def afk_reply_event(event):
        await afk_reply(event)
        
    @client.on(events.NewMessage(pattern=r'\.brat (.*)' ))
    async def brat_event(event):
        if not is_self_user(event, self_chatId):
            return
        args = event.pattern_match.group(1).strip()
        
        await brat(event, args)

    @client.on(events.NewMessage(pattern=r'\.userinfo'))
    async def userinfo_event(event):
        if not is_self_user(event, self_chatId):
            return
        await userinfo(event)