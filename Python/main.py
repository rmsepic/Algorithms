import threading

from print_in_order import Foo

from shortest_path_binary_matrix import shortestPathBinaryMatrix
from is_bipartite import isBipartite

from max_heap import MaxHeap

if __name__ == "__main__":
	foo = Foo()

	t1 = threading.Thread(group=None, target=foo.first, name="Thread A", args=[foo.pF])
	t2 = threading.Thread(group=None, target=foo.second, name="Thread B", args=[foo.pS])
	t3 = threading.Thread(group=None, target=foo.third, name="Thread C", args=[foo.pT])

	t2.start()

	t1.start()
	
	t3.start()

	