def vowels(string):
    vowels='hai hia'
    out=''
    for i in string: 
       if i in vowels:
           out+=i
           return out
       def extract(st):
           res=''
           for j in 'aeiouAEIOU':
               if j not in st:
                   res +=j
                   return j
           return res
    print(extract(filter('hello')))                   