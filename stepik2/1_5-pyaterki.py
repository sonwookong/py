class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.sps = []
    def add(self, *a):
        # добавить следующую часть последовательности
        vsps = self.sps + list(a)
        self.sps = []
        for x in range(0, len(vsps), 5):
            ec = vsps[x: 5 + x]
            if len(ec) < 5:
                self.sps = ec
            else:
                print(sum(ec))

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        return self.sps

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]