from .PaymentStrategy import PaymentStrategy


class UPIPayment(PaymentStrategy):
    def processPayment(self, ticket, amount: float) -> bool:
        print(f"Paid ₹{amount} for ticket {ticket.getTicketId()} via UPI.")
        return True