import requests
from urllib.parse import urlsplit
import os


def save_images_from_links(links, path, site_name):
	for index, link in enumerate(links):
		response_image = requests.get(link)
		response_image.raise_for_status()
		extension = get_extension_from_url(link)
		with open(f'{path}{site_name}{index}{extension}', 'wb') as file:
			file.write(response_image.content)
			file.close()

def get_extension_from_url(url):
	file_name = urlsplit(url)
	file_name = file_name[2]
	extension = os.path.splitext(file_name)
	extension = extension[1]
	return extension