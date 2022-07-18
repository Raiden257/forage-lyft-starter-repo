from datetime import datetime

from sternman_engine import SternmanEngine
from Spindler_battery import SpindlerBattery

class Palindrome(warning_light_is_on,last_service_date, current_date):
    def __init__(self):
        self.engine=SternmanEngine(warning_light_is_on)
        self.battery=SpindlerBattery(last_service_date, current_date)
    def needs_service(self):
        if(self.SternmanEngine_engine.needs_service==True or self.SpindlerBattery.needs_service==True):
            return True
        else: 
            return False
