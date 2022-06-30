from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.Spindler_Battery import SpindlerBattery

class Glissade(WilloughbyEngine):
    def __init__(self):
        self.WilloughbyEngine=WilloughbyEngine
        self.SpindlerBattery=SpindlerBattery

    def needs_service(self):
        if(self.willoughby_engine.needs_service==True or self.SpindlerBattery.needs_service==True):
            return True
        else: 
            return False
