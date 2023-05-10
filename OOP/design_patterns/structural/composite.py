import abc
import os
import uuid
from abc import abstractmethod
class UiComponent(abc.ABC):
    def __init__(self, identifier):
        self.identifier = identifier
    @abstractmethod
    def get_representation(self):
        pass

    def __str__(self):
        return self.get_representation()

class Heading(UiComponent):
    def __init__(self, identifier, text):
        super().__init__(identifier)
        self.text = text

    def get_representation(self):
        return f'*{self.text}*'

class Button(UiComponent):
    def __init__(self, identifier, text, func):
        super().__init__(identifier)
        self.text = text
        self.func = func

    def click(self, *args, **kwargs):
        return self.func(self, *args, **kwargs)



    def get_representation(self):
        return f'[{self.text}]'

class Text(UiComponent):
    def __init__(self, identifier, text):
        super().__init__(identifier)
        self.text = text

    def get_representation(self):
        return self.text
    
# COMPOSITE
class Container(UiComponent):
    def __init__(self, identifier, children = None):
        super().__init__(identifier)
        if children == None:
            children = []
        self.children = children

    def get_representation(self):
        return '\n'.join([c.get_representation() for c in self.children])


print(Container('cont1', [
    Heading('head1', 'Does it work'),
    Button('but1', 'Maybe it works', None)
]))


class UiComponentsComposition(UiComponent):
    def __init__(self, identifier, children = None):
        super().__init__(identifier)
        if children == None:
            children = []
        self.children = children

class Container1(UiComponentsComposition):
    def get_representation(self):
        return ' '.join([c.get_representation() for c in self.children])

class VerticalList(UiComponentsComposition):
    def get_representation(self):
        return os.linesep.join([f'--- c.get_representation()' for c in self.children])

class NewLine(UiComponent):
    def __init__(self):
        super().__init__(uuid.uuid4()) 

    def get_representation(self):
        return os.linesep