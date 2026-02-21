#task4.1
number = 1
while number <= 1000:
    if number % 3 == 0:
      print(number)
    number = number + 1


#task4.2
while True:
    inches = float(input("enter inches (negative value to quite): "))
    if inches < 0:
        break
cm = inches * 2.54
print(f"{inches} inches is {cm} centimeters.")



#task4.3
smallest = None
largest = None

while True:
    user_input = input("enter a number (empty string to quite): ")
    if user_input == "":
        break
    num = float(user_input)
    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num
    if smallest is not None:
        print(f"smallest number: {smallest}")
        print(f"largest number: {largest}")



#task4.4
import random

target = random.randint(1, 10)
guess = None

print("i'm thinking of a number from 1 to 10.")
while guess != target:
    guess = int(input("your guess: "))
    if guess < target:
        print("too low")
    elif guess > target:
        print("too high")
    else:
        print("correct")



#task4.5
attempts = 0
while attempts < 5:
    user = input("username: ")
    password = input("password: ")
    if user == "python" and password == "rules":
        print("welcome")
        break
    else:
        attempts += 1
        if attempts < 5:
            print("incorrect. you have {5-attempts} attempts left.")
        if attempts == 5:
            print("access denied")


#task4.6
import random

total_points = int(input("how many random points to generate? "))
n = 0
Iterator = 0
while Iterator < total_points:
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    if x * 2 + y * 2 < 1:
        n += 1
    Iterator += 1
pi_approx = 4 * n / total_points
print(f"the approximation of pi using {total_points} points is: {pi_approx}")