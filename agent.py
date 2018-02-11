import graph
from functools import reduce

CAR_DESIRE_THRESHOLD = 0.7
MAX_TANK = 100

class Neighborhood:
    def __init__(self, agents):
        self.agents = agents
        self.num_agents = len(agents)
        self.num_cars = reduce((lambda x, y: x + y.has_car()), agents)

        add_neighbors(agents)

    def determine_car_desire(self):
        num_cars = reduce((lambda x, y: x + y.has_car()), agents)

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

    def execute_sched():
        # Everyone buys cars at the beginning of the week
        self.maybe_buy_car()

        loc = self.sched[0]
        can_buy_car = True

        for dest in self.sched[1:]:
            if graph.distance(loc, dest) > self.tank:
                can_buy_car = False

            # TODO: Currently assumes it stops everywhere
            if dest.is_station:
                self.refuel()
                dest.visit()
            else:
                self.travel(loc, dest)

            loc = dest

        if can_buy_car:
            self.can_buy_car = True

'''        
    def evaluate_if_wants_car(self):
        num_neighbors = len(self.neighbors)
        neighbors_with_car = 0

        for neighbor in self.neighbors:
            if neighbor.has_car:
                neighbors_with_car += 1
'''

    def travel(self, loc, dest):
        self.tank -= graph.distance(loc, dest)
            
    def refuel(self):
        self.tank = MAX_TANK

'''
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
'''

    def buy_car(self):
        if self.wants_car and self.can_buy_car():
            self.has_car = True

    def desire_car(self):
        self.wants_car = True

def add_neighbors(agents):
    for agent in agents:
        for neighbor in agents:
            agent.add_neighbor(neighbor)
