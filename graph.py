from collections import defaultdict
from heapq import *



# ==================================================
# Stolen from : https://gist.github.com/kachayev/5990802
# ==================================================


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")

# ==========================
# end of stolen code
# =========================


class Node:
    def __init__(self,  isCharge, timeCharge):
        # assume neighbors is a [(int, Node)]
        self.isCharge = isCharge 
        self.timeCharge = timeCharge

# =============================================
# This code is based on the code from: https://gist.github.com/econchick/4666413
# =============================================

class Graph:
  def __init__(self, nodes):
    self.nodes = nodes #set()
    self.edges = defaultdict(list)
    self.edgeList = []
    self.time = 0  


  def add_node(self, value):
    self.nodes.add(value)


  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append((to_node, distance))
    self.edges[to_node].append((from_node, distance))
    self.edgeList += [(from_node, to_node, distance)]
    self.edgeList += [(to_node, from_node, distance)]


  def distance(self, initial, final):
    cost, path = dijkstra(self.edgeList, initial, final)   
    return cost

  def update():
    self.time += 1
    for n in self.nodes:
      if (not self.isCharge) and (n.timeCharge >= self.time):
        self.isCharge = True





if __name__ == "__main__":
  n1 = Node(False, 3)
  n2 = Node(True, 0)
  n3 = Node(False, 2)

  
  g = Graph([n1,n2,n3])
  g.add_edge(n1, n2, 1)
  g.add_edge(n2, n3, 5)
  g.add_edge(n1, n3, 20)
  assert (g.distance(n1,n3) == 6)
