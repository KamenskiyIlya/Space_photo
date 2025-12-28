import telegram
import urllib3
from environs import Env
import time

from help_scripts import post_photo_in_tg, get_photo_name

def main():
	env = Env()
	env.read_env()
	chat_id = env.str('CHAT_ID')
	bot = telegram.Bot(token=env.str('TG_BOT_TOKEN'))

	while True:
		try:
			photo_name = get_photo_name()
			post_photo_in_tg(chat_id, bot, photo_name)
			time.sleep(env.int('TIME_SLEEP', 14400))
		except telegram.error.BadRequest as er:
			print(er)


if __name__ == '__main__':
	main()

