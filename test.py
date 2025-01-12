import sys
sys.path.append('egor@egor-laptop:~/Work/new_room_navigation/')

import json
import requests
from modules.from_file import graph_from_file, coordinates_from_file
from modules.room_param import get_room_param
import cv2
import os


def draw_pos_user(address, image):
    hui = requests.get("http://217.171.146.102:8003/api/v1/location_basic/house/test")
    data = json.loads(hui.content)
    room_param = get_room_param(data['data']['loc'], address) 
    number = room_param['number']
    needNumber = 0
    coordinates = coordinates_from_file(f'/home/egor/Work/new_room_navigation/building/{address}/data/level_{room_param['level']}/coordinates.txt')
    for key, item in coordinates.items():
        if key == room_param['number']:
            needNumber = item

    # image = cv2.imread(f'/home/egor/Work/new_room_navigation/building/{address}/image/level_{room_param['level']}.jpg')

    circle = cv2.circle(
	    image, # the image on which you want to draw a circle
	    needNumber, # centre coordinates
	    20, # radius of circle
	    (0, 0, 255), # color
	    5 # thickness of circle
    )

    output_file = f'/home/egor/Work/new_room_navigation/result/level_path_{room_param['level']}.jpg'

    cv2.imwrite(output_file, circle)


draw_pos_user('house')

