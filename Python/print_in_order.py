# Leetcode problem
import threading 
from threading import Event

class Foo:
    def __init__(self):
        self.second_event = Event()
        self.third_event = Event()

    def pF(self):
        print("First")

    def pS(self):
        print("Second")

    def pT(self):
        print("Third")

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.second_event.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.second_event.wait()
        printSecond()
        self.third_event.set()
        


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.third_event.wait()
        printThird()

if __name__ == "__main__":
    foo = Foo()

    t1 = threading.Thread(group=None, target=foo.first, name="Thread A", args=[foo.pF])
    t2 = threading.Thread(group=None, target=foo.second, name="Thread B", args=[foo.pS])
    t3 = threading.Thread(group=None, target=foo.third, name="Thread C", args=[foo.pT])

    t2.start()

    t1.start()
    
    t3.start()