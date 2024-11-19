import sys
sys.path.append('egor@egor-laptop:~/Work/new_room_navigation')

import json


def get_data():
	with open('data_from_user/data.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
		data = json.load(fh)  #загружаем из файла данные в словарь data

	for key, item in data.items():
		item = item.lower()
		data[key] = item 

	return data