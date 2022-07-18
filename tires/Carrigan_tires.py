from abc import ABC

class Carrigan_tires(ABC, tire1, tire2,tire3, tire4)
    def __init__(self):
           pass
          
    def needs_service(self):
        if((tire1>=0.9) or (tire2>=0.9) or (tire3>=0.9) or (tire4>=0.9)):
            return True
            
        else:
            return False
            