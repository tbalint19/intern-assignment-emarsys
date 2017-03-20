from stop import Stop

class Route:

    def __init__(self):

        self.stops = []

    def get_last(self):
        if len(self.stops) == 0:
            return None
        return self.stops[-1]

    def get_stops(self):
        return "".join([stop.name for stop in self.stops])
