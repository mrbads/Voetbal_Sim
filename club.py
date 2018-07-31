#!/usr/bin/env python3

import json

# club file

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

class Club(object):
    """docstring for Club."""
    def __init__(self, name):
        super(Club, self).__init__()
        self.name = name
        self.league = ''
        self.overall = 0
        self.attack = 0
        self.midfield = 0
        self.defense = 0
        self.transferbudget = 0
        self.domestic_prestige = 0
        self.international_prestige = 0
        self.num_players = 0
        self.teams = 0
        self.result = 0
        self._generate_league(name)
        self._generate_overall(name)


    def _generate_league(self, club):
        for league, clubs in leagues:
            for name, overall in clubs:
                if name == club:
                    self.league = league

    def _generate_overall(self, club):
        for league, clubs in leagues:
            for name, overall in clubs:
                if name == club:
                    self.overall = overall

    def _generate_attack(self, club):
        pass

    def _generate_midfield(self, club):
        pass

    def _generate_defense(self, club):
        pass

    def _generate_budget(self, club):
        pass

    def _generate_dp(self, club):
        pass

    def _generate_ip(self, club):
        pass

    def _generate_players(self, club):
        pass

    def _generate_teams(self, club):
        pass
