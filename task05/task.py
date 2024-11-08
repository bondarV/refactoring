class Buffer:
    def __init__(self):
        self.sequence = []

    def add(self, *a):
        self.sequence.extend(a)
        while len(self.sequence) >= 5:
            print(sum(self.sequence[:5]))
            self.sequence = self.sequence[5:]

    def get_current_part(self):
        return self.sequence


if __name__ == '__main__':
    buffer = Buffer()
    buffer.add(1, 2, 3.5)
    print(buffer.get_current_part())
    buffer.add(4, 5, 6)
    print(buffer.get_current_part())
    buffer.add(7, 8, 9, 10)
    print(buffer.get_current_part())
    buffer.add(11, 12)
    print(buffer.get_current_part())
