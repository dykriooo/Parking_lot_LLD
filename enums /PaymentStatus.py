"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum PaymentStatus {
    PENDING,
    SUCCESS,
    FAILED
}
"""
from enums import Enum 
class PaymentStatus(Enum):
    PENDING ="PENDING"
    SUCCESS = "SUCCESS"
    FAILED ="failed"