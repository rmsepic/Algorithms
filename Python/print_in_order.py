# Leetcode problem
from threading import Event

class Foo:
    def __init__(self):
        self.second_event = Event()
        self.third_event = Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_event.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.second_event.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_event.set()
        


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.third_event.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()