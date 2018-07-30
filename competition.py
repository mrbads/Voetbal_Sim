#!/usr/bin/env python3

import itertools
import random

# Competition File
# -   Standings
# -   Schedule

leagues = [
['Eredivisie',
[['ADO Den Haag', 69],['Ajax', 76],['AZ', 73],['de Graafschap', 60],['Excelsior', 68],
['FC Emmen', 60],['FC Groningen', 68],['FC Utrecht', 72],['Feyenoord', 76],['Fortuna Sittard', 60],['Heracles Almelo', 69],
['NAC Breda', 67],['PEC Zwolle', 70],['PSV', 75],['SC Heerenveen', 70],['Vitesse', 71],['VVV-Venlo', 67],['Willem II', 68]]],
['Eerste Divisie',
[['Almere City FC', 60],['FC Den Bosch', 60],['FC Dordrecht', 60],['FC Eindhoven', 60],['FC Twente', 60],['FC Volendam', 60],
['Go Ahead Eagles', 60],['Helmond Sport', 60],['Jong Ajax', 60],['Jong AZ', 60],['Jong FC Utrecht', 60],['Jong PSV', 60],
['MVV Maastricht', 60],['N.E.C.', 60],['RKC Waalwijk', 60],['Roda JC', 60],['SC Cambuur', 60],['Sparta Rotterdam', 60],
['Telstar', 60],['TOP Oss', 60]]]
]

class Competition(object):
    """docstring for Competition."""
    standings = []

    def __init__(self, arg):
        super(Competition, self).__init__()
        self.arg = arg

    def roster(league):
        print(league[0])
        teams = []
        count = 0
        fixtures = {}
        league = league[1]
        for club in league:
            teams.append(club[0])
        if len(teams) % 2:
            teams.append('Day off')

        matches = itertools.permutations(teams, r=2)
        matches = list(matches)

        for round in range(0, int(len(teams)-1)*2):
            fixtures['Round %s' % round] = []

        # home_teams = random.sample(teams, k=int(len(teams)/2))

        for r,g in fixtures.items():
            count += 1
            print(r)
            print('all possibilities: {}'.format(len(matches)))
            if count % 2:
                # print('odd')
                home_teams = random.sample(teams, k=int(len(teams)/2))
                # print(home_teams)
                used = home_teams.copy()
                for team in home_teams:
                    options = []
                    for match in matches:
                        if match[0] == team:
                            options.append(match)
                    print(options)
                    pick = random.choice(options)
                    if g == []:
                        for i in range(0, len(options)):
                            if pick[1] not in used:
                                print('pick: {}'.format(pick))
                                g.append(pick)
                                used.append(pick[1])
                                matches.remove(pick)
                                break
                            else:
                                pick = random.choice(options)
                    else:
                        print(used)
                        for i in range(0, len(options)):
                            if pick[1] not in used:
                                print('pick: {}'.format(pick))
                                g.append(pick)
                                used.append(pick[1])
                                matches.remove(pick)
                                break
                            else:
                                options.remove(pick)
                                pick = random.choice(options)
            else:
                # print('even')
                away_teams = home_teams
                # print(away_teams)
                used = away_teams.copy()
                for team in away_teams:
                    options = []
                    for match in matches:
                        if match[1] == team:
                            options.append(match)
                    print(options)
                    pick = random.choice(options)
                    if g == []:
                        for i in range(0, len(options)):
                            if pick[0] not in used:
                                print('pick: {}'.format(pick))
                                g.append(pick)
                                used.append(pick[0])
                                matches.remove(pick)
                                break
                            else:
                                pick = random.choice(options)
                    else:
                        print(used)
                        for i in range(0, len(options)):
                            if pick[0] not in used:
                                print('pick: {}'.format(pick))
                                g.append(pick)
                                used.append(pick[0])
                                matches.remove(pick)
                                break
                            else:
                                options.remove(pick)
                                pick = random.choice(options)


        # print('-------------')
        # for r,g in fixtures.items():
        #     print('{} {} {}\n'.format(r,g,len(g)))

if __name__ == '__main__':
    Competition.roster(leagues[0])
