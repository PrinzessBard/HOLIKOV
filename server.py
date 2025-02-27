import sys
sys.path.append('prinzessbard@prinzessbard-laptop:~/Work/HOLIKOV')
# sys.path.append('root@4258309-vt02952:~/HOLIKOV')

from flask import Flask, request, send_file, jsonify, send_from_directory, make_response
from flask_cors import CORS
import json
from main import main
import os
import time
from modules.get_way import get_way
from modules.get_all_room import get_all_room
from modules.get_address import get_address
from modules.get_data import get_data
from modules.get_way import get_way
 
app = Flask(__name__)
CORS(app)

SAVE_FOLDER = get_way('file') + '/data_from_user'

@app.route('/upload', methods=['POST'])
def upload_file():
    print("Headers:", request.headers)
    print("Request Data:", request.data)

    data = request.get_json(force=True)  # force=True для извлечения JSON без проверки Content-Type
        
    # Сохраняем JSON в файл
    file_path = os.path.join(SAVE_FOLDER, 'data.json')
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    level = main()

    print(data["start_room_name"])
        
    return jsonify({"message": level}), 200


@app.route('/list', methods=['GET'])
def get_list():
    data = get_data()
    address = get_address(data['coordinates']['latitude'], data['coordinates']['longitude'])
    file = get_way('file') + f'/building/{address}/parametres.txt'
    rooms = get_all_room(file, 'level' ,'1')

    return jsonify({"message": rooms}), 200



@app.route('/default', methods=['GET'])
def get_photo_default():
    response = make_response(send_from_directory('result', 'level_path_0.jpg'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    # Добавляем уникальный идентификатор файла
    response.headers["X-File-Id"] = str(os.path.getmtime('result/level_path_0.jpg'))
    return response

@app.route('/photo1', methods=['GET'])
def get_photo1():
    response = make_response(send_from_directory('result', 'level_path_1.jpg'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    # Добавляем уникальный идентификатор файла
    response.headers["X-File-Id"] = str(os.path.getmtime('result/level_path_1.jpg'))
    return response


@app.route('/photo2', methods=['GET'])
def get_photo2():
    response = make_response(send_from_directory('result', 'level_path_2.jpg'))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    # Добавляем уникальный идентификатор файла
    response.headers["X-File-Id"] = str(os.path.getmtime('result/level_path_2.jpg'))
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9239)
