def even(value):
    flag =False
    if value%2==0:
      flag=True
      return flag
def squadd(a,b):
    return a**2 +b**2

def add(a,b):
    return a+b
def index_value(arr):
     out=[]
     for i in range(len(arr)):
         if not(even(i)^even(arr[i])):
             out+=[squadd(i,arr[i])]

         else:
             out+=[add(i,arr[i])]
             return out
         print(index_value([2,4,9,7,11,2,4,3,5,7,6]))
    
    
