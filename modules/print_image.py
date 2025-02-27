import sys
sys.path.append('prinzessbard@prinzessbard-laptop:~/Work/HOLIKOV')
# sys.path.append('root@4258309-vt02952:~/HOLIKOV')

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

    circle = cv2.circle(
	    image, # the image on which you want to draw a circle
	    needNumber, # centre coordinates
	    20, # radius of circle
	    (0, 0, 255), # color
	    5 # thickness of circle
    )

    return [1, circle]


def draw_path_on_map(image, path, coordinates):
    for i in range(len(path) - 1):
        start_room = path[i]
        end_room = path[i+1]
        start_coord = coordinates[start_room]
        end_coord = coordinates[end_room]
        # Отрисовка линии на изображении карты между двумя точками
        cv2.line(image, start_coord, end_coord, (0, 0, 255), 3, lineType=cv2.LINE_AA)  # красная линия, толщина 3
    return image


# Сохранение готового пути
def save_image(address, room_level,  sr_number, er_number, status, iter, iter_name=None):
    graph = graph_from_file(f'{get_way('file')}/building/{address}/data/level_{room_level}/graph.txt')
    coordinates = coordinates_from_file(f'{get_way('file')}/building/{address}/data/level_{room_level}/coordinates.txt')
    image = cv2.imread(f'{get_way('file')}/building/{address}/image/level_{room_level}.png')

    path = dijkstra(graph, sr_number, er_number)

    print(path)

    result_image = draw_path_on_map(image, path, coordinates)

    # result_circle = draw_pos_user(address, result_image, room_level)


    # if result_circle[0] == 0:
    #     result = result_image
    # elif status == 0:
    #     result = result_image
    # else:
    #     result = result_circle[1]

    output_file = f'{get_way('file')}/result/level_path_{status}.jpg'

    cv2.imwrite(output_file, result_image)

    os.system(f'xdg-open {output_file}') 


# def save_image(address, room_level,  sr_number, er_number, status, iter, iter_name=None):
#     graph = graph_from_file(f'{get_way('file')}/building/{address}/data/level_{room_level}/graph.txt')
#     coordinates = coordinates_from_file(f'{get_way('file')}/building/{address}/data/level_{room_level}/coordinates.txt')
#     image = cv2.imread(f'{get_way('file')}/building/{address}/image/level_{room_level}.jpeg')

#     result = None

#     if iter:
#         path = dijkstra(graph, sr_number, iter_name)

#         result_image = draw_path_on_map(image, path, coordinates)
#         result_circle = draw_pos_user(address, result_image, room_level)

#         path = dijkstra(graph, iter_name, er_number)
#         result = draw_path_on_map(result_circle[1], path, coordinates)
    
#     else:
#         path = dijkstra(graph, sr_number, er_number)

#         result_image = draw_path_on_map(image, path, coordinates)

#         # result_circle = draw_pos_user(address, result_image, room_level)
#         # result = result_circle[1]
#         result = result_image
    
#     output_file = f'{get_way('file')}/result/level_path_{status}.jpg'

#     cv2.imwrite(output_file, result)

#     os.system(f'xdg-open {output_file}') 


