from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery


class Rorschach(WilloughbyEngine):
    def __init__(self):
        self.WilloughbyEngine= WilloughbyEngine
        self.NubbinBattery=NubbinBattery

    def needs_service(self):
        if(self.WilloughbyEngine.needs_service==True or self.NubbinBattery.needs_service==True):
            return True
        else: 
            return False
