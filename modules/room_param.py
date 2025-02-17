import sys
# sys.path.append('prinzessbard@prinzessbard-laptop:~/Work/HOLIKOV')
sys.path.append('root@4258309-vt02952:~/HOLIKOV')

import jellyfish
from modules.get_way import get_way

def similar(first, second):
    first = first.replace(' ', '')
    second = second.replace(' ', '')
    if jellyfish.levenshtein_distance(first, second) > 4:
        return False
    else:
        return True


# Параметры помещения
def get_room_param(r_name, address):
	d = []
	try:
		with open(f"{get_way('file')}/building/{address}/parametres.txt", encoding="utf-8") as file:
			for line in file:
				value = line.split() # ['1', 'Вход_1', '1']
				dict = {"number": int(value[0]), "name": value[1], "level": int(value[2])}
				d.append(dict)
	except FileNotFoundError:
		print("File not found (get_room_param)")

	for item in d:
	    if similar(item["name"], r_name):
	        return item  
	    else:
	        continue
