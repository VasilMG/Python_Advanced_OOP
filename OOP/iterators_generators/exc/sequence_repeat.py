class sequence_repeat:
    def __init__(self,sequence, the_number):
        self.sequence = sequence
        self.the_number = the_number
        self.indx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indx == self.the_number:
            raise StopIteration
        if self.indx >= len(self.sequence):
            times = self.indx // len(self.sequence)
            value = self.sequence[self.indx - (times * len(self.sequence))]
            self.indx += 1
            return value
        value = self.sequence[self.indx]
        self.indx += 1
        return value



result = sequence_repeat('abc', 10)

for item in result:
    print(item, end ='')

# result = sequence_repeat('I Love Python', 3)
#
# for item in result:
#     print(item, end ='')
