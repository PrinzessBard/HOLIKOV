import sys
sys.path.append('egor@egor-laptop:~/Work/new_room_navigation/')

import cv2
import os
from modules.from_file import graph_from_file, coordinates_from_file
from modules.dijkstra import dijkstra

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