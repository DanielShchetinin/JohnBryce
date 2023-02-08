import requests

url = "https://shazam.p.rapidapi.com/charts/list"

headers = {
	"X-RapidAPI-Key": "d8ea678913mshde17644fe736f04p1c0220jsn27723a5e1e04",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)