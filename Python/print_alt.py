# Leetcode concurrency problem

import threading
from threading import Event

class FooBar:
    def __init__(self, n):
        self.n = n
        self.e1 = Event()
        self.e2 = Event()
        self.e1.set()

    def print_foo(self):
        print("foo")

    def print_bar(self):
        print("bar")

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.e1.wait() # e1 waiting for flag == true
            printFoo() 
            self.e1.clear() # e1 flag == false
            self.e2.set() # e2 flag == true


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.e2.wait()  # e2 waiting for flag == true
            printBar()
            self.e2.clear() # e2 flag == false
            self.e1.set() # e2 flag == true
            

if __name__ == "__main__":
    foobar = FooBar(3)
    t1 = threading.Thread(group=None, target=foobar.foo, name="Thread A", args=[foobar.print_foo])
    t2 = threading.Thread(group=None, target=foobar.bar, name="Thread B", args=[foobar.print_bar])

    t2.start()
    t1.start()
    

    