class Order:
    TAX_RATE = 0.08
    SERVICE_CHARGE = 0.05

    def __init__(self, customer):
        self.customer = customer
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def remove_dish(self, dish):
        if dish in self.dishes:
            self.dishes.remove(dish)
        else:
            raise ValueError("Такого блюда нет в заказе.")

    def calculate_total(self):
        return sum(dish.price for dish in self.dishes)

    def apply_discount(self):
        discount_rate = self.customer.get_discount() / 100
        return self.calculate_total() * (1 - discount_rate)

    def final_total(self):
        total_after_discount = self.apply_discount()
        total_with_tax = total_after_discount * (1 + Order.TAX_RATE)
        return total_with_tax * (1 + Order.SERVICE_CHARGE)

    def __str__(self):
        dish_list = "\n".join(str(dish) for dish in self.dishes)
        return f"Order for {self.customer.name}:\n{dish_list}\nTotal: ${self.final_total():.2f}"


class GroupOrder(Order):
    def __init__(self, customers):
        super().__init__(customer=None)
        self.customers = customers

    def split_bill(self):
        if not self.customers:
            raise ValueError("Нет клиентов для разделения счета.")
        return self.final_total() / len(self.customers)
