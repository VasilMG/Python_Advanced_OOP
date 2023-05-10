class take_skip:
    def __init__(self, step, count):
        self.step =step
        self.count = count
        self.next_value = 0
        self.the_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.the_count += 1
        if self.the_count > self.count:
            raise StopIteration
        value_to_return = self.next_value
        self.next_value += self.step
        return value_to_return

# numbers = take_skip(2, 6)
#
# for number in numbers:
#     print(number)

numbers = take_skip(10, 5)

for number in numbers:
    print(number)