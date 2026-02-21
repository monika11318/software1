# TASK 1
import random

def roll_dice():
    return random.randint(1, 6)

print("Task 1:")
number = roll_dice()

while True:
    print(number)
    if number == 6:
        break
    number = roll_dice()



# TASK 2
def roll_dice_with_sides(max_sides):
    return random.randint(1, max_sides)

print("\nTask 2:")
sides = int(input("How many sides does the dice have? "))

result = roll_dice_with_sides(sides)

while True:
    print(result)
    if result == sides:
        break
    result = roll_dice_with_sides(sides)



# TASK 3
def gallons_to_litres(gallons):
    return gallons * 3.78541

print("\nTask 3:")
amount = float(input("Enter gallons (negative number to stop): "))

while amount >= 0:
    litres = gallons_to_litres(amount)
    print("Litres:", litres)
    amount = float(input("Enter gallons (negative number to stop): "))



# TASK 4
def sum_of_list(numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print("\nTask 4:")
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_of_list(my_numbers))



# TASK 5
def even_numbers_only(values):
    even_nums = []
    for v in values:
        if v % 2 == 0:
            even_nums.append(v)
    return even_nums

print("\nTask 5:")
original_list = [1,2,3,4,5,6,7,8,9,10]
new_list = even_numbers_only(original_list)

print("Original:", original_list)
print("Even numbers:", new_list)



# TASK 6
def pizza_price_per_m2(diameter_cm, price):
    radius = diameter_cm / 2
    area_cm2 = 3.14 * radius * radius
    area_m2 = area_cm2 / 10000
    return price / area_m2

print("\nTask 6:")
diameter1 = float(input("Diameter of first pizza (cm): "))
price1 = float(input("Price of first pizza (€): "))

diameter2 = float(input("Diameter of second pizza (cm): "))
price2 = float(input("Price of second pizza (€): "))

price_value1 = pizza_price_per_m2(diameter1, price1)
price_value2 = pizza_price_per_m2(diameter2, price2)

if price_value1 < price_value2:
    print("First pizza is cheaper per square meter")
else:
    print("Second pizza is cheaper per square meter")