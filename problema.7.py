def max(a,b):
    lista =[a,b]
    max=0
    for numar in lista:
        if numar>max:
            max = numar
    return max
def min(a,b):
    lista = [a,b]
    min = a
    for numar in lista:
        if numar<min:
            min = numar
    return min
def max_min(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    S=max(min(a1,a2), max(a3,a4)) + min(max(a5,a6), min(a7,a8))
    T = min(a1, a2) + min(a3, a4) + min(a5, a6) + min(a7, a8) + min(a9, a10) + max(a1, a2) + max(a3, a4) + max(a5, a6) + max(a7, a8) + max(a9, a10)
    return print('S=',S,'si T=',T)
b1=int(input('b1='))
b2=int(input('b2='))
b3=int(input('b3='))
b4=int(input('b4='))
b5=int(input('b5='))
b6=int(input('b6='))
b7=int(input('b7='))
b8=int(input('b8='))
b9=int(input('b9='))
b10=int(input('b10='))
print(max_min(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10))  