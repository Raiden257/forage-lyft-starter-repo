from datetime import datetime

from willoughby_engine import WilloughbyEngine
from nubbin_battery import NubbinBattery


class Rorschach(current_mileage, last_service_mileage, current_date, last_service_date):
    def __init__(self):
        self.engine= WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery=NubbinBattery(last_service_date, current_date)

    def needs_service(self):
        if(self.WilloughbyEngine.needs_service==True or self.NubbinBattery.needs_service==True):
            return True
        else: 
            return False
