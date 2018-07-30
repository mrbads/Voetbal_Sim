#!/usr/bin/env python3

from roundrobin import RoundRobinScheduler

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
        league = league[1]
        for club in league:
            teams.append(club[0])
        if len(teams) % 2:
            teams.append('Day off')

        RR = RoundRobinScheduler(teams, 2)
        return RR.generate_schedule()

if __name__ == '__main__':
    Competition.roster(leagues[0])
