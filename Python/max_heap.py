class MaxHeap:
	def __init__(self):
		self.heap = []

	def parent(self, pos: int) -> int:
		return (pos - 1) // 2 if (pos - 1) // 2 >= 0 else 0

	def left_node(self, pos: int) -> int:
		return 2 * pos + 1

	def right_node(self, pos: int) -> int:
		return 2 * pos + 2

	# Insert into the ending of the heap array
	def insert(self, elem: int):
		self.heap.append(elem)
		idx = len(self.heap) - 1

		while elem > self.heap[self.parent(idx)]:
			self.swap(idx, self.parent(idx))
			idx = self.parent(idx)

	def swap(self, new: int, old: int):
		self.heap[new], self.heap[old] = self.heap[old], self.heap[new]
