import abc
import sys
from io import StringIO


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        pass

sys.stdin = StringIO('''Add 1
Add 2
Sum
List
Add 4
List
End
''')

ll = []
while True:
    command = input()
    if command == "End":
        break
    if command.startswith('Add'):
        _ , valuer_str = command.split()
        ll.append(int(valuer_str))
    elif command == 'List':
        print(ll)
    elif command == 'Sum':
        print(sum(ll))