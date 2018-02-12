#Engine
import random
import argparse
import graph
import agent
from joblib import Parallel, delayed
import multiprocessing
from multiprocessing import Pool

NUM_AGENTS = 4000
NUM_WEEKS = 10
PROB_WANT_CAR = .01

def execute_agent_loop(this_agent, graph):
    # Some agents spontaneously want cars
    if random.random() < PROB_WANT_CAR:
        this_agent.desire_car()

    this_agent.execute_sched(graph)
    

parser = argparse.ArgumentParser(description="process graph and station function")
parser.add_argument('nodes', metavar='NODES', type=str, help='Path to node file')
parser.add_argument('edges', metavar='EDGES', type=str, help='Path to edge file')
parser.add_argument('cities', metavar='CITIES', type=str, help='Path to cities file')
args = parser.parse_args()

p = Pool(200)

graph, cities = graph.read_graph(args.nodes, args.edges, args.cities)

neighborhoods = {}
work_areas = {}
city_dict = {}
num_nodes = len(graph.nodes)

for node in graph.nodes:
    neighborhoods[node] = []
    work_areas[node] = []
    if node.city in city_dict:
        city_dict[node.city].append(node)
    else:
        city_dict[node.city] = [node]

#create agents
agentList = []
for i in range(NUM_AGENTS):
    #set home to be current node
    #assign random nodes work
    schedule = []
    
    # Randomly set home and work (might be same neighborhood)
    home_index = random.randrange(0, num_nodes)
    home = graph.nodes[home_index]

    while home.city == "road":
        home_index = random.randrange(0, num_nodes)
        home = graph.nodes[home_index]

    home_city = home.city
    work_index = random.randrange(0, len(city_dict[home_city]) - 1)
    work = city_dict[home_city][work_index]

    for j in range(5):
        #start at home and then go to work
        weekday = [home, work]
        
        numDest = random.randrange(1, 5)
        for k in range(numDest):
            #assign a random node in the graph to be a destination
            randIndex = random.randrange(0, len(city_dict[home_city]) - 1)
            weekday.append(city_dict[home_city][randIndex])
            
        #return home
        weekday.append(home)
        schedule += weekday
    for j in range(2): #weekend
        #start at home
        weekend = [home]
        numDest = random.randrange(1, 10)

        for k in range(numDest):
            #create random destinations in graph
            if (random.randrange(1, 10) == 1):
                #1/10 of the time, go out of town
                randIndex = random.randrange(0, len(graph.nodes))
                weekend.append(graph.nodes[randIndex])
            else:
                randIndex = random.randrange(0, len(city_dict[home_city]) - 1)
                weekend.append(city_dict[home_city][randIndex])

        #return home
        weekend.append(home)
        schedule += weekend

    this_agent = agent.Agent(schedule)

    if random.random() < PROB_WANT_CAR:
        this_agent.desire_car()

    neighborhoods[home].append(this_agent)
    work_areas[work].append(this_agent)
    agentList.append(this_agent)

# Turn neighborhood into Neighborhood data structure
for node in neighborhoods.keys():
    agents = neighborhoods[node]
    neighborhood = agent.Neighborhood(agents)
    neighborhoods[node] = neighborhood

# Do same with work area
for node in work_areas.keys():
    agents = work_areas[node]
    work_area = agent.Neighborhood(agents)
    work_areas[node] = work_area

print "completed setup"

# Run actual simulation
for i in range(NUM_WEEKS):
    print i
    graph.update()

    #Parallel(n_jobs=NUM_AGENTS)(delayed(execute_agent_loop)(this_agent, graph) for agent in agentList)

    map((lambda x: execute_agent_loop(x, graph)), agentList)

    #jobs = []
    #for j in range(NUM_AGENTS):
    #    p = multiprocessing.Process(target=execute_agent_loop, args=(agentList[j], graph))
    #    jobs.append(p)
    #    p.start()

    #for job in jobs:
    #    job.join()

    # Neighborhood influence on desire to buy a car
    for node in neighborhoods.keys():
        neighborhoods[node].determine_car_desire()
    for node in work_areas.keys():
        work_areas[node].determine_car_desire()

    graph.clear_all_visits()

# statistics
num_cars = sum(map((lambda x: int(x.has_car)), agentList))
car_ratio = float(num_cars) / float(NUM_AGENTS)
num_want_cars = sum(map((lambda x: int(x.wants_car)), agentList))
num_didnt_get_car = num_want_cars - num_cars

print num_cars
print car_ratio
print num_want_cars
print num_didnt_get_car
