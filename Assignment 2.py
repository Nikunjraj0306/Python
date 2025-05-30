#TASK 1:
print("To find out if a no. is even or odd\n")
a=int(input("Enter a number: "))
if a%2==0:
    print(a, "is an even number.\n\n")
else:
    print(a, "is an odd number.\n\n")


#Task 2:
total=0
sum=range(1,51)
for i in sum:
    total+=i
print("The sum of numbers from 1 to 50 is:",total)