from typing import List

RED = -1
BLUE = 1
WHITE = 0

def isBipartite(graph: List[List[int]]) -> bool:
	# colors is a list that keeps track of the node's groups
	colors = [WHITE for i in range(len(graph))]
	queue = []

	colors[0] = RED
	queue.append(0)

	while len(queue) != 0:
		print(queue)
		u = queue.pop()
		
		for v in graph[u]:
			if colors[v] == WHITE:
				colors[v] = colors[u] * -1 # Set this to the opposite
				queue.append(v)
			elif colors[v] == colors[u]:
				# Same color connecting. Not bipartite
				print(colors)
				return False

		if len(queue) == 0 and WHITE in colors:
			i = colors.index(WHITE) 
			colors[i] = RED
			queue.append(i)

	
	print(colors)
	return True



