import mysql.connector

conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
)

cursor = conn.cursor()

cursor.execute(
    "CREATE DATABASE IF NOT EXISTS studentdb" 
)
cursor.execute("USE studentdb")
print("database create")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stud(

    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    mobile VARCHAR(100),
    email VARCHAR(100)
    )
    """
)
print("table create successfully.")

insert_query = "INSERT INTO stud (firstname, lastname, mobile, email) VALUES (%s, %s, %s, %s)"
Val = ("radhika", "sonagara", "1234567890", "radhika@example.com")
cursor.execute(insert_query, Val)

conn.commit()
print("record inserted ")

cursor.execute("SELECT * FROM stud")

rows = cursor.fetchall()

for row in rows:
    print(row)

update_query = "UPDATE stud SET firstname = %s WHERE id = %s"
Val= ("Radhika_updated", 1)
cursor.execute(update_query, Val)

conn.commit()
print("record updated ")


cursor.execute("SELECT * FROM stud")

rows = cursor.fetchall()

for row in rows:
    print(row)

    



