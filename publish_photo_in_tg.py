import telegram
import urllib3
from environs import Env
import argparse

from help_scripts import post_photo_in_tg


env = Env()
env.read_env()

CHAT_ID = env.str('CHAT_ID')
BOT = telegram.Bot(token=env.str('TG_BOT_TOKEN'))

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

if __name__ == '__main__':
	args = get_photo_name()
	post_photo_in_tg(CHAT_ID, BOT, args.photo_name)

