def findCriticalNodes(numNodes, edges):
	# Pick a vertex
	# Then do a BTS and see if the graph is connected

	ans = []
	vertices = []
	for i in range(0, numNodes):
		vertices.append([])
		# Find vertexs that connect to i	
		for e in edges:
			if e[0] == i:
				vertices[i].append(e[1])
			elif e[1] == i:
				vertices[i].append(e[0])

	print(vertices)

	for v in range(0, numNodes):
		temp_edges = edges 
		
		visited = [False] * (len(temp_edges))
		visited[v] = True
		queue = []
		if v != 0:
			queue.append(vertices[0])
			visited[0] = True
		else:
			queue.append(vertices[1])
			visited[1] = True
		
		# BTS on temp_edges
		while len(queue) != 0:
			vertex = queue.pop()
			print(vertex)
			for i in vertex:
				if visited[i] == False:
					queue.append(vertices[i])
					visited[i] = True

			print(visited)
		if all(vis == True for vis in visited) == False:
			ans.append(v)

	return ans




if __name__ == "__main__":
	numNodes = 6
	edges =  [[0, 2], [1, 3], [2, 4], [3, 5], [4, 5], [5, 4]]
	ans = findCriticalNodes(numNodes, edges)
	print(ans)
