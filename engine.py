#Engine
import random
import argparse

NUM_AGENTS = 100
NUM_WEEKS = 100

parser = argparse.ArgumentParser(description="process graph and station function")
parser.add_argument('graph', metavar='GRAPH', type=str, help='Path to graph file')
parser.add_argument('place_func', metavar='PLACEFUNC', type=str, help='Path to placement function file')
args = parser.parse_args

graph = Graph(args[graph])
neighborhoods = {}
num_nodes = len(graph.nodes)

for node in graph:
    neighborhood[node] = {}

#create agents
agentList = []
for i in range(NUM_AGENTS):
	#set home to be current node
	#assign random nodes work
	schedule = []

    home_index = random.range(0, num_nodes)
    home = graph.nodes[home_index]

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
    neighborhood[home].append(agent)

# Turn neighborhood into Neighborhood data structure
for node in neighborhoods.keys():
    agents = neighborhoods[node]
    neighborhood = Neighborhood(agents)
    neighborhoods[node] = neighborhood

