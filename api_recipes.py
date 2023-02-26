import requests

url = "https://edamam-recipe-search.p.rapidapi.com/search"

querystring = {"q":"chicken"}

headers = {
	"X-RapidAPI-Key": "f477a3a207msh82c9aa8b4c4bb07p121851jsn6f6f818c4162",
	"X-RapidAPI-Host": "edamam-recipe-search.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)