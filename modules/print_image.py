import sys
sys.path.append('egor@egor-laptop:~/Work/new_room_navigation/')

import cv2
import os
from modules.from_file import graph_from_file, coordinates_from_file
from modules.dijkstra import dijkstra
from modules.room_param import get_room_param
from modules.get_way import get_way
from modules.getUserPos import get_user_pos


def draw_pos_user(address, image, level):
    needNumber = get_user_pos(address, "coordinates", level)

    if needNumber == [0, 0]:
        return needNumber

    # image = cv2.imread(f'/home/egor/Work/new_room_navigation/building/{address}/image/level_{room_param['level']}.jpg')

    circle = cv2.circle(
	    image, # the image on which you want to draw a circle
	    needNumber, # centre coordinates
	    20, # radius of circle
	    (0, 0, 255), # color
	    5 # thickness of circle
    )

    return [1, circle]

    # output_file = f'/home/egor/Work/new_room_navigation/result/level_path_{level}.jpg'

#    cv2.imwrite(output_file, circle)


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
def save_image(address, room_level,  sr_number, er_number, status):
    graph = graph_from_file(f'{get_way('file')}/building/{address}/data/level_{room_level}/graph.txt')
    coordinates = coordinates_from_file(f'{get_way('file')}/building/{address}/data/level_{room_level}/coordinates.txt')
    image = cv2.imread(f'{get_way('file')}/building/{address}/image/level_{room_level}.jpg')

    path = dijkstra(graph, sr_number, er_number)

    result = 0

    result_image = draw_path_on_map(image, path, coordinates)

    result_circle = draw_pos_user(address, result_image, room_level)

    if result_circle[0] == 0:
        result = result_image
    elif status == 0:
        result = result_image
    else:
        result = result_circle[1]

    output_file = f'{get_way('file')}/result/level_path_{room_level}.jpg'

    cv2.imwrite(output_file, result)

    os.system(f'xdg-open {output_file}') 
