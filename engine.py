#Engine
import random
import argparse
import graph
import agent

NUM_AGENTS = 100
NUM_WEEKS = 100
PROB_WANT_CAR = .01

parser = argparse.ArgumentParser(description="process graph and station function")
parser.add_argument('nodes', metavar='NODES', type=str, help='Path to node file')
parser.add_argument('edges', metavar='EDGES', type=str, help='Path to edge file')
parser.add_argument('place_func', metavar='PLACEFUNC', type=str, help='Path to placement function file')
args = parser.parse_args()

graph = graph.read_graph(args[nodes], args[edges])

neighborhoods = {}
work_areas = {}
num_nodes = len(graph.nodes)

for node in graph:
    neighborhood[node] = []
    work_areas[node] = []

#create agents
agentList = []
for i in range(NUM_AGENTS):
	#set home to be current node
	#assign random nodes work
	schedule = []

    # Randomly set home and work (might be same neighborhood)
    home_index = random.range(0, num_nodes)
    home = graph.nodes[home_index]
    neighborhoods[home].append(agent)
    work_index = random.range(0, num_nodes)
    work = graph.nodes[work_index]
    work_areas[work].append(agent)

	for j in range(5):
		#start at home and then go to work
        weekday = [home, work]
        
		numDest = random.randrange(1, 5)
		for k in range(numDest):
            #assign a random node in the graph to be a destination
			randIndex = random.randrange(0, len(graph.nodes) - 1)
            weekday.append(graph.nodes[randIndex])
			
        #return home
		weekday.append(home)
        schedule += weekday
	for j in range(2): #weekend
		#start at home
        weekend = [home]

		numDest = random.randrange(1, 10)
		for k in range(numDest):
			#create random destinations in graph
            randIndex = random.randrange(0, len(graph.nodes) - 1)
            weekend.append(graph.nodes[randIndex])

		#return home
        weekend.append(home)
        schedule += weekend

    agent = Agent(schedule)

    if random.random() < PROB_WANT_CAR:
        agent.desire_car()

    neighborhood[home].append(agent)

# Turn neighborhood into Neighborhood data structure
for node in neighborhoods.keys():
    agents = neighborhoods[node]
    neighborhood = Neighborhood(agents)
    neighborhoods[node] = neighborhood

# Do same with work area
for node in work_areas.keys():
    agents = work_areas[node]
    work_area = Neighborhood(agents)
    work_areas[node] = work_area

# Run actual simulation
for i in range(NUM_WEEKS):
    graph.update()

    for agent in agentList:
        # Some agents spontaneously want cars
        if random.random() < PROB_WANT_CAR:
            agent.desire_car()

        agent.execute_sched()

    # Neighborhood influence on desire to buy a car
    for node in neighborhoods.keys():
        neighborhoods[node].determine_car_desire()
    for node in work_areas.keys():
        work_areas[node].determine_car_desire()

    graph.clear_all_visits()

# statistics
num_cars = reduce((lambda x, y: x + y.has_car()), agentList)
car_ratio = float(cars) / float(NUM_AGENTS)
num_want_cars = reduce((lambda x, y: x + y.wants_car), agentList)
num_didnt_get_car = num_cars - num_want_cars
