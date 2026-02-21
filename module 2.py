# task2.1

user_name = input("Enter your name: ")
print("Hello " + user_name + "!")



# task2.2

r = float(input("Enter the radius: "))
circle_area = 3.14 * (r ** 2)
print("Area of the circle is:", circle_area)



# task2.3

length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

rect_area = length * width
rect_perimeter = 2 * length + 2 * width

print("Rectangle area:", rect_area)
print("Rectangle perimeter:", rect_perimeter)



# task2.4

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

total = a + b + c
product = a * b * c
average = total / 3

print("Sum:", total)
print("Product:", product)
print("Average:", average)



# task2.5

talent = float(input("Enter talents: "))
pound = float(input("Enter pounds: "))
lot = float(input("Enter lots: "))

lots_total = talent * 20 * 32 + pound * 32 + lot
grams_total = lots_total * 13.3

kg = int(grams_total // 1000)
g = grams_total % 1000

print("Weight in modern units:")
print("Kilograms:", kg)
print("Grams:", g)



# task2.6

import random

# 3-digit code (0–9)
code3 = ""
for i in range(3):
    code3 += str(random.randint(0, 9))

# 4-digit code (1–6)
code4 = ""
for i in range(4):
    code4 += str(random.randint(1, 6))

print("3-digit code:", code3)
print("4-digit code:", code4)