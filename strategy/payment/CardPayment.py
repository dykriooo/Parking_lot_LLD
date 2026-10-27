from .PaymentStrategy import PaymentStrategy


class CardPayment(PaymentStrategy):
    def processPayment(self, ticket, amount: float) -> bool:
        print(f"Paid ₹{amount} for ticket {ticket.getTicketId()} via Card.")
        return True