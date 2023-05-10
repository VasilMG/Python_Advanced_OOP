from  project1.services.base_service import BaseService

class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str, capacity=CAPACITY):
        super().__init__(name, capacity)

    def details(self):
        result = [f"{self.name} Main Service:"]
        if self.robots:
            second_line = f"Robots: {' '.join([x.name for x in self.robots])}"
        else:
            second_line = 'Robots: none'
        result.append(second_line)
        return '\n'.join(result)

