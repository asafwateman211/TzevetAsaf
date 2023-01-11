from typing import List, Tuple

import networkx as nx
import pyvisgraph
from pyvisgraph import vis_graph as vg, graph

'''
from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate
from pyvisgraph import vis_graph as vg


# Navigator


def calculate_path(source: Coordinate, targets: List[Coordinate], enemies: List[Enemy], allowed_detection: float = 0) \
        -> Tuple[List[Coordinate], nx.Graph]:
    """Calculates a path from source to target without any detection

    Note: The path must start at the source coordinate and end at the target coordinate!

    :param source: source coordinate of the spaceship
    :param targets: target coordinate of the spaceship
    :param enemies: list of enemies along the way
    :param allowed_detection: maximum allowed distance of radar detection
    :return: list of calculated path waypoints and the graph constructed
    """
    return [source] + targets, nx.DiGraph()
'''

polys = [[graph.Point(0.0, 5.0), graph.Point(5.0, 5.0), graph.Point(5, 0), graph.Point(0, 0)],
         [graph.Point(4, 4), graph.Point(8, 4.0), graph.Point(4, 8.0), graph.Point(8, 8)]]
g = vg.VisGraph()
g.build(polys)
shortest = g.shortest_path(graph.Point(0, 0.0), graph.Point(9, 9))
print(shortest)
