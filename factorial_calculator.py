def factorialFunc(n): #operations on input function
    result = 1
    while n != 0:
        result = result * n
        n = n-1
    return result

num = input("Insert a positive integer number: ") #getting input
num= int(num)

operation = factorialFunc(num) #function calling
print("The chosen number's factorial is : ",operation)
