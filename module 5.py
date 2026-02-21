#1
import random

enter_dice = int(input("Enter the number of dice to roll: "))
sum_dice = 0

for i in range(0, enter_dice):
    dice_rolls = random.randint(1,6)
    sum_dice = sum_dice + dice_rolls

print(sum_dice)

#2
for_numbers = []
enter_numbers = str(input("Enter the numbers (empty to stop): "))

while enter_numbers != '':
    for_numbers.append(int(enter_numbers))
    enter_numbers = input("Enter the numbers (empty to stop): ")
for_numbers.sort(reverse=True)
print(for_numbers[0:5])

#3
ask_number = int(input("Enter the number: "))

if ask_number <= 1:
    print("The number is not a prime number")
else:
    for i in range(2, ask_number):
        if ask_number % i == 0:
            break
    else:
        print("The number is  a prime number")

#4
cities = []
for i in range(5):
    which_cities = input('Enter five cities: ')
    cities.append(which_cities)

for city in cities:
    print(city)