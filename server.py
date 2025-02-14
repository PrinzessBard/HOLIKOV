import sys
sys.path.append('prinzessbard@prinzessbard-laptop:~/Work/HOLIKOV')

from flask import Flask, request, send_file, jsonify
import json
from main import main
import os
from modules.get_way import get_way
 
app = Flask(__name__)

SAVE_FOLDER = get_way('file') + '/data_from_user'

arr = os.listdir("result")

PHOTO_1_PATH = f'result/{arr[0]}'
PHOTO_2_PATH = f'result/{arr[1]}'
os.makedirs(SAVE_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    print("Headers:", request.headers)
    print("Request Data:", request.data)

    try:
        data = request.get_json(force=True)  # force=True для извлечения JSON без проверки Content-Type
        
        # Сохраняем JSON в файл
        file_path = os.path.join(SAVE_FOLDER, 'data.json')
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        main()
        
        return jsonify({"message": "JSON файл успешно сохранен"}), 200
    except Exception as e:
        print("Ошибка:", str(e))
        return jsonify({"error": "Ошибка обработки JSON"}), 400


@app.route('/photo1', methods=['GET'])
def get_photo1():
    s = send_file(PHOTO_1_PATH, mimetype='image/jpeg')
    # os.remove(PHOTO_1_PATH)
    return s

@app.route('/photo2', methods=['GET'])
def get_photo2():
    return send_file(PHOTO_2_PATH, mimetype='image/jpeg')

# @app.route('/photo', methods=['GET'])
# def get_photo():
#     return send_file(PHOTO_PATH, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
