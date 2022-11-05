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



def Karatsuba_Recursive(a,b):
    wy = 0
    xz = 0
    answer_2 = 0
    n = len(a)
    if(len(a) == 1):
        answer_2 = int(a) * int(b)
        return str(answer_2)
    else:
        w,x = Split(a)
        y,z = Split(b)
        if(len(a)%2 != 0):
            a = a.zfill(len(a) + 1)
            b = b.zfill(len(b) + 1)
            n = len(a)
        
        wy = float(Karatsuba_Recursive(w, y))
        xz = float(Karatsuba_Recursive(x, z))
        
        answer = (wy * pow(10,n)) + (((int(w)+int(x))*(int(y)+int(z))-wy-xz) * pow(10,n/2)) + xz 
        return str(answer)

answer = Karatsuba_Recursive("123", "456")
print(answer)