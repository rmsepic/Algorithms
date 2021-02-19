# Leetcode problem

import threading

from threading import Lock
from typing import List

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.sem1 = Lock()
        self.sem2 = Lock()
        self.sem3 = Lock()
        self.sem2.acquire()
        self.sem3.acquire()
    
    def printNum(self, x: int) -> None:
        print(x)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
	    for i in range(1, self.n + 1):
	        self.sem1.acquire()
	        printNumber(0)
	        if i % 2 == 0:
	        	self.sem3.release()
	        else:
	        	self.sem2.release()
	          

    def even(self, printNumber: 'Callable[[int], None]') -> None:
	    for i in range(2, self.n + 1, 2):
	        self.sem3.acquire()
	        printNumber(i)
	        self.sem1.release()
	        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
        	self.sem2.acquire()
        	printNumber(i)
        	self.sem1.release()
        	

if __name__ == "__main__":
    zeo = ZeroEvenOdd(4)

    t1 = threading.Thread(group=None, target=zeo.zero, name="Thread A", args=[zeo.printNum])
    t2 = threading.Thread(group=None, target=zeo.odd, name="Thread B", args=[zeo.printNum])
    t3 = threading.Thread(group=None, target=zeo.even, name="Thread C", args=[zeo.printNum])

    t1.start()
    t2.start()
    t3.start()    
