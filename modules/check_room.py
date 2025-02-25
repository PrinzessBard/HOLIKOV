import sys
sys.path.append('prinzessbard@prinzessbard-laptop:~/Work/HOLIKOV')

from modules.get_all_room import get_all_room
from modules.get_address import get_address
from modules.get_way import get_way

def check_room(room, latitude, longitude):
    address = get_address(latitude, longitude)
    file = get_way('file') + f'/building/{address}/parametres.txt'
    rooms = get_all_room(file, 'l')

    for i in rooms:
        if room == i:
            return True
        
    return False