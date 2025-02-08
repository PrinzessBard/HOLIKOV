import requests
import json

def get_address(latitude, longitude): # {"latitude": 53.6638986476154, "longitude": 36.4019112515019}

    res = requests.get(f'https://api.geotree.ru/address.php?key=32ZoliIu9n5S&lon={longitude}&lat={latitude}')

    if res.status_code != 200:
        print("Get address from api status", res.status_code)
        return 0
    
    data = json.loads(res.content)

    # Орловская область, Болховский район, город Болхов, Первомайская улица, 145

    try: 
        address = data[0]['value']
    except KeyError:
        print("Get address from api status: error")
        return 0
    
    address = address.replace(",","")
    address = address.replace(" ","")

    print(address)
    #ОрловскаяобластьБолховскийрайонгородБолховПервомайскаяулица145


get_address("53.43204617582237", "36.00893012086987")
