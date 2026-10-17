from abc import ABC, abstractmethod


class VendingMachine:
    def __init__(self):
        self.snacks = 5
        self.idle_state = IdleState()
        self.has_money_state = HasMoneyState()
        self.out_of_stock_state = OutOfStockState()
        self.state = self.idle_state

    def handle(self, action):
        self.state.handle(self, action)


class State(ABC):
    @abstractmethod
    def handle(self, machine: VendingMachine, action):
        pass


class IdleState(State):
    def handle(self, machine: VendingMachine, action):
        if action == "insert_coin":
            machine.state = machine.has_money_state
        else:
            print("Insert a coin first")


class HasMoneyState(State):
    def handle(self, machine: VendingMachine, action):
        if action == "select_snack":
            if machine.snacks > 0:
                machine.snacks -= 1
                machine.state = machine.idle_state
                print("Dispensing your snack.")
            else:
                machine.state = machine.out_of_stock_state
                print("Out of stock! Refund initiated")
        else:
            print("Please select a snack")


class OutOfStockState(State):
    def handle(self, machine: VendingMachine, action):
        print("Sorry, no snacks left.")
