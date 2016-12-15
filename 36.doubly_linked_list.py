class Queue:
    def __init__(self):
        self.begin, self.end = None, None

    def push(self, other):
        if not self.begin:
            self.begin = self.end = [None, other, None]
        else:
            tmp = [None, other, self.begin]
            self.begin[0] = tmp
            self.begin = tmp

    def pop(self):
        assert self.end is not None
        result = self.end[1]
        if not self.end[0]:
            self.end = self.begin = None
        else:
            self.end = self.end[0]
            self.end[2] = None
        return result

a = Queue()
a.push(2)
a.push(5)
a.push(6)
a.push(7)
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
a.push(9)
a.push(17)
# print(a.pop())
# print(a.pop())