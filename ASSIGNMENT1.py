#1. Write a program that takes two numbers as input and prints their sum.
a=int(input("enter first number:"))
b=int(input("enter second number:"))
sum=int(a+b)
print(sum)

#2. Write a python program that checks whether a given number is even or odd.
number=int(input("enter a number:"))
if number%2==0:
    print("even number")

else:
    print("odd number")
    
#3. Write a python program that calculates the factorial of a given number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}.")

#4. Write a program that asks the user for their name and then prints a greeting message.
name=input("enter name:")
print(f"hello {name}, welcome")

#5. Write a program that takes a string input from the user and writes it to a text file.
user_input = input("Enter a string: ")
file_name = "demo.txt"
with open(file_name, "w") as file:
    file.write(user_input)

print(f"The string has been written to {file_name}.")

#6. Write a program that reads the content of a text file and prints it to the console.
file_name = "demo.txt"
with open(file_name, "r") as file:
    content = file.read()
    print(content)
    
#7. Write a python program that takes a string as input and returns its length.
str=input("enter a string:")
print(len(str))

#8. Write a python program that concatenates two strings and returns the result.
str1=input("enter str1:")
str2=input("enter str2:")
print(str1+str2)

#9. Write a python program that checks if a substring is present in a given string.
main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")
if substring in main_string:
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")

#10. Write a python program that converts a given string to uppercase.
statement=input("enter a statement:")
upper_statement=statement.upper
print(upper_statement)





