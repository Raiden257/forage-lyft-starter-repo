from datetime import datetime

from engine.sternman_engine import SternmanEngine
from battery.Spindler_battery import SpindlerBattery

class Palindrome(SternmanEngine):
    def __init__(self):
        self.SternmanEngine=SternmanEngine
        self.SpindlerBattery=SpindlerBattery
    def needs_service(self):
        if(self.SternmanEngine_engine.needs_service==True or self.SpindlerBattery.needs_service==True):
            return True
        else: 
            return False
