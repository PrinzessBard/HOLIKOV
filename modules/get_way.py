def get_way(key):
    try:
        with open('/root/HOLIKOV/file_way.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("file not found get way")

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

