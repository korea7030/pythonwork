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
        self.st1 = Stack()
        self.st2 = Stack()

    def enqueue(self, value):
        self.st1.add(value)

    def dequeue(self):
        if self.st2.is_empty():
            while self.st1.is_empty() is False:
                self.st2.add(self.st1.pop())

        return self.st2.pop()


class test(unittest.TestCase):
    def test(self):
        mq = MyQueue()
        mq.enqueue(1)
        mq.enqueue(2)

        self.assertEqual(1, mq.dequeue())
        mq.enqueue(3)
        self.assertEqual(2, mq.dequeue())

unittest.main()