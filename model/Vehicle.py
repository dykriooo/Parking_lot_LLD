"""
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

@Getter
@RequiredArgsConstructor
public abstract class Vehicle {
    private final String number;
    private final VehicleType type;
}
"""
from abc import ABC
from ..enums.VehicleType import VehicleType


class Vehicle(ABC):
    def __init__(self, number: str, vehicle_type: VehicleType):
        self.number = number
        self.vehicle_type = vehicle_type

    def getNumber(self) -> str:
        return self.number

    def getType(self) -> VehicleType:
        return self.vehicle_type
