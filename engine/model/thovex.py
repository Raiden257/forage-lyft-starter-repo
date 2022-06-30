from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery

class Thovex(CapuletEngine):
    def __init__(self):
        self.CapuletEngine=CapuletEngine
        self.NubbinBattery=NubbinBattery
        
    def needs_service(self):
        if(self.CapuletEngine.needs_service==True or self.NubbinBattery.needs_service==True):
            return True
        else: 
            return False