import requests

s_city = ',' # for example 'Moscow,Ru'
city_id = 0
appid = '' # your apikey

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
   # print("city:", cities)
    city_id = data['list'][0]['id']
   # print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    info=(data['name'])
    info2=(data['sys']['country'])
    a0=(data['weather'][0]['description'])
    a1=(data['main']["temp"])
    a2=(data['main']['temp_min'])
    a3=(data['main']['temp_max'])
    a4=(data['wind']['speed'])
except Exception as e:
    print("Exception (weather):", e)
    pass
