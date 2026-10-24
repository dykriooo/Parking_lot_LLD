from abc import ABC, abstractmethod
from ...model.Ticket import Ticket


class PaymentStrategy(ABC):
    @abstractmethod
    def processPayment(self, ticket: Ticket, amount: float) -> bool:
        pass
    