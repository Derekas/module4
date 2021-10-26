
import requests,json
import urllib3
urllib3.disable_warnings()
url = "https://api.covid19tracking.narrativa.com/api/countries"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))

data["countries"][29]["name"]

for i in data["countries"]:
    print(i["id"],"->",i["name_es"])

country =input("Input id of a country:")
url_regions = "https://api.covid19tracking.narrativa.com/api/countries/"+country+"/regions"
response = requests.request("GET", url_regions, verify=False)
data = dict(json.loads(response.text))
for elem in data["countries"][0][country]:
    print(elem["name_es"])
