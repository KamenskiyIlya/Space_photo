import telegram
import urllib3
from environs import Env
import os
from random import choice


if __name__ == '__main__':
	env = Env()
	env.read_env()
	chat_id = env.str('CHAT_ID')
	bot = telegram.Bot(token=env.str('TG_BOT_TOKEN'))

	photo = choice(os.listdir('images'))
	bot.send_photo(chat_id=chat_id, photo=open(f'images/{photo}', 'rb'))