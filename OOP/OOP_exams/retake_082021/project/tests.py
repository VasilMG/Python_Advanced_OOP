from appliances.fridge import Fridge
from appliances.laptop import Laptop
from project.people.child import Child
from project.appliances.tv import TV
from project.appliances.stove import Stove
from project.rooms.alone_young import AloneYoung
from rooms.alone_old import AloneOld
from rooms.old_couple import OldCouple
from rooms.room import Room
from rooms.young_couple_with_children import YoungCoupleWithChildren

from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren
from people.child import Child
from everland import Everland

everland = Everland()

def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)
    proba = OldCouple('pesho', 10, 10)
    print(proba.budget)
    print(proba.expenses)
    print(proba.members_count)
    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()
