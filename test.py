start_room_name = "Музыка"

d = []
with open(f"/home/egor/Work/new_room_navigation/building/school_3/parametres.txt", encoding="utf-8") as file:
    for line in file:
        value = line.split() # ['1', 'Вход_1', '1']
        dict = {"number": int(value[0]), "name": value[1], "level": int(value[2])}
        d.append(dict)

for item in d:
    if item["name"] == start_room_name:
        print(item)  
    else:
        continue
