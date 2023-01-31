from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )


load_dotenv()

app = Client(
    'controlcheque_bot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
    )


# @app.on_message(filter.command('inline'))
# async def inline(cliente,message):
#     botoes = InlineKeyboardMarkup(
#         [
#             [
#                 InlineKeyboardButton('Callback',callback_data='0')
#                 InlineKeyboardButton(
#                     'Link',
#                     url='https://www.youtube.com/watch?v=bO-ksqJNPXg'
#                     )
                
#             ]
#         ]
#     )




@app.on_message(filters.command('teclado'))
async def teclado(client, message):
    teclado = ReplyKeyboardMarkup(
        [
            ['/ajuda','/Olá!'],
            ['a','b','c']
        ],
        resize_keyboard=True
    )    
    await message.reply(
        'Teclado!',
        reply_markup=teclado,
        )



@app.on_message(filters.command('Start'))
async def messages(client, message):
    print(message.chat.username, message.text)
    await message.reply('Bem vindo!!')

@app.on_message()
async def messages(client, message):
    print(message.chat.username, message.text)
    await message.reply(message.text + '???')
    

async def main ():
    await app.start()
    await app.send_message('Joaojt','AI é bicho doidoo!!!')
    await app.stop()

app.run()
print('Rodando!!')