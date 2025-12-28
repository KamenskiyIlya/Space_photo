import telegram
import urllib3
from environs import Env


def main():
	env = Env()
	env.read_env()
	chat_id = env.str('CHAT_ID')
	bot = telegram.Bot(token=env.str('TG_BOT_TOKEN'))

	text = input('Введите текст сообщения для постинга в группу: ')
	bot.send_message(chat_id=chat_id, text=text)

if __name__ == '__main__':
	main()