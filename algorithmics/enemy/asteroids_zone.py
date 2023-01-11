from typing import List

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate

import shapely.geometry as geo


class AsteroidsZone(Enemy):
    def __init_(self, boundary: List[Coordinate]):
        self.boundary = boundary
        self.polygon = geo.Polygon(self.boundary)

    def get_vertices(self):
        return self.boundary

    def get_edges(self):
        return geo.LineString(self.boundary)

    def get_polygon(self):
        return self.polygon

    # Checks weather the point is inside the enemy
    def is_in_enemy(self, point):
        return self.polygon.contains(point)

    def is_path_valid(self, start_coordinate, target_coordinate):
        line = geo.LineString([start_coordinate, target_coordinate])
        intersection = self.polygon.intersection(line)
        return not(intersection.isempty())

