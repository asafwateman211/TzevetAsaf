from abc import ABC


class Enemy(ABC):
    # returns list of vertices for Graph
    # each vertex is type coordinate
    def get_vertices(self):
        pass

    # returns list of (edge1, edge2)
    # each couple is an edge in Graph
    def get_edges(self):
        pass

    # returns true coordinate is in enemy territory
    # else, returns false
    def is_in_enemy(self, coordinate):
        pass

    # returns true if (start_coordinate -> target_coordinate) is a valid path
    # else, returns false
    def is_path_valid(self, start_coordinate, target_coordinate):
        pass
