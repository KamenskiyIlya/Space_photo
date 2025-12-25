import requests
import os
import argparse
from environs import Env

from help_scripts import save_images_from_links

'''
Предварительная заготовка для дальнейшего тестирования, когда заработает сайт
'''

def get_cmd_args_epic():
	parser = argparse.ArgumentParser(description='Download images from NASA EPIC')
	parser.add_argument(
		'-c',
		'--count',
		default=1,
		help='Укажите какое кол-во фото нужно скачать за раз(не более 13шт)'
	)
	args = parser.parse_args()
	return args

def get_nasa_epic_images(count=1):
	params = {
				'api_key': env.str('NASA_API_KEY', 'DEMO_KEY'),
				'count': count,
	}
	url = 'https://api.nasa.gov/EPIC/api/natural/images'
	params_image_response = requests.get(url, params=params)
	params_image_response.raise_for_status()
	if 'error' in response.text:
		raise Exception(response.text)

	params_image_response_payload = params_image_response.json()
	images_links = []
	counter = 0

	for image in params_image_response_payload:
		if counter > count:
			break
		image_name = params_image_response_payload["image"]
		image_datetime_str = params_image_response_payload["date"]
		image_datetime = datetime.strptime(image_datetime_str, '%Y-%m-%d %H:%M:%S')
		image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_datetime.year}/{image_datetime.month}/{image_datetime.day}/png/{image_name}.png?api_key={params['api_key']}'
		images_links.append(image_url)
		counter += 1


	if not images_links:	
		return 'NASA не смогли прислать фото, попробуйте ещё раз'
	elif images_links:
		save_images_from_links(images_links, path, 'nasa_epic_')
	return

if __name__ == '__main__':
	env = Env()
	env.read_env()

	os.makedirs('images', exist_ok=True)
	path = 'images/'

	args = get_cmd_args_epic()

	get_nasa_epic_images()
