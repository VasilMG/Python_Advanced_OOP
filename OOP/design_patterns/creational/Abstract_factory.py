from abc import ABC, abstractmethod
from design_patterns.helpers.exporters import JsonDataExporter


class DataExporterFactory(ABC):
    @abstractmethod
    def create_exporter(self):
        pass

class JsonExporterFactory(DataExporterFactory):
    exporter = None
    def create_exporter(self):
        if self.exporter == None:
            self.exporter = JsonDataExporter()
        return self.exporter
