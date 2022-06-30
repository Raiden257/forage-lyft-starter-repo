from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.spindler_engine import SpindlerBattery


class Calliope(CapuletEngine):
    def __init__(self):
        self.engine=CapuletEngine
        self.battery=SpindlerBattery

    def needs_service(self):
        if(self.capulet_engine.needs_service==True or self.SpindlerBattery.needs_service==True):
            return True
        else: 
            return False
