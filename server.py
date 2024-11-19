from flask import Flask, request, send_file, jsonify
import json
from main import main
import os
 
app = Flask(__name__)

SAVE_FOLDER = '/home/egor/Work/new_room_navigation/data_from_user'

arr = os.listdir("result")

PHOTO_1_PATH = f'resukt/{arr[0]}'
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
    return send_file(PHOTO_1_PATH, mimetype='image/jpeg')

@app.route('/photo2', methods=['GET'])
def get_photo2():
    return send_file(PHOTO_2_PATH, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True, port=5000)