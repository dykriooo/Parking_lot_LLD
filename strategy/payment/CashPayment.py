from .PaymentStrategy import PaymentStrategy


class CashPayment(PaymentStrategy):
    def processPayment(self, ticket, amount: float) -> bool:
        print(f"Paid ₹{amount} for ticket {ticket.getTicketId()} via Cash.")
        return True