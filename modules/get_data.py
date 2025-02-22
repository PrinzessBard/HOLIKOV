import sys
# sys.path.append('prinzessbard@prinzessbard-laptop:~/Work/HOLIKOV')
sys.path.append('root@4258309-vt02952:~/HOLIKOV')

import json


def get_data():
	try:
		with open('data_from_user/data.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
			data = json.load(fh)  #загружаем из файла данные в словарь data
	except FileNotFoundError:
		print("FileNotFoundError (get_data)")

	for key, item in data.items():
		# item = item.lower()
		data[key] = item 

	return data # {'coordinates': {'latitude': '53.6638986476154', 'longitude': '36.4019112515019'}, 'start_room_name': 'гостиная', 'end_room_name': 'серверная'}

