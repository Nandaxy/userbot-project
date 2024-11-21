import requests
import os
import uuid 

def get_uuid():
    return str(uuid.uuid4())  

async def brat(event, args):
    url = f"https://api.ryzendesu.vip/api/sticker/brat?text={args}"


    response = requests.get(url)

    if response.status_code == 200:
 
        file = response.content
        
        if not os.path.exists('temp'):
            os.makedirs('temp')

        file_path = os.path.join('temp', f"{get_uuid()}.webp")
        with open(file_path, 'wb') as f:
            f.write(file)
       
        await event.reply(file=file_path)
        await event.delete()
        os.remove(file_path)
    else:
        await event.respond("Gagal mendapatkan gambar. Coba lagi nanti.")
