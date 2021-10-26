import requests,json
import urllib3
urllib3.disable_warnings()
url = "https://api.covid19tracking.narrativa.com/api/countries/spain/regions"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))
print("Spain Regions")
print("--------")
sort=[]
for elem in data["countries"][0]["spain"]:
    sort.append(elem["name"])

sort=sorted(sort)
for elem in sort:
    print(elem)    