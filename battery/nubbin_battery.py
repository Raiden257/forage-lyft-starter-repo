from abc import ABC
from datetime import datetime



class NubbinBattery(ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        
    
    def needs_service(self):
        if(self.current_date.year- self.last_service_date.year>4):
            return True
            
        else:
            return False