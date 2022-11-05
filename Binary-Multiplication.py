def Multiply2(x,y):
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
            sum = int(y[i]) * int(x[j]) + int(carry)
            sum = str(sum)
            if(len(sum) == 2):
            
                carry = sum[0]
                sum = sum[1]
                arr[columns] = sum
            else:
                carry = 0
                arr[columns] = sum
            columns = columns - 1
        i = i + 1
        idx = idx + 1
        TwoDarray.append(arr)

    sum = 0
    carry_2 = 0
    for k in range(tid,0,-1):
        sum = 0
        for i in range(0,len(y)):
            s = int(TwoDarray[i][k])
            sum = int(sum) + s
        if(carry_2==2):
            
            sum = int(sum)
            carry_2 = 1
            
        else:
            sum = int(sum) + int(carry_2)
            carry_2 = 0
            
    
        if(sum == 2):
            sum = str(sum)
            carry_2 = 1
            sum = 0    
        
        if(sum == 3):
            sum = str(sum)
            carry_2 = 1
            sum = 1 
        
        if(sum == 4):
            sum = str(sum)
            carry_2 = 2
            sum = 0
            
        res[k] = sum
    for i in range(0,len(res)):
        myString = myString + str(res[i])    

            
    
    return(myString)




answer = Multiply2("101", "101")
print(answer)