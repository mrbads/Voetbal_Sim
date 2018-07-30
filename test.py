from __future__ import print_function, unicode_literals

import itertools
import random
import copy

leagues = [
['Eredivisie',
[['ADO Den Haag', 69],['Ajax', 76],['AZ', 73],['de Graafschap', 60]]],
['Eerste Divisie',
[['Almere City FC', 60],['FC Den Bosch', 60],['FC Dordrecht', 60],['FC Eindhoven', 60],['FC Twente', 60],['FC Volendam', 60],
['Go Ahead Eagles', 60],['Helmond Sport', 60],['Jong Ajax', 60],['Jong AZ', 60],['Jong FC Utrecht', 60],['Jong PSV', 60],
['MVV Maastricht', 60],['N.E.C.', 60],['RKC Waalwijk', 60],['Roda JC', 60],['SC Cambuur', 60],['Sparta Rotterdam', 60],
['Telstar', 60],['TOP Oss', 60]]]
]

for league, clubs in leagues:
    for name, overall in clubs:
        print(name)
