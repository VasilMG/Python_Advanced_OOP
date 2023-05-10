import abc
import sys
from io import StringIO


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        pass
class AddCommand(Command):
    def __init__(self, values, value):
        self.values = values
        self.value = value
    def execute(self, *args, **kwargs):
        self.values.append(self.value)
class ListCommand(Command):
    def __init__(self, values):
        self.values = values

    def execute(self, *args, **kwargs):
        return self.values

class SumCommand(Command):
    def __init__(self, values):
        self.values = values
    def execute(self, *args, **kwargs):
        return sum(self.values)


sys.stdin = StringIO('''Add 1
Add 2
Sum
List
Add 4
List
End
''')

ll = []
commands =[]

while True:
    command = input()
    if command == "End":
        break
    if command.startswith('Add'):
        _ , valuer_str = command.split()
        commands.append(AddCommand(ll, int(valuer_str)))
    elif command == 'List':
        commands.append(ListCommand(ll))
    elif command == 'Sum':
        commands.append(SumCommand(ll))

print(ll)
for c in commands:
    result = c.execute()
    if result:
        print(c.execute())