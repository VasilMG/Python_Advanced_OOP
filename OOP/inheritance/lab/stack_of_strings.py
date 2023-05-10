# test zero
import unittest


class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push("apple")
        stack.push("carrot")
        self.assertEqual(str(stack), '[carrot, apple]')
        self.assertEqual(stack.pop(), 'carrot')
        self.assertEqual(stack.top(), 'apple')
        stack.push("cucumber")
        self.assertEqual(str(stack), '[cucumber, apple]')
        self.assertEqual(stack.is_empty(), False)


if __name__ == '__main__':
    unittest.main()


class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise TypeError('Please give a string type.')
        self.data.append(element)
    def pop(self):
        return self.data.pop()
    def top(self):
        return self.data[-1]
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def __str__(self):
        return f'[{", ".join(sorted(self.data, reverse= True))}]'

