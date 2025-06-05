#TASK 1:
num1=int(input("Enter a number: "))
def factorial(x):
    if x<2:
        return 1
    else:
        return x*factorial(x-1)
print("Factorial of",num1,"is:",factorial(num1))

#TASK 2:
import math
num1=int(input("\n\nEnter a number: "))
squareroot=math.sqrt(num1)
print("Square root:",squareroot)
natural_logarithm=math.log(num1)
print("Logarithm:",natural_logarithm)
sine_number=math.sin(num1)
print("Sine:",sine_number)