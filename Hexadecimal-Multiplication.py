import math

def ConverttoNumber(hexDigit):
    if(hexDigit == "A"):
        return 10

    elif(hexDigit == "B"):
        return 11
    
    elif(hexDigit == "C"):
        return 12
    
    elif(hexDigit == "D"):
        return 13
    
    elif(hexDigit == "E"):
        return 14
    
    elif(hexDigit == "F"):
        return 15
    
    else:
        return hexDigit
    
def ConverttoAlphabet(hexDigit):
    if(hexDigit == 10):
        return "A"

    elif(hexDigit == 11):
        return "B"
    
    elif(hexDigit == 12):
        return "C"
    
    elif(hexDigit == 13):
        return "D"
    
    elif(hexDigit == 14):
        return "E"
    
    elif(hexDigit == 15):
        return "F"
    
    else:
        return "Z"

def getReminder(number):
    rem = int(number) % 16
    div = math.floor(int(number) / 16)
    return rem,div
    
    


def Multiply16(x,y):
    idx = 1
    myString = ""
    tid = (len(y)*2)-1
    TwoDarray = []
    res = [0 for i in range(len(y)*2)]
    for i in range(len(y)-1,-1,-1):
        arr = [0 for i in range(len(y)*2)]
        columns = (len(y)*2)-idx
        carry = 0
        j = 0
        for j in range(len(x)-1,-1,-1):
            num1 = int(ConverttoNumber(y[i]))
            num2 = int(ConverttoNumber(x[j]))
            sum = (num1 * num2) + int(carry)
            sum = str(sum)
            if(len(sum) == 2):
                
                num,carry = getReminder(sum)
                if(int(num) > 9 and int(num)<16):
                    num = ConverttoAlphabet(int(num))
                    arr[columns] = num
                else:
                   n,c = getReminder(num)
                   if(int(n)>9):
                       n = ConverttoAlphabet(int(n))
                   arr[columns] = n
                   arr[columns-1] = c
                   
            if(len(sum) == 3):
                
                num,carry = getReminder(sum)
                if(int(num) > 9 and int(num)<16):
                    num = ConverttoAlphabet(int(num))
                    arr[columns] = num
                else:
                   n,c = getReminder(num)
                   if(int(n)>9):
                       n = ConverttoAlphabet(int(n))
                   arr[columns] = n
                   arr[columns-1] = c
            
            
            else:
                carry = 0
                arr[columns] = sum
            columns = columns - 1
        i = i + 1
        idx = idx + 1
        TwoDarray.append(arr)
    
    print(TwoDarray)
    sum = 0
    carry_2 = 0
    for k in range(tid,0,-1):
        sum = 0
        for i in range(0,len(y)):
            s = (TwoDarray[i][k])
            s = int(ConverttoNumber(s))
            sum = int(sum) + s
        
        sum = int(sum) + int(carry_2)
        carry_2 = 0
    
        if(len(str(sum)) == 2):
            if(sum <= 15):
               sum =  ConverttoAlphabet(sum)
                
                
            else:
                
                sum = str(sum)
                carry_2 = sum[0]
                sum = sum[1]    
            
        res[k] = sum
    for i in range(0,len(res)):
        myString = myString + str(res[i])    

            
    
    return(myString)

answer = Multiply16("A11", "345")
print(answer)