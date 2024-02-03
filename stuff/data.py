import requests
import json
# des = input("Enter destination: ")
# origin = input("Enter origin: ")


url = "https://api.travelpayouts.com/v2/prices/month-matrix"

strings = {"currency":"usd","show_to_affiliates":"true","origin":"NYC","destination":"WAS"}

querystring = strings


headers = {'x-access-token': '2160a9f9ca2fa3d348f4a3a32504538e'}


response = requests.request("GET", url, headers=headers, params=querystring)

# data = response.json

# print(type(data))

data = json.loads(response.text)

print(data.get('data', [])[0].get(''))
    
# for i in data['data']:
#     if i['depart_date'] == '2023-11-26':
#         print(i)
