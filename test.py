import requests
import json

hui = requests.get("https://api.geotree.ru/address.php?key=32ZoliIu9n5S&lon=36.00893012086987&lat=53.43204617582237")
data = json.loads(hui.content)

# Орловская область, Болховский район, город Болхов, Первомайская улица, 145

address = data[0]['value']
address = address.replace(",","")
address = address.replace(" ","")
#ОрловскаяобластьБолховскийрайонгородБолховПервомайскаяулица145
print(address)