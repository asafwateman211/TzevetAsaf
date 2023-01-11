from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate
import shapely.geometry as geo
import math


class BlackHole(Enemy):

    def __init__(self, center: Coordinate, radius: float):
        self.center = center
        self.radius = radius
        self.n_points = round(radius * 5)

    def set_number_of_vertices(self, n):
        self.n_points = round(n)

    def get_coordinates(self, theta):
        rad = self.radius / math.cos(math.pi / self.n_points)
        return geo.Point(self.center.x + rad * math.cos(theta), self.center.y + rad * math.sin(theta))

    # returns list of vertices for Graph
    # each vertex is type coordinate
    def get_vertices(self):
        thetas = [math.tau * i / self.n_points for i in range(0, self.n_points)]
        tmp = [self.get_coordinates(theta) for theta in thetas]
        return [Coordinate(sp.x, sp.y) for sp in tmp]

