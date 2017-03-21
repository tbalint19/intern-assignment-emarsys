from stop import Stop
from route import Route

class Planner:

    def __init__(self, unlocated_stops):
        self.unlocated_stops = unlocated_stops
        self.error_happened = False
        self.create_route()

    def create_route(self):
        self.planned_route = Route()
        self.error_happened = self.recursive_attach_to_route_from_unlocated()

    def recursive_attach_to_route_from_unlocated(self):
        current_stop = self.planned_route.get_last()
        stop_with_no_previous = None
        for examined_stop in self.unlocated_stops:
            if examined_stop.previous == current_stop:
                self.planned_route.stops.append(examined_stop)
                self.unlocated_stops.remove(examined_stop)
                return self.recursive_attach_to_route_from_unlocated()
            if examined_stop.previous is None and stop_with_no_previous is None:
                stop_with_no_previous = examined_stop
        if stop_with_no_previous is None:
            return len(self.unlocated_stops) > 0
        self.planned_route.stops.append(stop_with_no_previous)
        self.unlocated_stops.remove(stop_with_no_previous)
        return self.recursive_attach_to_route_from_unlocated()

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
