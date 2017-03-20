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

    def test_one_gives_back_self(self):
        self.planner = Planner([self.u])
        route = self.planner.get_route()
        self.assertEqual(route, "u")

    def test_one_dependency_returns_correct_route(self):
        self.planner = Planner([self.u, self.z, self.w])
        route = self.planner.get_route()
        self.assertTrue("zw" in route)

    def test_multiple_dependency_returns_correct_route(self):
        self.planner = Planner([self.u, self.z, self.w, self.v, self.x, self.y])
        route = self.planner.get_route()
        self.assertTrue("zw" in route and "wv" in route and "ux" in route and "vy" in route)


if __name__ == '__main__':
    unittest.main()
