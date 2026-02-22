import mysql.connector
from geopy.distance import geodesic


# ---------------- TASK 1 ----------------
print("Task 1 - Get airport name and municipality")

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="moni2061"
)

cursor = connection.cursor()

icao_code = input("Enter ICAO code: ")

sql1 = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(sql1, (icao_code,))
result = cursor.fetchone()

if result:
    name, municipality = result
    print(f"Airport name: {name}")
    print(f"Municipality: {municipality}")
else:
    print("Airport not found in database.")

cursor.close()
connection.close()



# ---------------- TASK 2 ----------------
print("\nTask 2 - Airport types by country")

connection2 = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="moni2061"
)

cursor2 = connection2.cursor()

iso_code = input("Give ISO country code: ")

sql2 = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country = %s
GROUP BY type
ORDER BY type
"""

cursor2.execute(sql2, (iso_code,))
results = cursor2.fetchall()

if results:
    for a_type, total in results:
        print(a_type, ":", total)
else:
    print("No airports found for this country.")

cursor2.close()
connection2.close()



# ---------------- TASK 3 ----------------
print("\nTask 3 - Distance between two airports")

connection3 = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="moni2061"
)

cursor3 = connection3.cursor()

icao1 = input("Enter first ICAO code: ")
icao2 = input("Enter second ICAO code: ")

sql3 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

cursor3.execute(sql3, (icao1,))
coords1 = cursor3.fetchone()

cursor3.execute(sql3, (icao2,))
coords2 = cursor3.fetchone()

if coords1 is not None and coords2 is not None:
    location1 = (coords1[0], coords1[1])
    location2 = (coords2[0], coords2[1])

    distance_km = geodesic(location1, location2).kilometers
    print(f"Distance: {round(distance_km, 2)} km")
else:
    print("Could not calculate distance (airport missing).")

cursor3.close()
connection3.close()