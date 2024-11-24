#Реализация 1: Циклический буфер на основе списка
"""
1.Полный контроль
2.Сложнее в реализации
3.Гибкая настройка
4.Отсутствие внешних библиотек
"""
class CircularBufferList:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def append(self, item):
        self.buffer[self.tail] = item
        if self.count == self.size:
            self.head = (self.head + 1) % self.size
        else:
            self.count += 1
        self.tail = (self.tail + 1) % self.size

    def get(self):
        if self.count == 0:
            raise IndexError("Буфер пуст")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def __repr__(self):
        return f"CircularBufferList({self.buffer}, head={self.head}, tail={self.tail}, count={self.count})"
    
#Реализация 2: Циклический буфер на основе deque
"""
1.Меньше контроля
2.Проще и короче
3.Ограничена функциональность
"""
from collections import deque

class CircularBufferDeque:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def append(self, item):
        self.buffer.append(item)

    def get(self):
        if len(self.buffer) == 0:
            raise IndexError("Буфер пуст")
        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.buffer.maxlen

    def __repr__(self):
        return f"CircularBufferDeque({list(self.buffer)})"