name = input("enter your name: ")
print("Hello, " + name + "!")
#dynamic software , we use input() function to take input from user and store it in a variable.
#user input is always stored as a string, so if we want to take input as an integer or float, we need to convert it using int() or float() functions.
#string is universal format for data type in python, so we can take input as string and convert it to other data types if needed.

#type conversion is the process of converting one data type to another data type.
#implicit type conversion is done by python automatically, 
num1 = 4+9.5
print(num1)
num2 = 4.5 + 4+7j
print(num2)

#while explicit type conversion is done by the user using built-in functions 
#like int(), float(), str(), etc.
print(int("10"))
print(float(10))
print(str(10))
print(bool(1))
print(complex(1))
print(list(('hello')))

#type conversion is not permanent, it only changes the data type of the variable for that particular operation, the original data type of the variable remains unchanged.

first_num = int(input("enter first number: "))
second_num = int(input("enter second number: "))
print(first_num + second_num)