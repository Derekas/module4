import requests,json
import urllib3
urllib3.disable_warnings()
url = "https://api.covid19tracking.narrativa.com/api/2021-10-22/country/spain"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))

data_spain=data["dates"]["2021-10-22"]["countries"]["Spain"]
data_global=data["total"] 

print("Global Data:")
print("----------")

print("Country", "Confirmed", "Today Confirmed", "Deaths", "Today's Deaths", sep="\t")