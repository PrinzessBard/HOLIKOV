def get_way(key):

    with open('/home/egor/Work/new_room_navigation/file_way.txt', 'r') as file:
        lines = file.readlines()

    symbols_to_remove = '\n'

    for symbol in symbols_to_remove:
        lines[0] = lines[0].replace(symbol, "")

    for symbol in symbols_to_remove:
        lines[1] = lines[1].replace(symbol, "")

    if key == 'sys':
        return lines[0]
    elif key == 'file':
        return lines[1]


#print(get_way('sys'))
#print(get_way('file'))

