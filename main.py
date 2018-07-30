#!/usr/bin/env python3

import club
import sim
import manager

clubs = [['ADO Den Haag', 69],['Ajax', 76],['AZ', 73],['de Graafschap', 60],['Excelsior', 68],['FC Emmen', 60],
['FC Groningen', 68],['FC Utrecht', 72],['Feyenoord', 76],['Fortuna Sittard', 60],['Heracles Almelo', 69],
['NAC Breda', 67],['PEC Zwolle', 70],['PSV', 75],['SC Heerenveen', 70],['Vitesse', 71],['VVV-Venlo', 67],
['Willem II', 68]]

def welcome():
    print('welcome to Voetbal_Sim')
    pass

def menu():
    print('[1] New Game \n[2] Career mode \n[3] Info \n[4] Quit')
    option = int(input('your choice:'))
    if option == 1:
        print('New Game')
        teams = selection()
        return(teams)
    elif option == 2:
        print('Career mode')
        manager.Manager.menu()
    elif option == 3:
        print('Info')
        print('Voetbal_Sim is a football simulator based upon fifa career mode.')
        menu()
    else:
        exit()

def selection():
    print('Choose your team:')
    for team in range(0,len(clubs)):
        print('[{}] - {}'.format(team, clubs[team][0]))
    option = int(input())
    home = club.Club(clubs[option][0],clubs[option][1])
    print(home.name, home.rating)
    print('Choose your opponent:')
    for team in range(0,len(clubs)):
        print('[{}] - {}'.format(team, clubs[team][0]))
    option = int(input())
    away = club.Club(clubs[option][0],clubs[option][1])
    print(away.name, away.rating)
    return(home, away)

def main():
    welcome()
    teams = menu()
    sim.Simulation.simulate(teams)
    pass

if __name__ == '__main__':
    main()
