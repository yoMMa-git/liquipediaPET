import requests
import json

base_url = 'https://api.liquipedia.net/api/v3/tournament'

s = requests.Session()
s.headers.update({
    "User-Agent": "MLBBTournamentMeta/1.0",
    "Authorization": "Apikey "
                     "PUT YOURS HERE"
})


def request_tournaments():
    r = s.get(url=base_url, params={
        "wiki": "mobilelegends",
        "conditions": "[[participantsnumber::!-1]] AND [[startdate::>2024-01-01]] AND [[liquipediatiertype::!Qualifier]] "
                      "AND [[liquipediatier::<3]]",
        "limit": 100,
        "order": "startdate ASC",
    })

    with open('tournament_data.json', 'w', encoding='utf-8') as f:
        json.dump(r.json()['result'], f, ensure_ascii=False, indent=4)
        f.close()
