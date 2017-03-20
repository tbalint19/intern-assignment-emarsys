from stop import Stop
from route import Route

class Planner:

    def __init__(self, unlocated_stops):
        self.unlocated_stops = unlocated_stops
        self.error_happened = False
        self.create_route()

    def create_route(self):
        self.planned_route = Route()
        while len(self.unlocated_stops) > 0:
            current_stop = self.planned_route.get_last()
            next_stop = self.get_next_stop(current_stop)
            if self.error_happened:
                break
            self.planned_route.stops.append(next_stop)
            self.unlocated_stops.remove(next_stop)

    def get_next_stop(self, current_stop):
        stop_with_no_previous = None
        for examined_stop in self.unlocated_stops:
            if examined_stop.previous == current_stop:
                return examined_stop
            if examined_stop.previous is None and stop_with_no_previous is None:
                stop_with_no_previous = examined_stop
        if stop_with_no_previous is None:
            self.error_happened = True
        return stop_with_no_previous

    def get_route(self):
        if not self.error_happened:
            return self.planned_route.get_stops()
        return None

    def get_route_data(self):
        if self.error_happened:
            response = {'route': None, 'status': 'invalid parameters', 'fragment': self.planned_route.get_stops()}
        else:
            response = {'route': self.planned_route.get_stops(), 'status': "generated", 'fragment': None}
        return response
