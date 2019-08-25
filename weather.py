import requests
def weather_info(city,units):
 if units:
  base=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=37c3fee1c7ca67429fb65b8c2570fa50&units={units}'
 else:
  base=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=37c3fee1c7ca67429fb65b8c2570fa50'
 return requests.get(base).json()
def quotes_info():
 result=requests.get('http://quotes.rest/qod').json()
 return result


