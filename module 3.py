# TASK 3.1

fish_length = float(input("Enter zander length in cm: "))

if fish_length >= 42:
    print("The zander is large enough.")
else:
    missing = 42 - fish_length
    print("Put the fish back into the lake.")
    print("It is", missing, "cm under the minimum size.")


# TASK 3.2

cabin = input("Enter cabin class (lux, A, B, C): ").lower()

if cabin == "lux":
    print("Luxury upper-deck cabin with a balcony.")
elif cabin == "a":
    print("A-class cabin above car deck with a window.")
elif cabin == "b":
    print("B-class cabin above car deck without a window.")
elif cabin == "c":
    print("C-class cabin above car deck without a window.")
else:
    print("Invalid cabin class entered.")


# TASK 3.3

gender = input("Enter biological gender (male/female): ").lower()
hb = float(input("Enter hemoglobin value (g/l): "))

if gender == "male":
    if hb < 134:
        print("Hemoglobin value is low.")
    elif 134 <= hb <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")

elif gender == "female":
    if hb < 117:
        print("Hemoglobin value is low.")
    elif 117 <= hb <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender input.")


# TASK 3.4

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")