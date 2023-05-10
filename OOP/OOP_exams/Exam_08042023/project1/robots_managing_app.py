from project1.services.main_service import MainService
from project1.services.secondary_service import SecondaryService
from project1.robots.male_robot import MaleRobot
from project1.robots.female_robot import FemaleRobot


class RobotsManagingApp:
    VALID_SERVICES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES.keys():
            raise Exception("Invalid service type!")
        service = self.VALID_SERVICES[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")
        robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        the_robot = next(filter(lambda x: x.name == robot_name, self.robots))
        the_service = next(filter(lambda x: x.name == service_name, self.services))
        if the_robot.__class__.__name__ == 'FemaleRobot' and the_service.__class__.__name__ == 'MainService':
            return "Unsuitable service."
        if the_robot.__class__.__name__ == 'MaleRobot' and the_service.__class__.__name__ == 'SecondaryService':
            return "Unsuitable service."
        if len(the_service.robots) == the_service.capacity:
            raise Exception("Not enough capacity for this robot!")
        the_service.robots.append(the_robot)
        self.robots.remove(the_robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        the_service = next(filter(lambda x: x.name == service_name, self.services))
        if robot_name not in [x.name for x in the_service.robots]:
            raise Exception("No such robot in this service!")
        the_robot = next(filter(lambda x: x.name == robot_name, the_service.robots))
        the_service.robots.remove(the_robot)
        self.robots.append(the_robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        the_service = next(filter(lambda x: x.name == service_name, self.services))
        for robot in the_service.robots:
            robot.eating()
        return f"Robots fed: {len(the_service.robots)}."

    def service_price(self, service_name: str):
        the_service = next(filter(lambda x: x.name == service_name, self.services))
        price = sum([x.price for x in the_service.robots])
        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        return '\n'.join([x.details() for x in self.services])
