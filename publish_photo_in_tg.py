import telegram
import urllib3
from environs import Env
import argparse

from help_scripts import post_photo_in_tg


def get_photo_name():
	parser = argparse.ArgumentParser(description='Post photo in telegram')
	parser.add_argument(
		'-n',
		'--photo_name',
		default=None,
		help='Укажите имя файл, если хотите хотите запостить конкретное фото с указанием разрешения'
	)
	args = parser.parse_args()
	return args

def main():
	env = Env()
	env.read_env()
	chat_id = env.str('CHAT_ID')
	bot = telegram.Bot(token=env.str('TG_BOT_TOKEN'))

	args = get_photo_name()
	post_photo_in_tg(chat_id, bot, args.photo_name)	

if __name__ == '__main__':
	main()

