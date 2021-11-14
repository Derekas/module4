import requests, json, urllib3

api_key = "XK1tOiCL9vnkAQXI96aNp9xkpHhXGSWl"
urllib3.disable_warnings()

localidad = input("Introduce la ciudad de la que quiera saber su tiempo: ")

url = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey="+api_key+"&q="+localidad+""
response = requests.request("GET", url, verify=False)
data = json.loads(response.text)
data = dict(data[0])


clave_ciudad = data["Key"]
nombre_ciudad= data["LocalizedName"]
print(clave_ciudad)
url = "http://dataservice.accuweather.com/currentconditions/v1/"+clave_ciudad+"?apikey="+api_key+""
response = requests.request("GET", url, verify=False)
data = json.loads(response.text)
data = dict(data[0])

print("Temperatura de ", nombre_ciudad," : ", data["Temperature"]["Metric"]["Value"])
print("Tiempo: ",data["WeatherText"])