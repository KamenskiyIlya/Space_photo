import telegram
import urllib3
from environs import Env
import time

from help_scripts import post_photo_in_tg


env = Env()
env.read_env()

CHAT_ID = env.str('CHAT_ID')
BOT = telegram.Bot(token=env.str('TG_BOT_TOKEN'))

if __name__ == '__main__':

	while True:
		try:
			post_photo_in_tg(CHAT_ID, BOT)
			time.sleep(env.int('TIME_SLEEP', 14400))
		except telegram.error.BadRequest as er:
			print(er)