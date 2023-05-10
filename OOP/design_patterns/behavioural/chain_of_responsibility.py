import abc


class Handler(abc.ABC):
    def __init__(self, next_handler = None):
        self.next_handler = next_handler
    @abc.abstractmethod
    def _handle(self, value):
        pass
    @abc.abstractmethod
    def _can_handle(self, value): #-> bool
        pass
    def handle(self, value):
        if not self._can_handle(value):
            return self.next_handler.handle(value)
        return self._handle(value)

class IntsHalndler(Handler):
    def _can_handle(self, value):
        return isinstance(value, int)

    def _handle(self, value):
        return f'{value} is int'

class FloatsHandler(Handler):
    def _can_handle(self, value):
        return isinstance(value, float)

    def _handle(self, value):
        return f'{value} is float'

class IntDivisionHandler(IntsHalndler):
    def __init__(self, base, next_handler=None):
        super().__init__(next_handler)
        self.base = base

    def _can_handle(self, value):
        return super()._can_handle(value) and value % self.base == 0

    def _handle(self, value):
        return super()._handle(value) + f'is dividable by {self.base}'


class AllHandler(Handler):
    def _can_handle(self, value):
        return True

    def _handle(self, value):
        return f'{value} is of unknown type'

hanlders =[
IntDivisionHandler(3),
    IntsHalndler(),
    FloatsHandler(),
    AllHandler()
]
for i in range(1, len(hanlders)):
    hanlders[i - 1].next_handler = hanlders[i]

value = ['a', 3, 35, 1.2567, 'peso', 85454.6, 4888, 26]
print('\n'.join([hanlders[0].handle(item) for item in value]))



