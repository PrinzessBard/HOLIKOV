import requests

r = requests.post("http://127.0.0.1:/upload", json={"address": "school_3","start_room_name": "Кабинет директора","end_room_name": "Кабинет завуча"})
hui = requests.get("http://62.113.103.41:35366/photo1")
with open('hui.png', 'wb') as file:
    file.write(hui.content)

    # school_3
    # coordinates for red point
    # room_name