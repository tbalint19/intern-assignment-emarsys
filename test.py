import unittest
from planner import Planner
from stop import Stop
from route import Route

class AllTests(unittest.TestCase):

    def setUp(self):
        self.u = Stop("u")
        self.z = Stop("z")
        self.w = Stop("w", self.z)
        self.v = Stop("v", self.w)
        self.x = Stop("x", self.u)
        self.y = Stop("y", self.v)
        self.a = Stop("a", self.v)
        self.b = Stop("b", self.v)
        self.c = Stop("c")
        self.d = Stop("d", self.c)
        self.e = Stop("e", self.d)
        self.c.previous = self.e

    def test_one_gives_back_self(self):
        self.planner = Planner([self.u])
        route = self.planner.get_route()
        self.assertEqual(route, "u")

    def test_one_dependency_returns_correct_route(self):
        self.planner = Planner([self.u, self.z, self.w])
        route = self.planner.get_route()
        self.assertTrue("zw" in route)

    def test_multiple_dependencies_returns_correct_route(self):
        self.planner = Planner([self.u, self.z, self.w, self.v, self.x, self.y])
        route = self.planner.get_route()
        self.assertTrue("zw" in route and "wv" in route and "ux" in route and "vy" in route)

    def test_one_gives_back_self_in_data(self):
        self.planner = Planner([self.u])
        data = self.planner.get_route_data()
        self.assertEqual(data['route'], "u")

    def test_one_dependency_returns_correct_route_in_data(self):
        self.planner = Planner([self.u, self.z, self.w])
        data = self.planner.get_route_data()
        self.assertTrue("zw" in data['route'])

    def test_multiple_dependencies_returns_correct_route_in_data(self):
        self.planner = Planner([self.u, self.z, self.w, self.v, self.x, self.y])
        data = self.planner.get_route_data()
        self.assertTrue("zw" in data['route'] and "wv" in data['route'] and "ux" in data['route'] and "vy" in data['route'])

    def test_forking_does_not_return_route(self):
        self.planner = Planner([self.u, self.z, self.w, self.v, self.x, self.y, self.a, self.b])
        data = self.planner.get_route_data()
        self.assertEqual(data['route'], None)

    def test_forking_can_return_fragment(self):
        self.planner = Planner([self.u, self.z, self.w, self.v, self.x, self.y, self.a, self.b])
        data = self.planner.get_route_data()
        print(data['fragment'])
        self.assertTrue(
            "zw" in data['fragment'] and
            "wv" in data['fragment'] and
            "ux" in data['fragment'] and
            ("vy" in data['fragment'] or "va" in data['fragment'] or "vb" in data['fragment']))

    def test_forking_returns_error(self):
        self.planner = Planner([self.u, self.z, self.w, self.v, self.x, self.y, self.a, self.b])
        data = self.planner.get_route_data()
        self.assertEqual(data['status'], "invalid parameters")

    def test_circle_does_not_return_route(self):
        self.planner = Planner([self.c, self.d, self.e])
        data = self.planner.get_route_data()
        self.assertEqual(data['route'], None)

    def test_circle_can_return_fragment(self):
        self.planner = Planner([self.c, self.d, self.e, self.u])
        data = self.planner.get_route_data()
        self.assertEqual(data['fragment'], "u")

    def test_circle_returns_error(self):
        self.planner = Planner([self.c, self.d, self.e, self.u])
        data = self.planner.get_route_data()
        self.assertEqual(data['status'], "invalid parameters")

if __name__ == '__main__':
    unittest.main()
