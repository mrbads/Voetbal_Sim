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

        print('  __  __                                     __  __')
        print(' |  \/  | __ _ _ __   __ _  __ _  ___ _ __  |  \/  | ___ _ __  _   _')
        print(" | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__| | |\/| |/ _ \ '_ \| | | |")
        print(" | |  | | (_| | | | | (_| | (_| |  __/ |    | |  | |  __/ | | | |_| |")
        print(" |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|    |_|  |_|\___|_| |_|\__,_|")
        print("                           |___/")

        print('Club: {} {}'.format(self.club.name, self.club.overall))
        print('League: {}'.format(self.club.league))
        print('[1] Next game \n[2] Team \n[3] Board \n[4] Calender \n[5] Standings \n[6] Quit')
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
            input('press enter to continue')
            self.menu()
        elif option == 5:
            name_sort = sorted(self.competition.standings, key=lambda tup: tup[0])
            cur_standing = sorted(name_sort, key=lambda tup: tup[1], reverse=True)
            print(cur_standing)
            input('press enter to continue')
            self.menu()
        else:
            exit()
        pass

    def calender(self):
        fixtures = []
        played = []
        for round in self.fixtures:
            for match in round:
                if self.club.name in match:
                    fixtures.append(match)
        for match in self.played:
            if self.club.name in match[0]:
                played.append(match)

        for i in range(0, int(len(fixtures)+len(played))):
            if i in range(0, len(played)):
                print('Round {}: {} {}'.format(i+1, played[i][0], played[i][1]))
            else:
                print('Round {}: {}'.format(i+1, fixtures[i-len(played)]))

    def next_game(self):
        if self.fixtures != []:
            for game in self.fixtures[0]:
                home = Club(game[0])
                away = Club(game[1])
                if home.name == self.club.name or away.name == self.club.name:
                    print(game)
                    input('press enter to continue')
                teams = [home, away]
                result = Simulation.simulate(teams)
                self.competition._update_standings(result)
                self.played.append([(result[0].name, result[1].name), (result[0].result, result[1].result)])
            self.fixtures.pop(0)
        else:
            print('End of the season')


        self.menu()
