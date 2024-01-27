class mtca:
     chairman ='mr.sunil'
     location ='palamaner'
     college  ='mtca'
     def __init__(self,name,mobile):
          self.name = name
          self.mobile = mobile
    

class Mca(mtca):
     principal ='mr.prabhakar naidu'
     strength =240
     staff    =9

class Btech(mtca):
     principal ='ms.sravani'
     strength  =350
     staff     =35

navyasree =Mca('navyasree',7686956467)
rajasekhar =Btech('rajasekhar',9705106971)   