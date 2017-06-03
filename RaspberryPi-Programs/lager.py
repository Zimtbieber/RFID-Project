from function import *
import sys, time


connection = database_con()

print("\n" + "*" * 50)
print("*                     Lager                      *")
print("*" * 50 + "\n")

while True:

    try:

        print("Warte auf Transponder...\n")

        id = str(read_rfid())
        id = id.replace("'", "")
        id = id.replace("b", "")

        cursor = connection.cursor()
        query = "SELECT * FROM wareneingang WHERE rfid='" + id + "'"
        cursor.execute(query)

        rfid = ""

        for row in cursor.fetchall():
            teil = str(row[1])
            rfid = str(row[2])

        if rfid == id:
            query = 'DELETE FROM wareneingang WHERE rfid="' + id + '"'
            cursor.execute(query)
            connection.commit()

            query = 'INSERT INTO lager (teil, rfid, timestamp) ' + 'VALUES ("' + teil + '", "' + id + '", NOW())'
            cursor.execute(query)
            connection.commit()
            time.sleep(0.3)

        else:
            pass

    except (KeyboardInterrupt):
        sys.exit(0)
