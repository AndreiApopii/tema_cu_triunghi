import math

def aria(a,b,c,d):
    if (a+b>c) and (a+c>b) and (b+c>a):
        sp =(a+b+c)/2
        aria = math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
        p=a+b+c
        return print('laturile',a,b,c,'pot forma un triunghi cu aria de',aria,'si perimetrul',p)
    elif (a+b>d) and (a+d>b) and (b+d>a):
        sp = (a+b+d)/2
        aria = math.sqrt(sp*(sp-a) * (sp-b) * (sp-d))
        p=a+b+d
        return print('laturile',a,b,d,'pot forma un triunghi cu aria de',aria,'si perimetrul',p)
    elif (a+c>d) and (a+d>c) and (c+d>a):
        sp = (a+c+d)/2
        aria = math.sqrt(sp*(sp-a) *(sp-c) * (sp-d))
        p=a+c+d
        return print('laturile',a,c,d,'pot forma un triunghi cu aria de',aria,'si perimetrul',p) 
    elif (b+c>d) and (b+d>c) and (c+d>b):
        sp = (b+c+d)/2
        aria = math.sqrt(sp*(sp-b) * (sp-c) * (sp-d))
        return print('laturile',b,c,d,'pot forma un triunghi cu aria de',aria,'si perimetrul',p)
    else:
        return ('laturile nu formeaza triunghi')    
x=int(input('x='))
y=int(input('y='))
z=int(input('z='))
q=int(input('q='))
print(aria(x,y,z,q))