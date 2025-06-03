import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def insert_into_db(data):
    try:
        connection = mysql.connector.connect(
            host = os.getenv('DB_HOST'),
            user= os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            port =int(os.getenv('DB_PORT'))
        )
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS device_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                manufacturer TEXT NOT NULL,
                model TEXT NOT NULL,
                os_version TEXT NOT NULL,
                apps LONGTEXT NOT NULL,
                network TEXT NOT NULL,
                storage TEXT NOT NULL,
                users TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT INTO device_data
            (manufacturer, model, os_version, apps, network, storage, users, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            data["manufacturer"],
            data["model"],
            data["os_version"],
            data["apps"],
            data["network"],
            data["storage"],
            data["users"],
            data["timestamp"]
        ))
        connection.commit()
        cursor.close()
        connection.close()
        print("Data inserted successfully")
    except Exception as e:
        print(f"DB error: {e}")


