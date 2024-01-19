import random 
number = random.randint(100,1000)
while True:
a=int(input('enter a number:-') )
if a== number:
    print(congrats! you successfully gused the number,a )
     break
 elif a < number:
    prnt('enter some grater number')
else:
   print('entersome lesser number')