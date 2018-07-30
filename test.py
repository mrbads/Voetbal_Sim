from __future__ import print_function, unicode_literals

import itertools
import random
import copy

from __init__ import ScheduleGenerationFailed, NoMatchFound
from scheduler import Scheduler

leagues = [
['Eredivisie',
[['ADO Den Haag', 69],['Ajax', 76],['AZ', 73],['de Graafschap', 60]]],
['Eerste Divisie',
[['Almere City FC', 60],['FC Den Bosch', 60],['FC Dordrecht', 60],['FC Eindhoven', 60],['FC Twente', 60],['FC Volendam', 60],
['Go Ahead Eagles', 60],['Helmond Sport', 60],['Jong Ajax', 60],['Jong AZ', 60],['Jong FC Utrecht', 60],['Jong PSV', 60],
['MVV Maastricht', 60],['N.E.C.', 60],['RKC Waalwijk', 60],['Roda JC', 60],['SC Cambuur', 60],['Sparta Rotterdam', 60],
['Telstar', 60],['TOP Oss', 60]]]
]


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

    def _generate_home_teams(self, home_teams=None):
        team_count = len(self.teams)
        odd_team_count = None in self.teams

        if not home_teams:
            if odd_team_count:
                home_count = (team_count - 1 ) // 2
                homes = random.sample(range(team_count - 1), home_count)
                homes.append(team_count - 1)
            else:
                home_count = team_count // 2
                homes = random.sample(range(team_count), home_count)
            self._home_teams = [self.teams[i] for i in homes]
        else:
            self._home_teams = home_teams
            homes = [self.teams.index(home) for home in home_teams]

        return homes

    def generate_matrix(self, home_teams=None):
        team_count = len(self.teams)
        home_at_home = team_count // 2
        away_at_home = (team_count - 1) // 2
        odd_team_count = None in self.teams
        homes = self._generate_home_teams(home_teams)
        matrix = [[None] * team_count for __ in range(team_count)]
        for i in range(team_count - 1):
            home_team = i in homes
            home_count = (away_at_home
                            if not home_team or odd_team_count else home_at_home)
            home_count -= matrix[i].count(True)
            try:
                if odd_team_count:
                    home_opps = random.sample(list(range(i + 1, team_count - 1)),
                                                home_count)
                    if home_team:
                        home_opps.append(team_count - 1)
                else:
                    home_opps = random.sample(list(range(i + 1, team_count)),
                                                home_count)
                for opp in range(i + 1, team_count):
                    is_home = opp in home_opps
                    matrix[i][opp] = is_home
                    matrix[opp][i] = not is_home
            except ValueError:
                return self.generate_matrix(home_teams=home_teams)
        return matrix

    def _generate_even_matches(self, evens):
        return [(team, opp)
                for team  in self.teams
                for opp in self.teams
                if team != opp] * evens

    def _generate_odd_matches(self, home_teams=None):
        matrix = self.generate_matrix(home_teams=home_teams)
        matches = []
        for team_idx in range(len(self.teams)):
            for opp_idx in range(team_idx + 1, len(self.teams)):
                if matrix[team_idx][opp_idx]:
                    matches.append((self.teams[team_idx],
                                    self.teams[opp_idx]))
                else:
                    matches.append((self.teams[opp_idx],
                                    self.teams[team_idx]))
        return matches

    def generate_matches(self, home_teams=None):
        is_odd = self.meetings % 2 == 1
        evens = self.meetings // 2

        matches = self._generate_even_matches(evens) if evens > 0 else []
        if is_odd:
            matches.extend(self._generate_odd_matches(home_teams))

        return matches

    def generate_round(self, matches):
        round = []
        try:
            random.shuffle(matches)
            round.append(matches.pop(0))
            poss = copy.copy(matches)
            for __ in range(1, self.match_count):
                match = Scheduler.find_unique_match(round, poss)
                round.append(match)
                matches.remove(match)
            return round
        except NoMatchFound:
            matches.extend(round)
            return None

    def __generate_schedule_round(self, matches):
        for __ in range(10):
            next_round = self.generate_round(matches)
            if next_round:
                return next_round
        else:
            raise ScheduleGenerationFailed('Schedule generation failed.')

    def generate_schedule(self, try_once=False, home_teams=None):
        rounds = []
        matches = self.generate_matches(home_teams=home_teams)

        try:
            for __ in range(self.round_count):
                rounds.append(self.__generate_schedule_round(matches))
        except ScheduleGenerationFailed as ex:
            if try_once:
                raise ex
            else:
                return self.generate_schedule(try_once, home_teams)

        return rounds


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

RR = RoundRobin(teams, 2)
print(RR.generate_schedule())

# use round robin algorithm to generate schedule
