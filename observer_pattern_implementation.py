class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.observers: list = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def set_price(self, new_price):
        self.price = new_price
        self.notify_observers()


class Dashboard:
    def __init__(self, stock):
        self.stock = stock

    def update(self):
        print(f"Dashboard updated: {self.stock.name} is now {self.stock.price}")


apple_stock = Stock("apple", 100)
tesla_stock = Stock("tesla", 200)

dashboard = Dashboard(apple_stock)
