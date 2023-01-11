from typing import List

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate
from pyvisgraph.graph import Point

import shapely.geometry as geo


class AsteroidsZone(Enemy):
    def __init__(self, boundary: List[Coordinate]):
        self.boundary = [Point(p.x, p.y) for p in boundary]     # List[Point]

    def get_vertices(self):
        return self.boundary
