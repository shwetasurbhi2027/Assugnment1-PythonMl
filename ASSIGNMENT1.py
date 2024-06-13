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

#11. Write a python program that generates the first n numbers in the Fibonacci sequence.
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = [0, 1]
for i in range(2, n):
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)
print("The first", n, "Fibonacci numbers are:", fibonacci_sequence[:n])

#12. Write a python program that calculates the sum of the digits of a given number
number_sum = input("Enter a number: ")
total = 0
for digit in number_sum:
    if digit.isdigit():
        total += int(digit)
print("The sum of the digits of the number is:", total)

#13. Write a program that asks the user for their birth year and calculates their  age.
birth_year=int(input("enter your birth year:"))
age=2024-birth_year
print(age)

#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
lines = ""
print("Enter multiple lines of input. Press Enter on an empty line to finish.")

while True:
    line = input()
    if line == "":
        break
    lines += line + "\n"
print(lines)

#15. Write a program that reads data from a CSV file and prints it to the console.
import csv
file_name = "data.csv"
with open(file_name, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
#16. Write a program in python that counts the frequency of each character in a string.
str = "hello everyone"
character_freq = {}
for char in str:
    if char in character_freq:
        character_freq[char] +=1
    else:
        character_freq[char] = 1
for char, freq in character_freq.items():
    print(f"Character '{char}' appears {freq} times.")

#17. Write a program in python that converts a given string to title case (first letter of each word capitalized).
state=input()
print(state.title())

#18. Write a python program that checks if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
word1 = "listen"
word2 = "silent"
if are_anagrams(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams.")
else:
    print(f"'{word1}' and '{word2}' are not anagrams.")
    
#19. Write a python program that removes all punctuation from a given string
punc_string = "Hello, everyone! How are you doing"
import string 
without_punc_string = ""
for char in punc_string:
    if char not in string.punctuation:  
        without_punc_string += char
print(without_punc_string)

#20. Write a python program that takes a list of numbers and returns their sum
list1 =[1,2,3,4,5]
sum = 0
for i in list1:
    sum += i
print(sum)

# QUESTION 21 : Write a python program that counts the occurrences of a specific element
def count_occurrences(list1, element):
    count = 0
    for i in list1:
        if i == element:
            count += 1
    return count
numbers = [10,20,30,40,10,20,100,10]
element = 10
occ = count_occurrences(numbers, element)
print(f"The element {element} occurs {occ} times in the list.")


#22. Write a python program that returns the minimum and maximum values in a list of numbers
list1 = [-1,4,2,10,72,34]
print("minimum value in list:", min(list1) , "maximum value in list:", max(list1))


#23. Write a program that converts the temperature from Celsius to Fahrenheit and vice versa based on user input
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter your choice (1 or 2): ")
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit:.2f}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius:.2f}°C")
else:
    print("Invalid choice")


#24. Write a program that acts as a simple calculator. It should take two numbers and an operator(+,-,*,/) as input and print the result
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
print("1. + \n2. - \n3. * \n4. /")
choice = input("which operation do you want to perform (1-4) ")
if choice == '1':
    print(num1+num2)
elif choice == '2':
    print(num1-num2)
elif choice == '3':
    print(num1*num2)
elif choice == '4':
    if num2 == 0:
        print("please give valid denominator")
    else:
        print(num1/num2)
else:
    print("choose valid operation")


#25. Write a program that copies the contents of one text file to another
with open("demo.txt", "r") as source_file:
    content = source_file.read()
with open("demo.txt", "w") as destination_file:
    destination_file.write(content)
print("Contents of 'demo.txt' have been copied to 'demo.txt'.")


#26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix
str="hello eveyone, what's up"
prefix = "hello"
print(str.startswith(prefix))
print(str.endswith('ace'))


#27. Write a program in python that converts a string into a list of its characters
str1 = "hello"
char_list = list(str1)
print(char_list)








