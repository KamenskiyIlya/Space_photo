import requests
import os
import argparse
from environs import Env

from help_scripts import save_images_from_links


def get_cmd_args_apod():
	parser = argparse.ArgumentParser(description='Download images from NASA APOD')
	parser.add_argument(
		'-c',
		'--count',
		type=int,
		default=1,
		help='Укажите какое кол-во фото нужно скачать за раз'
	)
	args = parser.parse_args()
	return args


def get_nasa_apod_images(count=1, api_key):
	params = {
		'api_key': api_key,
		'count': count,
	}
	url = 'https://api.nasa.gov/planetary/apod'
	response = requests.get(url, params=params)
	response.raise_for_status()
	if 'error' in response.text:
		raise Exception(response.text)

	response_payload = response.json()
	images_links = [
		payload['hdurl'] for payload in response_payload
		if 'hdurl' in payload
	]

	if not images_links:
		return 'NASA не смогли прислать фото, попробуйте ещё раз'
	elif images_links:
		save_images_from_links(images_links, path, 'nasa_apod_')
	return


def main():
	env = Env()
	env.read_env()
	api_key = env.str('NASA_API_KEY', 'DEMO_KEY')

	os.makedirs('images', exist_ok=True)
	path = 'images/'

	args = get_cmd_args_apod()

	get_nasa_apod_images(args.count, api_key)


if __name__ == '__main__':
	main()
