import requests
import os
import argparse
from environs import Env

from help_scripts import save_images_from_links

'''
Предварительная заготовка для дальнейшей разработки, когда заработает сайт
'''

def get_cmd_args_epic():
	parser = argparse.ArgumentParser(description='Download images from NASA EPIC')
	pass

def get_nasa_epic_images():
	params = {'api_key': env.str('NASA_API_KEY', 'DEMO_KEY')}
	url = 'https://api.nasa.gov/EPIC/api/natural/images'
	response = requests.get(url, params=params)
	response.raise_for_status()
	response_payload = response.json()
	images_links =[payload['hdurl'] for payload in response_payload if 'hdurl' in payload]

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
