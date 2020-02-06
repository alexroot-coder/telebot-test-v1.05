# -*- coding: utf-8 -*-
import requests

api = '' #your apiKey

try:
	res = requests.get('https://newsapi.org/v2/top-headlines',
				params = { 'country' : 'ru' , 'apiKey': api})
	data1 = res.json()
	b0=(data1['articles'][0]['title'])
	b1=(data1['articles'][0]['description'])
	b2=(data1['articles'][0]['url'])
except Exception as e:
    print("Exception (find):", e)
    pass

