
from abc import ABC, abstractmethod

from design_patterns.creational.animal_basic import Dog, Cat


class DataExporter(ABC):
    @staticmethod
    @abstractmethod
    def export(data):
        pass

class JsonDataExporter(DataExporter):
    @staticmethod
    def export(data):
        return json.dumps(data.__dict__)

class StringDataExporter(DataExporter):
    @staticmethod
    def export(data):
        return str(data)
    


def create_data_exporter(type):
    if type == 'json':
        return JsonDataExporter
    else:
        return StringDataExporter


the_type = 'json' 

de = create_data_exporter(the_type)
animals = [
    Dog('Sharo'),
    Cat('Mimi', 5)
]

[print(de.export(a)) for a in animals]

# 2nd Solution

import json
from abc import ABC, abstractmethod

from design_patterns.creational.animal_basic import Dog, Cat
from design_patterns.helpers.exporters import JsonDataExporter, StringDataExporter

class DataExporterBase(ABC):
    @abstractmethod
    def export(self, type, data):
        pass

class DataExporter(DataExporterBase):
    def export(self, type, data):
        if type == 'json':
            return json.dumps(data.__dict__)
        else:
            return str(data)

the_type = 'json' 

de = DataExporter()
animals = [
    Dog('Sharo'),
    Cat('Mimi', 5)
]


[print(de.export(the_type, a)) for a in animals]

