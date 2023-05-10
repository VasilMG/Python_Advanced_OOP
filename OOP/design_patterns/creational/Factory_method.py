from design_patterns.creational.animal_basic import Dog, Cat
from design_patterns.helpers.exporters import JsonDataExporter, StringDataExporter

class DataExporterFactory:  
    jason_exporter = None
    def create_exporter(self, type):
        if type == 'json':  
            if self.jason_exporter is None:
                self.jason_exporter = JsonDataExporter()
            return self.jason_exporter
        else:
            return StringDataExporter()


the_type = 'json'
factory = DataExporterFactory()
de = factory.create_exporter(the_type)
animals = [
    Dog('Sharo'),
    Cat('Mimi', 5)
]


[print(de.export(a)) for a in animals]