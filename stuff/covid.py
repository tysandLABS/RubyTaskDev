import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"X-RapidAPI-Key": "40b672c508mshfeca090fbf35a99p1ac94djsn8ee2fc2cd00c",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

# Create a response variable for the API call
response = requests.get(url, headers=headers)

# Store json into a variable
covid_dict = response.json()

print(covid_dict['response'])

for i in covid_dict['response']:
    print(i['country'])

