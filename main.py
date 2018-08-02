#!/usr/bin/env python3

import club
from sim import Simulation
from loading import Load

clubs = ['ADO Den Haag','Ajax','AZ','de Graafschap','Excelsior','FC Emmen','FC Groningen','FC Utrecht','Feyenoord',
        'Fortuna Sittard','Heracles Almelo','NAC Breda','PEC Zwolle','PSV','SC Heerenveen','Vitesse','VVV-Venlo','Willem II']

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

class Main(object):
    """docstring for Main."""
    def __init__(self):
        super(Main, self).__init__()
        self.main()

    def welcome(self):
        print(" __      __        _   _           _    _____ _")
        print(" \ \    / /       | | | |         | |  / ____(_)")
        print("  \ \  / /__   ___| |_| |__   __ _| | | (___  _ _ __ ___")
        print("   \ \/ / _ \ / _ \ __| '_ \ / _` | |  \___ \| | '_ ` _ \ ")
        print("    \  / (_) |  __/ |_| |_) | (_| | |  ____) | | | | | | |")
        print("     \/ \___/ \___|\__|_.__/ \__,_|_| |_____/|_|_| |_| |_|")
        print("")
        print('welcome to Voetbal Sim')

    def menu(self):
        print('[1] New Game \n[2] Career mode \n[3] Info \n[4] Quit')
        option = int(input('your choice: '))
        if option == 1:
            print('New Game')
            teams = self.selection()
            self.quick_match(teams)
            self.menu()
        elif option == 2:
            load = Load()
            load.create()
        elif option == 3:
            print('Info')
            print('Voetbal_Sim is a football simulator based upon fifa career mode.')
            menu()
        else:
            exit()

    def selection(self):
        print('Choose your team:')
        for team in range(0,len(clubs)):
            print('[{}] - {}'.format(team, clubs[team]))
        option = int(input())
        home = club.Club(clubs[option])
        print(home.name)
        print('Choose your opponent:')
        for team in range(0,len(clubs)):
            print('[{}] - {}'.format(team, clubs[team]))
        option = int(input())
        away = club.Club(clubs[option])
        print(away.name)
        return(home, away)

    def main(self):
        self.welcome()
        self.menu()

    def quick_match(self, teams):
        home = teams[0]
        away = teams[1]
        print('Selected teams: \n {} vs {}'.format(home.name, away.name))
        input('press enter to continue')
        result = Simulation.simulate(teams)
        print(' {} vs {}\n {} - {}'.format(result[0].name, result[1].name, result[0].result, result[1].result))

if __name__ == '__main__':
    Main()
