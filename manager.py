#!/usr/bin/env python3

from roundrobin import RoundRobinScheduler

# manager file
# -   Board requests
# -   Player requests

class Manager(object):
    """docstring for Manager."""
    def __init__(self, club, teams, league):
        super(Manager, self).__init__()
        self.club = club
        self.teams = teams
        self.league = league

    def menu(self):
        # overview of all possible options:
        # -   next game
        # -   team management
        # -   board management
        # -   calender
        # -   quit
        print('Manager menu')
        print('[1] Next game \n[2] Team \n[3] Board \n[4] Calender \n[5] Quit')
        option = int(input('Your choice: '))
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            self.calender(self.club)
        else:
            main.menu()
        pass

    def calender(self, club):
        RR = RoundRobinScheduler(self.teams, 2)
        schedule = RR.generate_schedule()
        for round in schedule:
            for match in round:
                if club in match:
                    print(match)

        self.menu()
