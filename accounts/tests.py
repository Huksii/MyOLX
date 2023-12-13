from django.test import TestCase
import requests

url = "http://192.168.31.61:8080/api/ads/"

response = requests.get(url)

data = response.json()

print(data)

text = f"""
ID : {data[0]["id"]}
Title : {data[0]["title"]}
Descriprion : {data[0]["description"]}
"""