import math

def Split(number):
    num1 = ""
    num2 = ""         
    n = math.floor(len(str(number)) / 2)
    number = str(number)
    for i in range(0,n):
        num1 = num1 + (number[i])
        
    for j in range(n,len((number))):
        num2 = num2 + (number[j])
    
    return (num1),(num2)

def Multiply_Recursive(a,b):
    wy = 0
    xy = 0
    xz = 0
    wz = 0
    n = len(a)
    if((len(a) == 1) and (len(b) == 1)):
        return str(int(a)*int(b))
    else:
        if(len(a)%2 != 0):
            a = a.zfill(len(a) + 1)
            b = b.zfill(len(b) + 1)
            n = len(a)
        w,x = Split(a)
        y,z = Split(b)
        
        wy = float(Multiply_Recursive(w, y))
        xy = float(Multiply_Recursive(x, y))
        xz = float(Multiply_Recursive(x, z))
        wz = float(Multiply_Recursive(w, z))
        
        answer = (wy * pow(10,n)) + ((wz + xy) * pow(10,n/2)) + xz 
        return str(answer)
    
answer = Multiply_Recursive("123", "456")
print(answer)