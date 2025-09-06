def fibonacci_number(n): #defining a function
    a = 0
    b = 1 #as fibonacci no. starts with 0 

    print(a) #printing the a and  b directly because if n is 0 or 1,output will be 0 and 1 respectively
    print(b)

    for i in range(2,n): #looping from 2 to n because 0 and 1 are already printed
        c = a + b #adding the previous two numbers to get the next number
        print(c)
        a = b #updating the values of a and b so the result wont be same in next iteration
        b = c
fibonacci_number(20) #calling the function for output 
 #YEAHHHOOO