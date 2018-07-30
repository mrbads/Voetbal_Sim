import itertools
import random
import competitions-scheduler

leagues = [
['Eredivisie',
[['ADO Den Haag', 69],['Ajax', 76],['AZ', 73],['de Graafschap', 60]]],
['Eerste Divisie',
[['Almere City FC', 60],['FC Den Bosch', 60],['FC Dordrecht', 60],['FC Eindhoven', 60],['FC Twente', 60],['FC Volendam', 60],
['Go Ahead Eagles', 60],['Helmond Sport', 60],['Jong Ajax', 60],['Jong AZ', 60],['Jong FC Utrecht', 60],['Jong PSV', 60],
['MVV Maastricht', 60],['N.E.C.', 60],['RKC Waalwijk', 60],['Roda JC', 60],['SC Cambuur', 60],['Sparta Rotterdam', 60],
['Telstar', 60],['TOP Oss', 60]]]
]

league = leagues[0]

print(league[0])
teams = []
count = 0
fixtures = {}
league = league[1]
for club in league:
    teams.append(club[0])
if len(teams) % 2:
    teams.append('Day off')

print(teams)
teams = random.sample(teams, k=len(teams))
print(teams)

# use round robin algorithm to generate schedule

class RoundRobin(object):
    """docstring for RoundRobin."""
    def __init__(self, teams, meetings):
        super(RoundRobin, self).__init__()
        if not isinstance(teams, list):
            teams = list(range(1, teams+1))
        if len(teams) % 2 == 1:
            teams.append(None)
        self.teams = teams
        self.meetings = meetings

    @property
    def match_count(self):
        return int(len(self.teams) / 2)

    @property
    def round_count(self):
        return int((len(self.teams) - 1) * self.meetings)

    @property
    def home_teams(self):
        if hasattr(self, '_home_teams'):
            return tuple(self._home_teams)
        else:
            return ()
