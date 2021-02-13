# Shortest Path Binary Matrix problem
# Leetcode challenge from 13 Feb 2021

# Problem is to find the shortest path from the upper left of a matrix to the lower right
# Each cell can be either a 0 or a 1

import sys
import heapq

from typing import List

class Coord:
	def __init__(self, x: int, y: int, dist: int):
		self.x = x
		self.y = y
		self.dist = dist


# Make sure it is not out of bounds
def withinRange(x: int, y: int, tot_x: int, tot_y: int):
	return (x >= 0) and (y >= 0) and (x < tot_x) and (y < tot_y)

def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
	if grid[0][0] == 1:
		return -1

	# Set distances to maximum
	#dist = [sys.maxsize] * size
	visited = [ [False for i in range(len(grid))] for j in range(len(grid[0]))]
	pq = []	# Priority queue
	c = Coord(0, 0, 1)
	pq.append(c)
	visited[0][0] = True

	print(pq)

	while len(pq) != 0:
		v = pq.pop(0)
		print(visited)
		print(len(pq))

		if v.x == len(grid) - 1 and v.y == len(grid[0]) - 1:
			return v.dist

		for i in range(-1, 2):
			row = v.x + i
			for j in range(-1, 2):
				col = v.y + j

				if withinRange(row, col, len(grid), len(grid[0])) and grid[row][col] == 0 and visited[row][col] == False:
					visited[row][col] = True
					pq.append(Coord(row, col, v.dist + 1))


	return -1



