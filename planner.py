from stop import Stop
from route import Route

class Planner:

    def __init__(self, unlocated_stops):
        self.unlocated_stops = unlocated_stops
        self.create_route()

    def create_route(self):
        self.planned_route = Route()
        while len(self.unlocated_stops) > 0:
            current_stop = self.planned_route.get_last()
            next_stop = self.get_next_stop(current_stop)
            self.planned_route.stops.append(next_stop)
            self.unlocated_stops.remove(next_stop)

    def get_next_stop(self, current_stop):
        stop_with_no_previous = None
        for examined_stop in self.unlocated_stops:
            if examined_stop.previous == current_stop:
                return examined_stop
            if examined_stop.previous is None and stop_with_no_previous is None:
                stop_with_no_previous = examined_stop
        return stop_with_no_previous

    def get_route(self):
        return self.planned_route.get_stops()
