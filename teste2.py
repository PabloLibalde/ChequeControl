from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

load_dotenv()


app = Client(
    'controlcheque_bot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
    )


REPLY_MESSAGE = 'Mensagem Reply (Botoes de baixo, rodapé)'    
REPLY_MESSAGE_BUTTONS = [
    [
        ('/servidores')
    ]
]    


#Função Start
@app.on_message(filters.command('start') & filters.private) #Criado o comando
def start(bot, message): #Criado a função
    bot.send_message(message.chat.id, "Olá, bem vindo ao Bot.") # Resposta do metodo
    message.reply(
        text="vou chamar o /Menu para ti!!",
        reply_markup=ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    )
    
    
#ReplyKeyboards, Botões de baixo, redapé


@app.on_message(filters.command('menu'))
def menu(bot, message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )
    
#Função InlineButtons, botões da tela



# @app.on_message(filters.command('Servidores') & filters.private)
# def lista_servidores(bot, message):

# message.reply(
#         text=text,
#         reply_markup=reply_markup,
#         disable_web_page_preview=True

#função HELP    
@app.on_message(filters.command('help')) 
def command1(bot, message): 
    message.reply_text(" Função HELP do Bot Sessão") 
    
#CallBack Query

SERVIDORES_MESSAGE = 'Escolha um dos servidores abaixo.'
SERVIDORES_BUTTONS = [
    [
        InlineKeyboardButton('IP 1.10', callback_data='192.168.1.10')
    ],
    [
        InlineKeyboardButton('IP 2.12', callback_data='192.168.2.12')
    ]
]       

@app.on_message(filters.command('servidores') & filters.private)
def servidores(bot, message):
    message.reply(
        text=SERVIDORES_MESSAGE,
        reply_markup = InlineKeyboardMarkup(SERVIDORES_BUTTONS)
    )
    
@app.on_callback_query()
def callback_query(client, callbackquery):
    if callbackquery.data == '192.168.1.10':
        
        SERVER1_TEXT = 'Servidor 192.168.1.10'
        SERVER1_BUTTON = [
            [
                InlineKeyboardButton('Anchieta', callback_data='anchieta'),
                InlineKeyboardButton('Guarapari', callback_data='guarapari'),
                InlineKeyboardButton('Voltar', callback_data='Servidores')
            ]
        ]
        
        callbackquery.edit_message_text(
            SERVER1_TEXT,
            reply_markup = InlineKeyboardMarkup(SERVER1_BUTTON)
        )

    elif callbackquery.data == '192.168.2.12':
        
        SERVER1_TEXT = 'Servidor 192.168.2.12'
        SERVER1_BUTTON = [
            [
                InlineKeyboardButton('SGP', callback_data='sgp'),
                InlineKeyboardButton('SDN', callback_data='sdn'),
                InlineKeyboardButton('Voltar', callback_data='Servidores')
            ]
        ]
        
        callbackquery.edit_message_text(
            SERVER1_TEXT,
            reply_markup = InlineKeyboardMarkup(SERVER1_BUTTON)
        )
    elif callbackquery.data == 'Servidores':
        callbackquery.edit_message_text(
            SERVIDORES_MESSAGE,
            reply_markup = InlineKeyboardMarkup(SERVIDORES_BUTTONS)
        )

        
        


#echobot
@app.on_message(filters.text & filters.private)
def echobot(client, message):
    message.reply_text(f'{message.text} - Opção Invalida')
    message.reply(
        text="vou chamar o /Menu para ti!!",
        reply_markup=ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    )
    
    
print("Bot Rodando!!!")
app.run()