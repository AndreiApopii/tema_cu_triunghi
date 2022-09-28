import math
def inaltime(a,b,c):
    if (a+b>c) and (b+c>a) and (a+c>b):
        sp =(a+b+c)/2
        A = math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
        ha=(2*A)/a
        hb=(2*A)/b
        hc=(2*A)/c
        return print('inaltimea pe latura',a,'este',ha,'pe latura',b,'este',hb,'iar pe latura',c,'este',hc)
    else:
        return print('laturile nu formeaza triunghi')
lata=int(input('a='))
latb=int(input('b='))
latc=int(input('c='))
inaltime(lata,latb,latc)