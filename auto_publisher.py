import telegram
from environs import Env
import time

from help_scripts import post_photo_in_tg, get_random_photo_name


def main():
	env = Env()
	env.read_env()
	chat_id = env.str('CHAT_ID')
	bot = telegram.Bot(token=env.str('TG_BOT_TOKEN'))
	STANDART_TIME_DELAY = 14400
	delay_time = env.int('DELAY_TIME', STANDART_TIME_DELAY)

	while True:
		try:
			photo_name = get_random_photo_name()
			post_photo_in_tg(chat_id, bot, photo_name)
			time.sleep(delay_time)
		except telegram.error.BadRequest as er:
			print(er)


if __name__ == '__main__':
	main()
