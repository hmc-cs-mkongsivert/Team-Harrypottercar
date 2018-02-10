#Engine
import random

numAgents = 100

#create agents
agentList = []
for i in range(numAgents):
	agent = Agent()
	#set home to be current node
	#assign random nodes work
	schedule = []
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