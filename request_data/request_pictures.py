import requests

s = requests.Session()
s.headers.update({
    "User-Agent": "MLBBTournamentMeta/1.0",
})

base_url = "https://www.liquipedia.net/mobilelegends/api.php"

picture_params = {
    "action": "query",
    "generator": "images",
    "gimlimit": 500,
    "titles": "Portal:Heroes",
    "prop": "imageinfo",
    "iiprop": "url",
    "format": "json"
}

r = s.get(url=base_url, params=picture_params)
print(r.json())
for elem in r.json()['query']['pages']:
    link = str(r.json()['query']['pages'][elem]['imageinfo'][0]['url'])
    name = link.split('/')[-1]
    resp = s.get(link)
    if resp.status_code == 200:
        with open(f'../misc/{name}', 'wb') as file:
            file.write(resp.content)
            file.close()
