from wild_zoo.project import Customer
from wild_zoo.project import Trainer
from wild_zoo.project import Equipment
from wild_zoo.project import ExercisePlan
from wild_zoo.project import Subscription
class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        for s in self.subscriptions:
            if s.id == subscription_id:
                the_subs = s
        for c in self.customers:
            if c.id == the_subs.customer_id:
                the_cust = c
        for t in self.trainers:
            if t.id == the_subs.trainer_id:
                the_trainer = t
        for p in self.plans:
            if p.id == the_subs.exercise_id:
                the_plan = p
        for e in self.equipment:
            if e.id == the_plan.equipment_id:
                the_equ = e
        return repr(the_subs) + '\n' + repr(the_cust) + '\n' + repr(the_trainer) + '\n' + repr(the_equ) +\
            '\n' + repr(the_plan)

