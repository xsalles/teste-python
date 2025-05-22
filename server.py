import mysql.connector
from datetime import datetime
from informations import get_system_info

data = get_system_info()

try:
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="absolute"
    )
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)



cursor = db.cursor()

sql = """
   INSERT INTO dispositivos (
        hostname, 
        serie_number, 
        equipament_name,
        ram_memory,
        os, 
        os_version, 
        disk, 
        model,
        manufacturer, 
        location
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

values = (
    data["hostname"],
    data["serie_number"],
    data["equipament_name"],
    data["ram_memory"],
    data["os"],
    data["os_version"],
    data["disk"],
    data["model"],
    data["manufacturer"],
    data["location"]
)

print("Inserting data into the database...")

try:
    cursor.execute(sql, values)
    db.commit()
    print("Data inserted successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")

cursor.close()
db.close()