class reverse_iter:
    def __init__(self, values):
        self.values = values
        self.indx = -1
    def __iter__(self):
        return self

    def __next__(self):
        if self.indx < - len(self.values):
            raise StopIteration
        value_to_retrn = self.values[self.indx]
        self.indx -= 1
        return value_to_retrn

reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:
    print(item)
