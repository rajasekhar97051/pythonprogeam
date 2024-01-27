from abc import ABC,abstractmethod
class modelcar():
    @abstractmethod
    def Break():
         pass
    @abstractmethod
    def speed_up():
         pass
class Nexon(Modelcar):
     def _init_(self,speed=0,stop=True):
          self.speed = speed
          self.stop  =stop
     def speed_up(self):
          self.speed+=5
          self.stop =False
     def stop(self):
          self.speed =0
          self.stop  =True   
                
   