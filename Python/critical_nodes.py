def findCriticalNodes(numNodes, edges):
	vertices = []
	ans = []
	# Pick a vertex
	for i in range(0, numNodes):
		vertices.append([])
		# Find vertexs that connect to i	
		for e in edges:
			if e[0] == i:
				vertices[i].append(e[1])
			elif e[1] == i:
				vertices[i].append(e[0])

	# Check if the vertices in v have edges to anything
	for i in range(0, numNodes):
		for v in vertices[i]:
			print(v)
			if len(vertices[v]) == 1 and vertices[v][0] == i:
				# Only vertex i is connected to v
				ans.append(i)

	return ans




if __name__ == "__main__":
	numNodes = 7
	edges =  [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]
	ans = findCriticalNodes(numNodes, edges)
	print(ans)
