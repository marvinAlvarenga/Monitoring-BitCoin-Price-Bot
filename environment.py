import os

# Chat to send the menssage
CHAT_ID = os.environ['MY_CHAT_ID']

# Bot token
BOT_TOKEN = os.environ['BOT_TOKEN']

BASE_URL = (
    f'https://api.telegram.org/bot{BOT_TOKEN}'
    f'/sendMessage?chat_id={CHAT_ID}'
    '&parse_mode=Markdown&text='
)
