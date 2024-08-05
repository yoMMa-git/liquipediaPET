import json
import requests

base_url = "https://api.liquipedia.net/api/v3/match"

s = requests.Session()
s.headers.update({
    "User-Agent": "MLBBTournamentMeta/1.0",
    "Authorization": "Apikey "
                     "PUT YOURS HERE"
})


def request_matches():
    with open('tournament_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        f.close()

    namefile = open('tournament_names.txt', 'a', encoding='utf-8')

    for elem in data:
        parent = elem['pagename']
        name = (elem['shortname'] or elem['name']).replace(' ', '_')
        print("Added tournament:", name)
        namefile.write(name + '\n')
        with open(f'matches_data/{name}_matches.json', 'w', encoding='utf-8') as f:
            r = s.get(url=base_url, params={
                "wiki": "mobilelegends",
                "conditions": f"[[parent::{parent}]]",
            })
            json.dump(r.json()['result'], f, ensure_ascii=False, indent=4)
            f.close()

    namefile.close()
