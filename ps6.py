import requests
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print(json)

for person in json['people']:
        print(person)
for person in json['people']:
    print('')
    print(person['name'], ":", sep='', end=" ")
    print(person['craft'])