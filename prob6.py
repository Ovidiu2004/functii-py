import math

a = int(input('dati a= '))
b = int(input('dati b= '))
c = int(input('dati c= '))
d = int(input('dati d= '))
 

def triunghi(x, y, z, k):

    if (x + y > z) or (x + z > y) or (y + z > x):
        p = x + y + z
        sp = p/2
        aria = math.sqrt (sp*(sp-x)*(sp-y)*(sp-z))
        return p, aria

    elif (y + z > k) or (z + k > y) or (y + k > z):
        p = y + z + k
        sp = p/2
        aria = math.sqrt(sp*(sp-y) * (sp-z) * (sp-k))
        return p, aria

    elif (y + z > k) or (x + k > y) or (y + k > x):
        p = y + x + k
        sp = p/2
        aria = math.sqrt(sp*(sp-x) *(sp-y) * (sp-k))
        return p, aria

    elif (x + z > k) or (z + k > x) or (z + k > x):
        p = x + z + k
        sp = p/2
        aria = math.sqrt(sp*(sp-x) * (sp-z) * (sp-k))
        return p, aria

    else:
        return "Nu exista triunghi cu asa laturi "    
 
print(triunghi())

