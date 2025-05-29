#TASK 1:
print("To find out if a no. is even or odd\n")
a=int(input("Enter a number: "))
if a%2==0:
    print(a, "is an even number.\n\n")
else:
    print(a, "is an odd number.\n\n")


#Task 2:
print("To find sum of all integers in a range\n")
x= int(input("Enter starting number of range: "))
y= int(input("Enter ending number of range: "))
total=0
sum=range(x,y+1)
if x<y:
    for i in sum:
     total+=i
    print("The sum of numbers from",x,"to",y,"is:",total)
else:
    print("\nRange should be in increasing order.")
