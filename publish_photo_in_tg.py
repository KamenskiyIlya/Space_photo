import telegram
import urllib3
from environs import Env


env = Env()
env.read_env()

CHAT_ID = env.str('CHAT_ID')
BOT = telegram.Bot(token=env.str('TG_BOT_TOKEN'))

if __name__ == '__main__':
	post_photo_in_tg(CHAT_ID, BOT)

