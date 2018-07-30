#!/usr/bin/env python3

from club import Club
from sim import Simulation
from roundrobin import RoundRobinScheduler

# manager file
# -   Board requests
# -   Player requests

class Manager(object):
    """docstring for Manager."""
    def __init__(self, club, teams, league):
        super(Manager, self).__init__()
        self.club = Club(club)
        self.teams = teams
        self.league = league
        self.fixtures = []
        self.played = []
        self._generate_fixtures()

    def _generate_fixtures(self):
        fixtures = []
        RR = RoundRobinScheduler(self.teams, 2)
        schedule = RR.generate_schedule()
        for round in schedule:
            for match in round:
                if self.club.name in match:
                    fixtures.append(match)
        self.fixtures = fixtures

    def menu(self):
        # overview of all possible options:
        # -   next game
        # -   team management
        # -   board management
        # -   calender
        # -   quit
        print('Manager menu')
        print('Club: {} {}'.format(self.club.name, self.club.overall))
        print('League: {}'.format(self.club.league))
        print('[1] Next game \n[2] Team \n[3] Board \n[4] Calender \n[5] Quit')
        option = int(input('Your choice: '))
        if option == 1:
            if self.fixtures != []:
                match = self.fixtures[0]
                print(match)
                home = Club(match[0])
                away = Club(match[1])
                teams = [home, away]
                result = Simulation.simulate(teams)
                self.played.append([self.fixtures[0], result])
                self.fixtures.pop(0)
            else:
                print('End of the season')
            self.menu()
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            self.calender(self.club)
        else:
            exit()
        pass

    def calender(self, club):
        fixtures = self.fixtures
        played = self.played
        for i in range(0, int(len(fixtures)+len(played))):
            if i in range(0, len(played)):
                print('Round {}: {}'.format(i+1, played[i]))
            else:
                print('Round {}: {}'.format(i+1, fixtures[i-len(played)]))
        # for round in played:
        #     print(round)
        # for round in fixtures:
        #     print(round)


        self.menu()
