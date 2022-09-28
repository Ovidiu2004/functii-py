a1 = int(input('dati a1= '))
a2 = int(input('dati a2= '))
a3 = int(input('dati a3= '))
a4 = int(input('dati a4= '))
a5 = int(input('dati a5= '))
a6 = int(input('dati a6= '))
a7 = int(input('dati a7= '))
a8 = int(input('dati a8= '))
a9 = int(input('dati a9= '))
a10 =int(input('dati a10= '))

 
def maxim(x, y):
    if (x > y):
        return x
    elif y>x :
        return y
  
def minim(x, y):
    if (x < y):
        return x
    elif y<x :
        return y

def expresie():
    s=maxim(minim(a1,a2), maxim(a3,a4)) + minim(maxim(a5,a6), minim(a7,a8))
    T = minim(a1, a2) + minim(a3, a4) + minim(a5, a6) + minim(a7, a8) + minim(a9, a10) + maxim(a1, a2) + maxim(a3, a4) + maxim(a5, a6) + maxim(a7, a8) + maxim(a9, a10)

print(expresie())   