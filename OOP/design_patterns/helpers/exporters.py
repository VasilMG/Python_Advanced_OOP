import json
from abc import ABC, abstractmethod

class DataExporter(ABC):
    @staticmethod
    @abstractmethod
    def export(data):
        pass
# Adapter - structural DP
class JsonDataExporter(DataExporter):
    @staticmethod
    def export(data):
        return json.dumps(data.__dict__)
# Adapter - structural DP
class StringDataExporter(DataExporter):
    @staticmethod
    def export(data):
        return str(data)
