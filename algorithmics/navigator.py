from typing import List, Tuple

import networkx as nx
import shapely
from shapely import geometry

from algorithmics.enemy import radar
from algorithmics.enemy.asteroids_zone import AsteroidsZone
from algorithmics.pyvisgraph import graph
from algorithmics.pyvisgraph.graph import Point
from pyvisgraph import vis_graph as vg


from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate


# Navigator

def coords_to_point(c: Coordinate):
    p = Point(c.x, c.y)
    return p


def enemy_to_points(enemies: List[Enemy]):
    polys=[]
    for e in enemies:
        if (type(e) == radar):
            pass
        polys.append(e.get_vertices())
    return polys


def to_list(t): #t is polygon
    xx, yy = t.exterior.coords.xy
    l = []
    for i in range(0, len(xx)):
        l.append(Point(xx[i], yy[i]))
    return l


def get_graph(source: Point, targets: List[Point], enemies: List[Enemy]):
    g = vg.VisGraph()
    pols =[e.get_polygon() for e in enemies]
    new_enemies = []
    flag = False
    for e in enemies:
        pol = e.get_polygon()
        flag = False
        for h in enemies:
            pol2 = h.get_polygon()
            if e != h and pol.intersects(pol2):
                new_enemies.append(pol.union(pol2))
                flag = True
        if not flag:
            new_enemies.append(e)
    polys = [e.get_vertices() for e in enemies]
    temp=[]
    '''
    for pol in polys:
        pol = geometry.Polygon([[p.x, p.y] for p in pol])
        for pol2 in polys:
            pol2 = geometry.Polygon([[p.x, p.y] for p in pol2])
            temp.append(pol.intersection(pol2))
    for t in temp:
        polys += [to_list(t)]
    '''
    g.build(polys)
    return g


def calculate_path(source: Coordinate, targets: List[Coordinate], enemies: List[Enemy], allowed_detection: float = 0) \
        -> Tuple[List[Point], nx.Graph]:

    """Calculates a path from source to target without any detection

    Note: The path must start at the source coordinate and end at the target coordinate!

    :param source: source coordinate of the spaceship
    :param targets: target coordinate of the spaceship
    :param enemies: list of enemies along the way
    :param allowed_detection: maximum allowed distance of radar detection
    :return: list of calculated path waypoints and the graph constructed
    """



    targets2 =[]
    for i in range(0,len(targets)):
        targets2.append(coords_to_point(targets[i]))
    source = coords_to_point(source)
    g = get_graph(source, targets2, enemies)
    print(g.shortest_path(source, targets2[0]))
    return g.shortest_path(source, targets2[0]), nx.Graph()


polys = [[Coordinate(0.0, 1.0), Coordinate(3.0, 1.0), Coordinate(1.5, 4.0)],
         [Coordinate(4.0, 4.0), Coordinate(7.0, 4.0), Coordinate(5.5, 8.0)]]
a = AsteroidsZone([Coordinate(0.0, 1.0), Coordinate(3.0, 1.0), Coordinate(1.5, 4.0)])
enemies = [a]
#g = vg.VisGraph()
#g.build(polys)
#shortest = g.shortest_path(graph.Point(1.5,0.0), graph.Point(4.0, 6.0))
calculate_path(Coordinate(-1, -1), [Coordinate(1, 3),Coordinate(5,5),Coordinate(-1,7)], enemies)

