from datetime import datetime
from calliope import calliope
from glissade import glissade
from palindrome import palindrome
from rorschach import rorschach
from thorvex import thorvex
from Carrigan_tires import carrigan_tires
from Octoprime_tires import octoprime_tires

class Car_factory():
    def __init_(self):
        pass
    
    def create_calliope():
        car = calliope(current_mileage, last_service_mileage, current_date, last_service_date)
        car.tires=octoprime_tires
        return car
    
    def create_glissade():
        car = glissade(current_mileage, last_service_mileage, current_date, last_service_date)
        car.tires=carrigan_tires
        return car
    
    def create_palindrome():
        car = palindrome(current_mileage, last_service_mileage, current_date, last_service_date)
        car.tires= octoprime_tires
        return car
    
    def create_rorschach():
        car = rorschach(current_mileage, last_service_mileage, current_date, last_service_date)
        car.tires=carrigan_tires
        return car
    
    
   def create_thorvex():
        car = thorvex(current_mileage, last_service_mileage, current_date, last_service_date)
        car.tires=octoprime_tires
        return car
    
