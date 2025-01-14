import sys
sys.path.append('egor@egor-laptop:~/Work/new_room_navigation')

from modules.print_image import draw_path_on_map, save_image
from modules.repeat_points import checking_nearby_points
from modules.room_param import get_room_param
from modules.get_data import get_data
from modules.get_address import get_address


# основная функция
def main():
    data = get_data()

    latitude = data["coordinates"]['latitude']
    longitude = data["coordinates"]['longitude']

    address = get_address(latitude, longitude)
    # address = "house"
    start_room_name = data['start_room_name'].lower()
    end_room_name = data['end_room_name'].lower()

    sr_param = get_room_param(start_room_name, address) # [number, name, level]
    er_param = get_room_param(end_room_name, address)

    ladder_1 = checking_nearby_points(address, sr_param, "Лестница", sr_param['level'])
    ladder_2 = checking_nearby_points(address, er_param, "Лестница", er_param['level'])

    if sr_param['level'] != er_param['level']:
        for i in range(1, 3):
            if i == 1:
                save_image(address, sr_param['level'], sr_param['number'], ladder_1)
            else:
                save_image(address, er_param['level'], ladder_2, er_param['number'])                  
    else:
        save_image(address, sr_param['level'], sr_param['number'], er_param['number'])


if __name__ == "__main__":
    main()
