import requests
import json

def get_address(latitude, longitude): # {"latitude": 53.6638986476154, "longitude": 36.4019112515019}

    hui = requests.get(f'https://api.geotree.ru/address.php?key=32ZoliIu9n5S&lon={longitude}&lat={latitude}')
    data = json.loads(hui.content)

    # Орловская область, Болховский район, город Болхов, Первомайская улица, 145

    address = data[0]['value']
    address = address.replace(",","")
    address = address.replace(" ","")
    #ОрловскаяобластьБолховскийрайонгородБолховПервомайскаяулица145
    print(address)
    return address
