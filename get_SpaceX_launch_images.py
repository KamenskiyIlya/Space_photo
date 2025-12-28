import requests
import os
import argparse
from random import choice

from help_scripts import save_images_from_links


def get_cmd_args_spacex():
	parser = argparse.ArgumentParser(description='Download images from SpaceX')
	parser.add_argument(
		'-id',
		'--launch_id',
		default='latest',
		help='Скачивает фото запуска с указанным id, если id не задается, тогда скачиваются фото последнего запуска'
	)
	parser.add_argument(
		'-r',
		'--random_launch',
		type=bool,
		default=False,
		help='Если указать этот параметр как булево значение True, тогда скачаются фото случайного запуска.'
	)
	args = parser.parse_args()
	return args

def get_spacex_launch_images(id='latest', random=False):
	if random:
		url = 'https://api.spacexdata.com/v5/launches/'
		all_lounch_response = requests.get(url)
		all_lounch_response.raise_for_status()
		if 'error' in all_lounch_response:
			raise Exception(response.text)

		response_payload = all_lounch_response.json()
		launches_id = [launch["id"] for launch in response_payload]
		id = choice(launches_id)

	url = f'https://api.spacexdata.com/v5/launches/{id}'
	response = requests.get(url)
	response.raise_for_status()
	if 'error' in response.text:
		raise Exception(response.text)

	response_payload = response.json()
	images_links = response_payload["links"]["flickr"]["original"]

	if not images_links:	
		return 'SpaceX не делала фото этого запуска.'
	elif images_links:	
		save_images_from_links(images_links, path, 'SpaceX_')
	return

if __name__ == '__main__':
	os.makedirs('images', exist_ok=True)
	path = 'images/'
	
	args = get_cmd_args_spacex()

	get_spacex_launch_images(args.launch_id, args.random_launch)