from datetime import datetime

from willoughby_engine import WilloughbyEngine
from Spindler_battery import SpindlerBattery

class Glissade(current_mileage, last_service_mileage, current_date, last_service_date):
    def __init__(self):
        self.engine=WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery=SpindlerBattery(last_service_date, current_date)

    def needs_service(self):
        if(self.willoughby_engine.needs_service==True or self.SpindlerBattery.needs_service==True):
            return True
        else: 
            return False
