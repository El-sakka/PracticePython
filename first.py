# Practice
# 1- Write a program to prompt a user to enter his name, age and print these information on
# the console

# name = input("Enter your Name : ")
# age = int(input("Enter your Age : "))
# print("your name is "+name +"\nYour age is "+str(age))

# Write a program to prompt a user to enter 2 numbers and print the values of adding,
# subtracting, multiplying and dividing these 2 numbers

# x = int(input("Enter first Number "))
# y = int(input("Enter second Number "))
# print("adding : ")
# print(x+y)
# print("subtracting : ")
# print(x-y)
# print("Multiplying : ")
# print(x*y)
# print("dividing : ")
# print(x/y)

# Write a program to prompt a user to enter 3 numbers and print the greatest number of
# these 3 numbers
# x = int(input())
# y = int(input())
# z = int(input())
# print(max(x,max(y,z)))

# Write a program to prompt a user to enter a number and print the binary
# representation of this number (each digit in a separate line)

# n = int(input("enter your number "))
# result = 0 
# mul = 1 
# while(n>0):
#     result = result + ((n%2) * mul)
#     mul = mul * 10
#     n = n/2
# print(result)

# n = int(input("enter number "))
# result = 0
# mul = 1

# while n > 0 :
#     x = n%2
#     y = x*mul
#     result = result + y
#     mul = mul * 10
#     n = n/2
# print(result)

# Write a program to prompt a user to enter 2 numbers and print the GCD (greatest
# common divisor) of these 2 number (using the subtraction Euclidean method)

x = int(input("enter first number "))
y = int(input("enter second numebr "))

m = min(x,y)
while m >= 1:
    if x%m==0 and y%m==0:
        break
    m = m -1
print(m)