import requests

r = requests.post("http://127.0.0.1:5000/upload", json={"address": "school_3","start_room_name": "Кабинет директора","end_room_name": "Центр инифиатв"})
hui = requests.get("http://127.0.0.1:5000/photo1")
with open('hui.png', 'wb') as file:
    file.write(hui.content)