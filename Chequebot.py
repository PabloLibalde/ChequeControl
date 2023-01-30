from os import getenv
from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()



app = Client(
    'controlcheque_bot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
)

from asyncio import run

async def main ():

    await app.start()
    await app.send_message('ketullybrunow','Olá Ketully Gostosa')
    await app.stop()

run(main())