a=int(input('enter 1st number'))
b=int(input('enter 2st number'))
c=input('enter the operator we want to perform\n')
if   c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='**':
    print(a**b)
elif c=='//':
    print(a//b)
elif c=='%':
    print(a%b)
else:
    print("enter arithmetic operator")

