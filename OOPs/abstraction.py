from abc import ABC, abstractmethod
 class Car(ABC): //abstract class
 def mileage(self): //abstract method
 pass
 class Tesla(Car):
 def mileage(self):
 print("The mileage is 30kmph")
 class Suzuki(Car):
 def mileage(self):
 print("The mileage is 25kmph ")
 t= Tesla()
 t.mileage()
 s =Suzuki()
 s.mileage()