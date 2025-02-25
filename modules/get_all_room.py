def get_all_room(file, status, level=None):
    old_rooms = {}
    try:
        with open(file, encoding="utf-8") as file:
            for line in file:
                key, *value = line.split()
                old_rooms[key] = value
    except FileNotFoundError:
        print("FileNotFoundError graph_from_file")

    rooms = []

    for key, item in old_rooms.items():
      if status == 'level':
        if item[1] == level:
          rooms.append(item[0])
          continue
        else:
          continue
      
      rooms.append(item[0])
      
    return rooms