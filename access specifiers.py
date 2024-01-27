class cname:
   _a=10
   b=20
   def __init__(self,c,d):
     self._c = c
     self.d = d
   def _disply(self):
    print(self._c,self.d)

   @classmethod
   def classdiplay(cls):
    print(cls._a,cls.b)


    obj=cname(3,4)