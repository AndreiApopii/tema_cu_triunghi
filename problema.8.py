import math
def med_lat(a,b,c):
    if (a+b>c)and(a+c>b)and(c+b>a):
        ma=0.5*(math.sqrt((2*(b**2))+(2*(c**2))-(a**2)))
        mb=0.5*(math.sqrt((2*(a**2))+(2*(c**2))-(b**2)))
        mc=0.5*(math.sqrt((2*(b**2))+(2*(a**2))-(c**2)))
        return print('meiana laturii',a,'este',ma,'a laturii',b,'este',mb,'si a laturii',c,'este',mc)
    else:
        return print('nu formeaza triunghi')
la=int(input('la='))
lb=int(input('lb='))
lc=int(input('lc='))
med_lat(la,lb,lc)

