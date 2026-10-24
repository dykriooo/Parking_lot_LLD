"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum PaymentMode {
    CASH, UPI, CARD
}
"""
from enums import Enum 
class PaymentMode(Enum):
    CASH = "CASH"
    UPI ="UPI"
    CARD ="CARD"