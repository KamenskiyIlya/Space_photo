import requests
from urllib.parse import urlsplit
import os
from random import choice


def save_images_from_links(links, path, site_name, params=None):
	for index, link in enumerate(links):
		response_image = requests.get(link, params=params)
		response_image.raise_for_status()

		extension = get_extension_from_url(link)
		with open(f'{path}{site_name}{index}{extension}', 'wb') as file:
			file.write(response_image.content)


def get_extension_from_url(url):
	file_name = urlsplit(url)
	file_name = file_name[2]
	extension = os.path.splitext(file_name)
	extension = extension[1]
	return extension


def post_photo_in_tg(chat_id, bot, photo_name):
	with open(f'images/{photo_name}', 'rb') as photo:
		bot.send_photo(chat_id=chat_id, photo=photo)
	return


def get_photo_name(photo_name=None):
	if not photo_name:
		photo_name = choice(os.listdir('images'))
	return photo_name
