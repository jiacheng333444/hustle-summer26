print("Hello World")

x = 6
if x > 5:
    print("X is greater than 5")

message = "hello, world"
print(message)

for i in range(5):
    print(i)

def greeting(name):
    return "Hello, world" + " " + name

print(greeting("Alice"))

# Snippet 1
x = 10
y = 2
result = x / y
print("Result:", result)
#Zero divison error 

# Snippet 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(numbers)):
    print(numbers[i - 1])
#Index Error

# Snippet 3
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))
# Syntax Error

# Snippet 4
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
# Syntax Error

# Snippet 5
for i in range(5):
    print(i)
# Syntax Error

# Snippet 6
def greet(name):
    return"Hello," + name
print(greet("Alice"))
#Syntax Error

# Snipptet 7
numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number
    print("Sum of numbers:", total)
#Indentation Error

# Snippet 8
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(0))
#program never stops

# Snippet 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")
#Syntax Error

# Snippet 10
num1 = 10
num2 = 0
def divide_numbers(x, y):
    result = x / y
    return result
if num2 != 0:
    print(divide_numbers(num1, num2))
else:
    print("Can Not Divide By Zero!")
#zero division error    