import re 
pattern='[Aa][Pp] ?[0-3][1-9] ?[A-Za-z] ?[0-9]{4}'
data=re.findall(pattern,'AP01 a 1234')
print(data)