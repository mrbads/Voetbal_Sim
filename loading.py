#!/usr/bin/env python3

import pickle

from manager import Manager

# loading file
# -   create/load career mode

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

class Load(object):
    """docstring for Load."""
    def __init__(self):
        super(Load, self).__init__()


    def create(self):
        print('new Career mode')
        club, teams, league = self.team_selection()
        manager = Manager(club, teams, league)
        manager.menu()

    def load(self):
        with open('data.pickle', 'rb') as f:
        # The protocol version used is detected automatically, so we do not
        # have to specify it.
            data = pickle.load(f)
        manager = Manager(data.club.name, data.teams, data.league, data.fixtures, data.played, data.competition, new=False)
        manager.menu()

    def team_selection(self):
        print('Choose your league: ')
        for league in range(1,len(leagues)+1):
            print('[{}] - {}'.format(league, leagues[league-1][0]))
        option = int(input('Your choice: '))
        print(leagues[option-1][0])
        league = leagues[option-1]
        print('Choose your team: ')
        for teams in range(1, len(league[1])+1):
            print('[{}] - {}'.format(teams, league[1][teams-1][0]))
        option = int(input('Your choice: '))
        print(league[1][option-1][0])
        club = league[1][option-1][0]
        teams = league[1]
        return(club, teams, league)
