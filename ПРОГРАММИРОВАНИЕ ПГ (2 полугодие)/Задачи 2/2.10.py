class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount

    def remove_stock(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Insufficient stock available.")

    def calculate_total_value(self):
        return self.price * self.quantity


product = Product("Apple", 10, 50)
product.add_stock(10)
product.remove_stock(5)
print(product.calculate_total_value())
