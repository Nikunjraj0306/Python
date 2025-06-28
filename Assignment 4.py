#TASK: 1
try:
    file_name="Sample.txt"
    with open(file_name,"r") as file1:
        print(file1.read())
    file1.close()
except FileNotFoundError:
    print("Error: The file",file_name,"was not found.")
finally:
    print("Thank You")

#TASK: 2
thing=input(str("Enter text to write to the file: "))
x="output.txt"
file2=open( x ,"w")
y=file2.write("\n" + thing)
print("Data Successfully written to output.txt.\n")
file2.close

file2= open("output.txt","a")
additional_input=input(str("Enter additional text to append: "))
appended_text=file2.write('\n'+ additional_input)
print("Data successfully appended.\n")
file2.close

file2=open("output.txt","r")
print("Final content of output.txt:",file2.read())
file2.close
