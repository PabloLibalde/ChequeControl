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


@app.on_callback_query()
def callback(client, callback_query):
    if callback_query.data =='Servidores':
        
        servidor_texto = 'Selecione um servidor'
        lista_servidores = [
            [
                InlineKeyboardButton('server 192.168.1.10', callback_data='192.168.1.10'),
                InlineKeyboardButton('server 192.168.1.11', callback_data='192.168.1.11')
            ],
            [
                InlineKeyboardButton('server 192.168.1.12', callback_data='192.168.1.12'),
                InlineKeyboardButton('server 192.168.1.13', callback_data='192.168.1.13')
            ],
            [
                InlineKeyboardButton('Retornar', callback_data='servidores' )
            ]
        ]
        
        callback_query.edit_message_text(
            servidor_texto,
            repy_markup = InlineKeyboardMarkup(
                lista_servidores
            )
        )
    
    
    
    # pages = {
    #     'lista_servidores': {
    #         '192.168.1.10': InlineKeyboardButton('server 192.168.1.10', callback_data='192.168.1.10'),
    #         '192.168.1.11': InlineKeyboardButton('server 192.168.1.11', callback_data='192.168.1.11'),
    #         '192.168.1.12': InlineKeyboardButton('server 192.168.1.12', callback_data='192.168.1.12'),
    #         '192.168.1.13': InlineKeyboardButton('server 192.168.1.13', callback_data='192.168.1.13'),
    #         'texto': 'Selecione um servidor'
        # },
        # '192.168.1.10':{
        #     'anchieta': InlineKeyboardButton('Anchieta', text= 'Reiniciar'),
        #     'itapemirim': InlineKeyboardButton('Itapemirim', text= 'Reiniciar'),
        #     'afonso claudio': InlineKeyboardButton('Afonso Claudio', text= 'Reiniciar'),
        #     'guarapari': InlineKeyboardButton('Guarapari', text= 'Reiniciar'),
        #     'retornar': InlineKeyboardButton('Retornar', callback_data='servidores'),
        #     'texto': 'Voce esta no servidor 192.168.1.10'
        # },
        # '192.168.1.11':{
        #     'sdn': InlineKeyboardButton('Sao Domingos', text= 'Reiniciar'),
        #     'sgp': InlineKeyboardButton('Sao Gabriel da Palha', text= 'Reiniciar'),
        #     'iconha': InlineKeyboardButton('Iconha', text= 'Reiniciar'),
        #     'retornar': InlineKeyboardButton('Retornar', callback_data='servidores'),
        #     'texto': 'Voce esta no servidor 192.168.1.11'            
        # },
        # '192.168.1.12':{
        #     'viana': InlineKeyboardButton('Viana', text= 'Reiniciar'),
        #     'retornar': InlineKeyboardButton('Retornar', callback_data='servidores'),
        #     'texto': 'Voce esta no servidor 192.168.1.12'            
        # },
        # '192.168.1.13':{
        #     'serra': InlineKeyboardButton('Serra', text= 'Reiniciar'),
        #     'retornar': InlineKeyboardButton('Retornar', callback_data='servidores'),
        #     'texto': 'Voce esta no servidor 192.168.1.13'            
        # }        
    # }
    # page = pages[callback_query.data]
    # print(page)
    # print('-'*10)
    # print(page.values)
    # print('-'*10)
    # print(page['192.168.1.10'])
    # print('-'*10)
    # print('-'*10)
    # await callback_query.edit_message_text(
    #     page['texto'],
    #     reply_markup = InlineKeyboardMarkup([
    #     [
    #         page['192.168.1.10'],
    #         page['192.168.1.11']
    #     ],
    #     [
    #         page['192.168.1.12'],
    #         page['192.168.1.13']
    #     ]
    #     ])
    # )

@app.on_callback_query()
def callback(client, callback_query):
    pages = {
        '192.168.1.10':{
            'anchieta': InlineKeyboardButton('Anchieta', text= 'Reiniciar'),
            'itapemirim': InlineKeyboardButton('Itapemirim', text= 'Reiniciar'),
            'afonso claudio': InlineKeyboardButton('Afonso Claudio', text= 'Reiniciar'),
            'guarapari': InlineKeyboardButton('Guarapari', text= 'Reiniciar'),
            'retornar': InlineKeyboardButton('Retornar', callback_data='servidores'),
            'texto': 'Voce esta no servidor 192.168.1.10'
        }
    }
    page = pages[callback_query.data]
    callback_query.edit_message_text(
        page['texto'],
        reply_markup = InlineKeyboardMarkup([
         [
             page['anchieta'],
             page['itapemirim']
         ],
         [
             page['afonso claudio'],
             page['guarapari']
         ]
        ])
    )
    
    
    

@app.on_message(filters.command('servidores'))
async def servidores(client, message):
    botoes = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Servidores', callback_data='lista_servidores'),
                InlineKeyboardButton('Nada', callback_data='estado1')                
            ]
        ]
    )
    await message.reply(
        'Teclado!',
        reply_markup=botoes,
        )




@app.on_message(filters.command('teclado'))
async def teclado(client, message):
    teclado = ReplyKeyboardMarkup(
        [
            ['/inline','/Olá!'],
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
    



print('Rodando!!')
app.run()
