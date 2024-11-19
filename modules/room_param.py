import jellyfish

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
	with open(f"/home/egor/Work/new_room_navigation/building/{address}/parametres.txt", encoding="utf-8") as file:
	    for line in file:
	        value = line.split() # ['1', 'Вход_1', '1']
	        dict = {"number": int(value[0]), "name": value[1], "level": int(value[2])}
	        d.append(dict)

	for item in d:
	    if similar(item["name"], r_name):
	        return item  
	    else:
	        continue