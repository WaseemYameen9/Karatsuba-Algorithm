def Multiply_string(a,b):
    idx = 1
    myString = ""
    tid = (len(b)*2)-1
    TwoDarray = []
    res = [0 for i in range(len(b)*2)]
    for i in range(len(b)-1,-1,-1):
        arr = [0 for i in range(len(b)*2)]
        columns = (len(b)*2)-idx
        carry = 0
        j = 0
        for j in range(len(a)-1,-1,-1):
            sum = int(b[i]) * int(a[j]) + int(carry)
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
        for i in range(0,len(b)):
            s = int(TwoDarray[i][k])
            sum = int(sum) + s
        
        sum = int(sum) + int(carry_2)
        carry_2 = 0
    
        if(len(str(sum)) == 2):
            sum = str(sum)
            carry_2 = sum[0]
            sum = sum[1]    
            
        res[k] = sum
    for i in range(0,len(res)):
        myString = myString + str(res[i])    

            
    
    return(myString)

s = Multiply_string("123","456")
print(s)