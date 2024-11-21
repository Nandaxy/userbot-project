from datetime import datetime, timedelta

# AFK status
afk_status = {
    "is_afk": False,
    "reason": "",
    "duration": None, 
    "start_time": None,
    "end_time": None,
}


def parse_duration(duration_str):
    try:
        unit = duration_str[-1]  
        value = int(duration_str[:-1])  
        
        if unit == 's':
            return timedelta(seconds=value)
        elif unit == 'm':
            return timedelta(minutes=value)
        elif unit == 'h':
            return timedelta(hours=value)
        elif unit == 'd':
            return timedelta(days=value)
        else:
            raise ValueError("Durasi tidak valid (gunakan s, m, h, atau d).")
    except Exception:
        raise ValueError("Format durasi tidak valid. Gunakan format seperti 1s, 1m, 1h, atau 1d.")

async def set_afk(event, reason, duration=None):
    # print(reason)
    afk_status["is_afk"] = True
    afk_status["reason"] = reason
    afk_status["start_time"] = datetime.now()

    if duration:  
        try:
            parsed_duration = parse_duration(duration)
            afk_status["duration"] = parsed_duration
            afk_status["end_time"] = datetime.now() + parsed_duration
        except ValueError as e:
            await event.reply(f"Error: {e}")
            return
    else:
        afk_status["duration"] = None  
        afk_status["end_time"] = None

    response_message = (
        f"AFK mode activated.\n"
        f"📄 Alasan: {reason}\n"
        f"⏳ Durasi: {duration if duration else '-'}"
    )
    await event.reply(response_message)

async def remove_afk(event, notify):
    if not afk_status["is_afk"]:
        await event.reply("Sedang Tidak AFK.")
        return

    afk_status["is_afk"] = False
    afk_status["reason"] = ""
    afk_status["duration"] = None
    afk_status["start_time"] = None
    afk_status["end_time"] = None
    
    if notify:
        await event.reply("AFK mode deactivated.")

async def afk_reply(event):
    # print(event)
    if not event.is_private:
        return

    if afk_status["is_afk"]:
        now = datetime.now()
        reason = afk_status["reason"]
        start_time = afk_status["start_time"]

      
        if "end_time" in afk_status and afk_status["end_time"] and now > afk_status["end_time"]:
            await remove_afk(event, notify=False)
            return  

        elapsed_time = now - start_time
        hours, remainder = divmod(elapsed_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)


    
        response_message = (
            f"Sedang AFK.\n"
            f"📄 Alasan: {reason}\n"
            f"🕒 Sejak: {hours}h, {minutes}m, {seconds}s\n"
        )
        
        if afk_status["duration"]:
            response_message += f"⏳ Durasi: {afk_status['duration'] if afk_status['duration'] else '-'}\n"
       

        if afk_status["end_time"]:
            remaining_time = afk_status["end_time"] - now
            response_message += f"⏳ Sisa waktu: {remaining_time}.\n"
        await event.reply(response_message)

