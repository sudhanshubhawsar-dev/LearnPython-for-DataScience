age = input("enter your age:")
print(type(age)) 
#By default, the input() function returns a string. To convert it to another type like int or float, you need to explicitly cast it.
age = int(input("Enter your age: "))
print(f"You are {age} years old.")
print(type(age)) 

name = "Sudhanshu"
age = 28
print(f"Hello, my name is {name} and I am {age} years old.")
print("Hello, my name is {} and I am {} years old.".format(name,age))
