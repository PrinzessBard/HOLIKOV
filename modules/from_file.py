def graph_from_file(file):
    graph = {}
    with open(file, encoding="utf-8") as file:
        for line in file:
            key, *value = line.split()
            graph[key] = value

    new_graph = {}
    for key, item in graph.items():
        new_key = int(key)
        new_graph[new_key] = [[int(item[0]), int(item[1])], [int(item[2]), int(item[3])], [int(item[4]), int(item[5])], [int(item[6]), int(item[7])]]



    for key, item in new_graph.items():
        for i in item:
            for j in item:
                if j[0] == 0 and j[1] == 0:
                    item.remove(j) 
                else:
                    pass

     
    return new_graph


# Функция для получения словаря координат из файла
def coordinates_from_file(file):
    coordinates = {}
    with open(file, encoding="utf-8") as file:
        for line in file:
            key, *value = line.split()
            coordinates[key] = value

    new_coordinates = {}
    for key, item in coordinates.items():
        new_key = int(key)
        new_coordinates[new_key] = (int(item[0]), int(item[1]))

    return new_coordinates
