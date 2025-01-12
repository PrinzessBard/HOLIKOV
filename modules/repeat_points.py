import sys
sys.path.append('egor@egor-laptop:~/Work/new_room_navigation/')

from modules.from_file import graph_from_file
from modules.dijkstra import dijkstra
from modules.get_way import get_way

def get_summa_p(start, end, address, room_level):
    def val(i, array_points):
        point_pos = array_points.index(i) + 1
        if point_pos == len(array_points):
            return False
        else:
            number = array_points[(array_points.index(i) + 1)]
            return number

    graph = graph_from_file(f'{get_way('file')}/building/{address}/data/level_{room_level}/graph.txt')

    summa = 0
    array_points = dijkstra(graph, start, end)

    for i in array_points:
        for j in graph[i]:
            point = val(i, array_points)
            if point == False:
                break
            else:
                if point  != j[0]:
                    continue
                else:
                    summa = summa + j[1]

    return summa


def checking_nearby_points(address, sr_param, repeat_name, level):
    d = []
    with open(f"{get_way('file')}/building/{address}/parametres.txt", encoding="utf-8") as file:
        for line in file:
            value = line.split() # ['1', 'Вход_1', '1']
            if value[1] == repeat_name and value[2] == str(level):
                dict = {"number": int(value[0]), "name": value[1], "level": int(value[2])}
                d.append(dict)
            else:
                continue


    weight_value = {}


    for i in range(0, len(d)):
        key = d[i]['number']
        value = get_summa_p(sr_param['number'], key, address, level)
        weight_value[key] = value

    min = list(weight_value.keys())[0]


    for key, item in weight_value.items():
        if item < weight_value[min]:
            min = key
        else:
            continue


    return min
