#!/usr/bin/env python3

from club import Club
from competition import Competition
from sim import Simulation

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
        self.stats = {"Points: ": 0,"Wins: ": 0,"Draws: ": 0,"Losses: ": 0}
        self.competition = Competition()
        self._generate_fixtures()

    def _generate_fixtures(self):
        # fixtures = []
        schedule = self.competition.roster(self.league)
        self.fixtures = schedule
        # for round in schedule:
        #     for match in round:
        #         if self.club.name in match:
        #             fixtures.append(match)
        # self.fixtures = fixtures

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
            self.next_game()
            self.menu()
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            self.calender()
            self.menu()
        else:
            exit()
        pass

    def calender(self):
        fixtures = []
        for round in self.fixtures:
            for match in round:
                if self.club.name in match:
                    fixtures.append(match)
        played = self.played
        for i in range(0, int(len(fixtures)+len(played))):
            if i in range(0, len(played)):
                print('Round {}: {} Played'.format(i+1, played[i]))
            else:
                print('Round {}: {}'.format(i+1, fixtures[i-len(played)]))
        print("{}: {} Points".format(self.club.name, self.club.result))
        print(self.competition.standings)

    def next_game(self):
        if self.fixtures != []:
            for game in self.fixtures[0]:
                print(game)
                home = Club(game[0])
                away = Club(game[1])
                teams = [home, away]
                result = Simulation.simulate(teams)
                self.competition._update_standings(result)
                if home.name == self.club.name or away.name == self.club.name:
                    self.played.append(game)
                self.fixtures.pop(0)
        else:
            print('End of the season')
            print('Matches played: {} Points: {}'.format(len(self.played), self.club.result))


        self.menu()
