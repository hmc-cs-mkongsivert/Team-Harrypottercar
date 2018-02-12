from collections import defaultdict
import pdb
from heapq import *

MAX_VISITS_PER_WEEK = 1000000000000000

# ==================================================
# Stolen from : https://gist.github.com/kachayev/5990802
# ==================================================


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f.name,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t.name: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    print "fuck"
    return float("inf")

# ==========================
# end of stolen code
# ==========================


class Node:
    def __init__(self, name, isCharge, timeCharge):
        # assume neighbors is a [(int, Node)]
        self.name = name
        self.isCharge = isCharge[0:len(isCharge)-1] == 'True'

        if timeCharge != "inf":
            self.timeCharge = int(timeCharge)
        else:
            self.timeCharge = float("inf")

        self.visits = 0

    def visit(self):
        if self.visits < MAX_VISITS_PER_WEEK:
            self.visits += 1
            return True
        return False

    def clear_visits(self):
        visits = self.visits
        self.visits = 0
        return visits

    def set_city(self, city):
        self.city = city

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

# =============================================
# This code is based on the code from: https://gist.github.com/econchick/4666413
# =============================================

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes #set()
        self.edges = defaultdict(list)
        self.edgeList = []
        self.time = 0
        self.stored_paths = {}  

    def add_node(self, value):
        self.nodes.append(value) # TODO this was add...

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))
        self.edges[to_node].append((from_node, distance))
        self.edgeList += [(from_node, to_node, distance)]
        self.edgeList += [(to_node, from_node, distance)]

    def get_edge(self, from_node, to_node):
        for edge in self.edges[from_node.name]:
            if edge[0] == to_node:
                return edge[1]

        return float("inf")

    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

        return None

    def distance(self, initial, final):
        cost, path = dijkstra(self.edgeList, initial, final)   
        return cost

    def path(self, initial, final):
        if (initial, final) in stored_paths:
            return stored_paths[(initial, final)]
        else:
            cost, path = dijkstra(self.edgeList, initial, final)   
            ret = []

            # Make path an actual list
            while path != ():
                ret.append(path[0])
                path = path[1]

            stored_paths[(initial, final)] = ret
            return ret

    def update(self):
        self.time += 1

        for n in self.nodes:
            if (not n.isCharge) and (n.timeCharge >= self.time):
                n.isCharge = True

    def clear_all_visits(self):
        visits = {}

        for n in self.nodes:
            visits[n] = n.clear_visits()

        return visits


def read_graph(node_f, edge_f, city_f):
    graph = Graph([])
    cities = []

    with open(node_f) as f:
        for line in f.readlines():
            if line != '\n':
                words = line.split(', ')
                node = Node(words[0], words[2], words[1])
                graph.add_node(node)

    with open(edge_f) as f:
        for line in f.readlines():
            if line != '\n':
                words = line.split(', ')
                graph.add_edge(words[0], words[1], int(words[2][:len(words[2])-1]))

    with open(city_f) as f:
        for line in f.readlines():
            if line != '\n':
                words = line.split(', ')
                city = words[0]
                cities.append(city)
                
                for node in words[1:]:
                    if node[-1] == "\n":
                        node = node[:len(node)-1]
                    graph.get_node(node).set_city(city)

    return graph, cities

if __name__ == "__main__":
    n1 = Node('a', 'city1', False, 3)
    n2 = Node('b', 'city2', True, 0)
    n3 = Node('c', 'city3', False, 2)
    
    g = Graph([n1,n2,n3])
    g.add_edge(n1, n2, 1)
    g.add_edge(n2, n3, 5)
    g.add_edge(n1, n3, 20)
    assert (g.distance(n1,n3) == 6)
    print n1.name
    print n3.name
    print map((lambda x: x.name), g.path(n1,n3))
