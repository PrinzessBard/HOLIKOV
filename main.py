import sys
sys.path.append('prinzessbard@prinzessbard-laptop:~/Work/HOLIKOV')
# sys.path.append('root@4258309-vt02952:~/HOLIKOV')

from modules.print_image import draw_path_on_map, save_image
from modules.repeat_points import checking_nearby_points
from modules.room_param import get_room_param
from modules.get_data import get_data
from modules.get_address import get_address
from modules.getUserPos import get_user_pos
from modules.check_room import check_room


# основная функция
def main():
    # try:
    data = get_data()

    latitude = data["coordinates"]['latitude']
    longitude = data["coordinates"]['longitude']

    address = get_address(latitude, longitude)
        # address = "house"
    start_room_name = data['start_room_name'].lower()
    end_room_name = data['end_room_name'].lower()

    if start_room_name == "user":
        start_room_name = get_user_pos(address, "graph")

    sr_param = get_room_param(start_room_name, address) # [number, name, level]
    er_param = get_room_param(end_room_name, address)

    isLift = check_room("Лифт", "53.45162229736113", "35.99646337330341")

    # ladder = "Лифт" if data['isBag'] or data['isDisabled'] and isLift else "Лестница", sr_param['level']
    ladder = "Лестница"

    ladder_1 = checking_nearby_points(address, sr_param, ladder, sr_param['level'])
    ladder_2 = checking_nearby_points(address, er_param, ladder, er_param['level'])

    iter_name = get_room_param(data['iter_room_name'], address)['number'] if data['iter_room_name'] != "" else None

    if sr_param['level'] != er_param['level']:
        for i in range(1, 3):
            if i == 1:
                save_image(address, sr_param['level'], sr_param['number'], ladder_1, i, True if iter_name != None else False, iter_name if iter_name != None else "")
            else:
                save_image(address, er_param['level'], ladder_2, er_param['number'], i, True if iter_name != None else False, iter_name if iter_name != None else "")    

        return (sr_param['level'], er_param['level'])              
    else:
        save_image(address, sr_param['level'], sr_param['number'], er_param['number'], 1, True if iter_name != None else false, iter_name if iter_name != None else "")
        return (sr_param['level'], er_param['level'])    
    # except TypeError:
    #     print("type error (main)")


if __name__ == "__main__":
    main()
