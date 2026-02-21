# -------- TASK 1: Season Finder --------

print("Task 1 - Season Finder")

seasons = ("spring", "summer", "autumn", "winter")

month = int(input("Give month number (1-12): "))

if 1 <= month <= 12:

    if month in [12, 1, 2]:
        season = seasons[3]

    elif month in [3, 4, 5]:
        season = seasons[0]

    elif month in [6, 7, 8]:
        season = seasons[1]

    else:
        season = seasons[2]

    print("Season is:", season)

else:
    print("Invalid month number")


# -------- TASK 2: Name Checker --------

print("\nTask 2 - Name Checker")

names = set()

while True:
    name = input("Type a name (press Enter to quit): ")

    if not name:
        break

    if name in names:
        print("This name is already in the list")
    else:
        names.add(name)
        print("Name successfully added")

print("\nNames entered:")
for n in names:
    print("-", n)


# -------- TASK 3: Airport Database --------

print("\nTask 3 - Airport Database")

airports = {}

while True:
    choice = input("Select option (add/search/exit): ").lower()

    if choice == "add":
        icao = input("ICAO code: ")
        name = input("Airport name: ")
        airports[icao] = name
        print("Airport added successfully.")

    elif choice == "search":
        icao = input("Enter ICAO code to search: ")
        result = airports.get(icao)

        if result:
            print("Airport found:", result)
        else:
            print("Airport not found.")

    elif choice == "exit":
        print("Exiting program...")
        break

    else:
        print("Please choose a valid option.")