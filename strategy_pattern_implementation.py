from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing ${amount} payment using Credit Card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing ${amount} payment using PayPal")


class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing ${amount} using Cryptocurrency")


class PaymentProcessor:
    @staticmethod
    def process_payment(strategy: PaymentStrategy, amount):
        strategy.pay(amount)


processor = PaymentProcessor()
processor.process_payment(CreditCardPayment(), 100)
processor.process_payment(PayPalPayment(), 200)
