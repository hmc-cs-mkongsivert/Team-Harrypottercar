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
		#start at home
		#go to work
		numDest = random.randrange(1, 5)
		for k in range(numDest):
			pass
			#create random destinations in graph
		#return home
	for j in range(2): #weekend
		#start at home
		numDest = random.randrange(1, 10)
		for k in range(numDest):
			pass
			#create random destinations in graph
		#return home

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
    for agent in agentList:
        agent.execute_sched()
