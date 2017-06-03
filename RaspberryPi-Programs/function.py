import sys, serial
import serial, mysql.connector

def read_rfid():
   ser = serial.Serial("/dev/ttyAMA0")
   ser.baudrate = 9600
   daten = ser.read(14)
   ser.close()
   daten = daten.replace(b'\x02', b'')
   daten = daten.replace(b'\x03', b'')
   return daten

def database_con():
   try:
      textVerbindung = ("Datenbankverbindung aufbauen...")
      print(textVerbindung)
      connection = mysql.connector.connect \
         (host="***.***.***.***", user="***", passwd="***", db="***")
      print("Verbindung wurde erfolgreich hergestellt!\n")
      return connection
   except:
      fehler = "Keine Verbindung zur Datenbank möglich."
      return fehler
      sys.exit(0)
