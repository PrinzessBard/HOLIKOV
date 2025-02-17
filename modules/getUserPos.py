import sys
# sys.path.append('prinzessbard@prinzessbard-laptop:~/Work/HOLIKOV')
sys.path.append('root@4258309-vt02952:~/HOLIKOV')

from modules.from_file import coordinates_from_file
from modules.room_param import get_room_param
from modules.get_way import get_way
import requests
import json

def get_user_pos(address, status, level=None):
    try:
        hui = requests.get("http://92.255.111.193:8003/api/v1/location_basic/house/test")
        data = json.loads(hui.content)

        room_param = get_room_param(data['data']['loc'], address)
        if level != None:
            if(room_param['level'] != level):
                return [0, 0]

        # number = room_param['number']
        needNumber = 0
        coordinates = coordinates_from_file(f'{get_way('file')}/building/{address}/data/level_{room_param['level']}/coordinates.txt')
        for key, item in coordinates.items():
            if key == room_param['number']:
                needNumber = item
        
        if status == "coordinates":
            return needNumber
        elif status == "graph":
            return room_param['name']
    except TypeError:
        print("Type error (get_user_pos)")
