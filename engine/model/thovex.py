from datetime import datetime

from capulet_engine import CapuletEngine
from nubbin_battery import NubbinBattery

class Thovex(current_mileage, last_service_mileage, current_date, last_service_date):
    def __init__(self):
        self.engine=CapuletEngine(current_mileage, last_service_mileage)
        self.battery=NubbinBattery(last_service_date, current_date)
        
    def needs_service(self):
        if(self.CapuletEngine.needs_service==True or self.NubbinBattery.needs_service==True):
            return True
        else: 
            return False