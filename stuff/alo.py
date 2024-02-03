import requests as req

# north_american_countries = {
#     "Canada": {"population": 37590000, "capital": "Ottawa"},
#     "United States": {"population": 331000000, "capital": "Washington, D.C."},
#     "Mexico": {"population": 126200000, "capital": "Mexico City"},
#     "Guatemala": {"population": 17800000, "capital": "Guatemala City"},
#     "Belize": {"population": 400000, "capital": "Belmopan"},
#     "El Salvador": {"population": 6486000, "capital": "San Salvador"},
#     "Honduras": {"population": 9905000, "capital": "Tegucigalpa"},
#     "Nicaragua": {"population": 6540000, "capital": "Managua"},
#     "Costa Rica": {"population": 5094000, "capital": "San José"},
#     "Panama": {"population": 4254000, "capital": "Panama City"},
#     "Colombia": {"population": 50882891, "capital": "Bogotá"},
#     "Venezuela": {"population": 28887118, "capital": "Caracas"},
#     "Ecuador": {"population": 17688599, "capital": "Quito"},
#     "Peru": {"population": 32510453, "capital": "Lima"},
#     "Bolivia": {"population": 11469896, "capital": "La Paz"},
#     "Chile": {"population": 19107216, "capital": "Santiago"},
#     "Argentina": {"population": 45195777, "capital": "Buenos Aires"},
#     "Paraguay": {"population": 7132538, "capital": "Asunción"},
#     "Brazil": {"population": 212559417, "capital": "Brasília"},
#     "Uruguay": {"population": 3473730, "capital": "Montevideo"},
#     "Guyana": {"population": 782766, "capital": "Georgetown"},
#     "Suriname": {"population": 586632, "capital": "Paramaribo"},
#     "French Guiana": {"population": 298682, "capital": "Cayenne"},
#     "Trinidad and Tobago": {"population": 1399488, "capital": "Port of Spain"},
#     "Barbados": {"population": 287025, "capital": "Bridgetown"}
# }

# for countries in north_american_countries:
#         if query == countries:
#             print(countries)        
    
# query = input("Enter a country: ")
# answer = countries(query)
# if (answer):
#     print("The population of", query, "is", answer)
# else:
#     print("No information available for", query)

# list1 = ["wo","ou","wi"]

# list1.reverse()

# print(list1)


# # Operating System List
# systems = ['wi', 'ou', 'wh']
# print('Original List:', systems)

# # List Reverse
# systems.reverse()


# # updated list
# print('Updated List:', systems)


url: str = 'https://checkip.amazonaws.com'
request = req.get(url)
ip: str = request.text

print(ip)