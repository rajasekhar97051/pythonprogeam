num =int(input('enter'))

match num%2:
    case 0:
       print(num**2)
    case 1:
       print(num**3)
    case _:
       print('invalid input') 