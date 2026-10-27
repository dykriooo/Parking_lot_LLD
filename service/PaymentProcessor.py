from ..enums.PaymentStatus import PaymentStatus
from ..strategy.payment.PaymentStrategy import PaymentStrategy


class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def pay(self, ticket, amount: float) -> bool:
        success = self.strategy.processPayment(ticket, amount)
        if success:
            ticket.setPaymentStatus(PaymentStatus.SUCCESS)
        else:
            ticket.setPaymentStatus(PaymentStatus.FAILED)
            print("Payment failed for ticket: " + ticket.getTicketId())
        return success