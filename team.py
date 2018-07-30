#!/usr/bin/env python3

# Team File
# -   Stats
# -   Rating
# -   Chemistry
# -   Formation


class Team(object):
    """docstring for Team."""
    def __init__(self, name, rating):
        super(Team, self).__init__()
        self.name = name
        self.rating = rating
