import requests
import json

res = requests.get("http://92.255.111.193:8003/api/v1/location_basic/level/test")
data = json.loads(res.content)
print(data)
