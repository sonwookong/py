class MoneyBox:
    def __init__(self, capacity):
        self.mon = 0
        self.capacity = capacity # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        return self.mon + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.mon += v