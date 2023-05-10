from project1.client import Client


class FoodOrdersApp:
    MEALS = ["Starter", "MainDish", "Dessert"]
    RECEIPT_ID = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    # -------------------------------------------------------------------------------------
    def __check_if_client_is_registered(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return True

    def __validate_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def __find_client(self, phone_number: str):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    #----------------------------------------------------------------------------------------

    def register_client(self, client_phone_number: str):
        numbers = [x.phone_number for x in self.clients_list]
        if client_phone_number in numbers:
            raise Exception("The client has already been registered!")
        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ not in self.MEALS:
                continue
            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return '\n'.join([x.details() for x in self.menu])
        
    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantity):
        self.__validate_menu()
        if not self.__check_if_client_is_registered(client_phone_number):
            self.register_client(client_phone_number)
        client = self.__find_client(client_phone_number)
        meals_to_order = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantity.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantity.items():
            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0
            client.ordered_meals[meal_name] += meal_quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        for ordered_meal, quantity in client.ordered_meals.items():
            for menu_meal in self.menu:
                if ordered_meal == menu_meal.name:
                    menu_meal.quantity += quantity
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}
        return f"Client {client_phone_number} successfully canceled his order."



    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        self.RECEIPT_ID += 1
        current_bill = client.bill
        client.shopping_cart = []
        client.bill = 0
        return f"Receipt #{self.RECEIPT_ID} with total amount of {current_bill:.2f} " \
               f"was successfully paid for {client_phone_number}."



    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."









