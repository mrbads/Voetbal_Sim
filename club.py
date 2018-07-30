#!/usr/bin/env python3

# club file

class Club(object):
    """docstring for Club."""
    def __init__(self, arg, rating):
        super(Club, self).__init__()
        self.name = arg
        self.rating = rating
