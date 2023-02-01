from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )

load_dotenv()

list_servers=['177.70.7.254','200.165.132.147']
list_ports=['2013','2014','2015']

app = Client(
    'controlcheque_bot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
    )

teclado = ReplyKeyboardMarkup(
        [
            ['/Lista_Servidores'],
            ['/Reiniciar_Portas']
        ],
        resize_keyboard=True
    )


@app.on_callback_query()
async def callback(client, callback_query):
    pages = {
        'data': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_2'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='page_3'),
            'texto': 'Voce esta na página 1'
        },
        'page_2': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_3'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='data'),
            'texto': 'Voce esta na página 2'
        },
        'page_3': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='data'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='page_2'),
            'texto': 'Voce esta na página 3'
        }
    }
    page = pages[callback_query.data]
    await callback_query.edit_message_text(
        page['texto'], 
        reply_markup=InlineKeyboardMarkup([[
            page['anterior'], page['proximo']
        ]]),
    )
    print(callback_query)
    
@app.on_message(filters.command('Lista_Servidores'))
async def start(client, message):
    global teclado
    callback_data='data'
    
@app.on_message(filters.command('start'))
async def start(client, message):
    global teclado
    await message.reply('Olááá! Bem vindo! \n'
                           'Espero poder lhe ajudar. \n'
                           'Escolha abaixo uma das opções:',
                            reply_markup=teclado)
    

@app.on_message()
async def geral(client, message):
    global teclado
    await message.reply(
        'Escolha abaixo uma das opções',
        reply_markup=teclado
        )

print('Rodando!!')
app.run()