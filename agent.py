import graph
import pdb
from functools import reduce

CAR_DESIRE_THRESHOLD = 0.4
MAX_TANK = 400 # Tesla miles per charge

class Neighborhood:
    def __init__(self, agents):
        self.agents = agents
        self.num_agents = len(agents)
        #if num_agents > 0:
        #    self.num_cars = reduce((lambda x, y: x + y.has_car()), agents)
        #else:
        #    self.num_cars = 0

        #add_neighbors(agents)

    def determine_car_desire(self):
        if self.num_agents > 0:
            num_cars = sum(map((lambda x: int(x.has_car)), self.agents))

            if float(num_cars) / float(self.num_agents) > CAR_DESIRE_THRESHOLD:
                map((lambda x: x.desire_car()), self.agents)

class Agent:
    def __init__(self, sched):
        self.sched = sched
        self.tank = MAX_TANK
        self.wants_car = False
        self.can_buy_car = False
        self.has_car = False
        self.neighbors = []

    def execute_sched(self, graph):
        # Everyone buys cars at the beginning of the week
        self.maybe_buy_car()

        loc = self.sched[0]
        can_buy_car = True

        for dest in self.sched[1:]:
            path = graph.path(dest, loc)
            prev = loc

            for node in path[1:]:
                if graph.get_edge(prev, node) > self.tank:
                    can_buy_car = False

                # TODO: Currently assumes it stops everywhere
                if graph.get_node(node).visit():
                    self.refuel()
                else:
                    self.travel(prev, node) # Deduct fuel

                prev = graph.get_node(node)

            loc = dest

        if can_buy_car:
            self.can_buy_car = True

    def travel(self, loc, dest, graph):
        self.tank -= graph.get_edge(loc, dest)
            
    def refuel(self):
        self.tank = MAX_TANK

    def maybe_buy_car(self):
        if self.wants_car and self.can_buy_car:
            self.has_car = True

    def desire_car(self):
        self.wants_car = True

def add_neighbors(agents):
    for agent in agents:
        for neighbor in agents:
            agent.add_neighbor(neighbor)
