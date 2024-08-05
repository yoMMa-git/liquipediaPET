import json


def analyze_matches():
    namefile = open('tournament_names.txt', 'r', encoding='utf-8')

    heroes_pick_dict = {}
    heroes_ban_dict = {}
    total_matches = 0

    for tourney in namefile.read().splitlines():
        try:
            with open(f'matches_data/{tourney}_matches.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for match in data:
                    if match['winner']:  # if match has already been played
                        for game in match['match2games']:
                            heroes = game['extradata']
                            del heroes['team1side'], heroes['team2side']
                            if heroes:
                                for hero in heroes:
                                    if hero.find('ban') > 0:
                                        if heroes[hero] in heroes_ban_dict:
                                            heroes_ban_dict[heroes[hero]] += 1
                                        else:
                                            heroes_ban_dict.setdefault(heroes[hero], 1)
                                    elif hero.find('champion') > 0:
                                        if heroes[hero] in heroes_pick_dict:
                                            heroes_pick_dict[heroes[hero]] += 1
                                        else:
                                            heroes_pick_dict.setdefault(heroes[hero], 1)
                                total_matches += 1
                f.close()
        except NameError:
            print(f"{tourney} doesn't exist!")

    # print("PICK: ", sorted(heroes_pick_dict.items(), key=lambda x: x[1], reverse=True))
    # print("BAN: ", sorted(heroes_ban_dict.items(), key=lambda x: x[1], reverse=True))
    # print("Total matches: ", total_matches)

    with open('results.json', 'w', encoding='utf-8') as rf:
        json.dump([{"picks": heroes_pick_dict}, {"bans": heroes_ban_dict}, {"matches": total_matches}], rf,
                  ensure_ascii=False, indent=4)
        rf.close()
