from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate


class BlackHole(Enemy):

    def __init__(self, center: Coordinate, radius: float):
        """Initializes a new black hole object anchored at the given point

        :param center: the location of the black hole
        :param radius: radius of the post
        """
        self.center = center
        self.radius = radius
        self.depth_interval = radius / 2

    def set_vertices_depth_interval(self, interval):
        self.depth_interval = interval

    # returns list of vertices for Graph
    # each vertex is type coordinate
    def get_vertices(self):
        pass

    # returns list of (edge1, edge2)
    # each couple is an edge in Graph
    def get_edges(self):
        pass

    # returns true if (start_coordinate -> target_coordinate) is a valid path
    # else, returns false
    def is_path_valid(self, start_coordinate, target_coordinate):
        pass
