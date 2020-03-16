import unittest

class Stack:
    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def print_stack(self):
        print(self.items)

    def is_empty(self):
        return self.items == []

class MyQueue:
    def __init__(self):
        self.st1 = list()
        self.st2 = list()

    def enqueue(self, value):
        self.st1.append(value)

    def dequeue(self):
        if len(self.st2) == 0:
            while len(self.st1) > 0:
                self.st2.append(self.st1.pop())

        return self.st2.pop()


mq = MyQueue()
mq.enqueue(1)
mq.enqueue(2)

print(mq.dequeue())