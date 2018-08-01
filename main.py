#!/usr/bin/env python3

import club
from sim import Simulation
from manager import Manager

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

def welcome():
    print(" __      __        _   _           _    _____ _")
    print(" \ \    / /       | | | |         | |  / ____(_)")
    print("  \ \  / /__   ___| |_| |__   __ _| | | (___  _ _ __ ___")
    print("   \ \/ / _ \ / _ \ __| '_ \ / _` | |  \___ \| | '_ ` _ \ ")
    print("    \  / (_) |  __/ |_| |_) | (_| | |  ____) | | | | | | |")
    print("     \/ \___/ \___|\__|_.__/ \__,_|_| |_____/|_|_| |_| |_|")
    print("")
    print('welcome to Voetbal Sim')

def menu():
    print('[1] New Game \n[2] Career mode \n[3] Info \n[4] Quit')
    option = int(input('your choice: '))
    if option == 1:
        print('New Game')
        teams = selection()
        return(teams)
    elif option == 2:
        print('Career mode')
        manager = Manager('Ajax', clubs, leagues[0])
        manager.menu()
    elif option == 3:
        print('Info')
        print('Voetbal_Sim is a football simulator based upon fifa career mode.')
        menu()
    else:
        exit()

def selection():
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

def main():
    welcome()
    teams = menu()
    Simulation.simulate(teams)
    pass

if __name__ == '__main__':
    main()
