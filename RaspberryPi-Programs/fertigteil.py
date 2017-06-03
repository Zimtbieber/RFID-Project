from function import *
import sys


connection = database_con()

print("\n" + "*" * 50)
print("*                     Fertigteil                      *")
print("*" * 50 + "\n")

ka = ""
re = ""
sc = ""
si = ""
le = ""

print("Warte auf Transponder...")

def ein_ausbuchen():
    # Karrosserie
    query = 'DELETE FROM montage WHERE rfid="' + id_ka + '"'
    cursor.execute(query)
    connection.commit()

    # Reifen
    query = 'DELETE FROM montage WHERE rfid="' + id_re + '"'
    cursor.execute(query)
    connection.commit()

    # Schrauben
    query = 'DELETE FROM montage WHERE rfid="' + id_sc + '"'
    print(query)
    cursor.execute(query)
    connection.commit()

    # Sitz
    query = 'DELETE FROM montage WHERE rfid="' + id_si + '"'
    cursor.execute(query)
    connection.commit()

    # Lenkrad
    query = 'DELETE FROM montage WHERE rfid="' + id_le + '"'
    cursor.execute(query)
    connection.commit()



    query = 'INSERT INTO fertigteil (teil, rfid, timestamp) ' + 'VALUES ("' + "Auto fertig" + '", "' + id + '", NOW())'
    cursor.execute(query)
    connection.commit()

while True:
    try:
        id = str(read_rfid())
        id = id.replace("'", "")
        id = id.replace("b", "")

        cursor = connection.cursor()
        query = "SELECT * FROM montage WHERE rfid='" + id + "'"
        cursor.execute(query)

        rfid = ""

        for row in cursor.fetchall():
            teil = str(row[1])
            rfid = str(row[2])

        if teil == "Karrosserie":
            ka = "Karrosserie"
            id_ka = rfid
        if teil == "Reifen":
            re = "Reifen"
            id_re = rfid
        if teil == "Schrauben":
            sc = "Schrauben"
            id_sc = rfid
        if teil == "Sitze":
            si = "Sitz"
            id_si = rfid
        if teil == "Lenkrad":
            le = "Lenkrad"
            id_le = rfid

        if ka != "" and re != "" and sc != "" and si != "" and le != "":

            ein_ausbuchen()

            ka = ""
            re = ""
            sc = ""
            si = ""
            le = ""

        else:
            pass

        print("\nKarrosserie:\t" + ka + "\nReifen:\t\t" + re + "\nSchrauben:\t" + sc +
              "\nSitze:\t\t" + si + "\nLenkrad:\t" + le)

    except (KeyboardInterrupt):
        sys.exit(0)


