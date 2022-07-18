from abc import ABC

class Octoprime_tires(ABC,tire1,tire2,tire3,tire4):
    def __init__(self):
           pass
          
    def needs_service(self):
        if((tire1+tire2+tire3+tire4)<=3):
            return True
            
        else:
            return False