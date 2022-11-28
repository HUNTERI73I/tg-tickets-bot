from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

# BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
BOT_TOKEN = "1164761584:AAEsnCW5VerSEEVFH0U76CuOKOBpdKhEYm0"
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
LOG_CHAT = env.str("LOG_CHAT")


HEROKU_APP_NAME = env.str("HEROKU_APP_NAME")

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = env.int('PORT')

WEBHOOK = True
