from design_patterns.creational.animal_basic import Cat
from design_patterns.helpers.exporters import DataExporter, JsonDataExporter
# for Adapter DP --> see helpers --> exporters

class EncryptDataExporter(DataExporter):
    def __init__(self, exporter):
        self.exporter = exporter

    def __encrypt(self, value):
        return f'---{value}---'


    def export(self, data):
        for key in data.__dict__.keys():
            value = getattr(data, key)
            encrypted_value = self.__encrypt(value)
            setattr(data, key, encrypted_value)
        return self.exporter.export(data)

exporter = EncryptDataExporter(JsonDataExporter())
cat = Cat("sharo", 92)

print(exporter.export(cat))