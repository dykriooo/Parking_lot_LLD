from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def processPayment(self, ticket, amount: float) -> bool:
        pass