#!/usr/bin/env python3

import random
import math

# Simulation file
# Simulate the game and return win/draw/loss

class Simulation(object):
    """docstring for Simulation."""
    home_adv = 3
    outcomes = [1,2,3]
    result = 0

    def __init__(self, arg):
        super(Simulation, self).__init__()
        self.arg = arg

    def simulate(teams):
        # simulate the game
        home = teams[0]
        away = teams[1]
        home.overall = home.overall + Simulation.home_adv
        diff = home.overall - away.overall
        # print(diff)
        # Different states the differential can take:
        # -   < -10             5%     10%     85%
        # -   negative      25%-5%  25%-10% 50%-85%
        # -   0                 33%     33%     33%
        # -   <10           50%-85% 25%-10%  25%-5%
        # -   >10               85%     10%     5%
        if diff <= -10:
            # print(1)
            chances = [5, 10, 85]
            result = random.choices(Simulation.outcomes, weights=chances)
        elif diff < 0:
            # print(2)
            diff = math.fabs(diff)
            A = 25-((20/9)*(diff-1))
            B = 25-((15/9)*(diff-1))
            C = 50+((35/9)*(diff-1))
            chances = [A, B, C]
            # print('Win: {}% \nDraw: {}% \nLoss: {}% \nTotal: {}%'.format(A,B,C,(A+B+C)))
            result = random.choices(Simulation.outcomes, weights=chances)
        elif diff == 0:
            # print(3)
            chances = [33, 33, 33]
            result = random.choices(Simulation.outcomes, weights=chances)
        elif diff < 10:
            # print(4)
            A = 50+((35/9)*(diff-1))
            B = 25-((15/9)*(diff-1))
            C = 25-((20/9)*(diff-1))
            chances = [A, B, C]
            # print('Win: {}% \nDraw: {}% \nLoss: {}% \nTotal: {}%'.format(A,B,C,(A+B+C)))
            result = random.choices(Simulation.outcomes, weights=chances)
        else:
            # print(5)
            chances = [85, 10, 5]
            result = random.choices(Simulation.outcomes, weights=chances)

        if result == [1]:
            return Simulation.win(home, away)
        elif result == [2]:
            return Simulation.draw(home, away)
        elif result == [3]:
            return Simulation.loss(home, away)

    def win(home, away):
        home.result = 3
        away.result = 0
        return home, away

    def draw(home, away):
        home.result = 1
        away.result = 1
        return home, away

    def loss(home, away):
        home.result = 0
        away.result = 3
        return home, away
