import cv2
import heapq
import os
import jellyfish


# Алгоритм Дейкстера для нахождения кратчайшего пути по графу
def dijkstra(graph, start, goal):
    queue = [(0, start)]
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == goal:
            break

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    # Восстановление пути
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]

    return path[::-1]  # возвращаем путь в обратном порядке


def similar(first, second):
    first = first.replace(' ', '')
    second = second.replace(' ', '')
    if jellyfish.levenshtein_distance(first, second) > 4:
        return False
    else:
        return True


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


# Прорисовка пути на макете
def draw_path_on_map(image, path, coordinates):
    for i in range(len(path) - 1):
        start_room = path[i]
        end_room = path[i+1]
        start_coord = coordinates[start_room]
        end_coord = coordinates[end_room]
        # Отрисовка линии на изображении карты между двумя точками
        cv2.line(image, start_coord, end_coord, (0, 255, 0), 3)  # красная линия, толщина 3
    return image


# Сохранение готового пути
def save_image(address, room_level,  sr_number, er_number):
    graph = graph_from_file(f'/home/egor/Work/new_room_navigation/building/{address}/data/level_{room_level}/graph.txt')
    coordinates = coordinates_from_file(f'/home/egor/Work/new_room_navigation/building/{address}/data/level_{room_level}/coordinates.txt')
    image = cv2.imread(f'/home/egor/Work/new_room_navigation/building/{address}/image/level_{room_level}.jpg')

    path = dijkstra(graph, sr_number, er_number)

    result_image = draw_path_on_map(image, path, coordinates)

    output_file = f'/home/egor/Work/new_room_navigation/result/level_path_{room_level}.jpg'

    cv2.imwrite(output_file, result_image)

    os.system(f'xdg-open {output_file}') 


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


# основная функция
def main():
	# address = input("Address: ").lower()
	# start_room_name = input("Start room name: ").lower()
	# end_room_name = input("End room name: ").lower()

	address = "school_3"
	start_room_name = "Музыка"
	end_room_name = "Кабинет директора"

	sr_param = get_room_param(start_room_name, address) # [number, name, level]
	er_param = get_room_param(end_room_name, address)

	if sr_param['level'] != er_param['level']:
		print("Successfully !=")
	else:
		save_image(address, sr_param['level'], sr_param['number'], er_param['number'])


if __name__ == "__main__":
    main()