import sys, mysql.connector, time

from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from PyQt5 import QtGui, QtCore
import threading
from db_auslesen import Ui_DatabaseOverview

class MainWindow (QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.ui = Ui_DatabaseOverview()
        self.ui.setupUi(self)

        #------------ My Code -----------#

        self.setWindowIcon(QtGui.QIcon('Images/RFID_Logo.png'))

        # Verbindung Datenbank
        try:
            print("Datenbankverbindung aufbauen...")
            connection = mysql.connector.connect \
                (host="***", user="***", passwd="***", db="***")
            global connection
            print("Verbindung hergestellt\n")
        except:
            print("Keine Verbindung möglich!\n")

        # Logo's
        self.ui.lblImgWareneingang.setPixmap(QtGui.QPixmap("Images/RFID_Logo_Wareneingang.png"))
        self.ui.lblImgLager.setPixmap(QtGui.QPixmap("Images/RFID_Logo_Lager.png"))
        self.ui.lblImgMontage.setPixmap(QtGui.QPixmap("Images/RFID_Logo_Montage.png"))
        self.ui.lblImgFertigteile.setPixmap(QtGui.QPixmap("Images/RFID_Logo_Fertigteil.png"))

        #------------ Tabellen ------------#
        horHeader = ['ID', 'Teil', 'RFID', 'Zeitstempel']
        self.ui.tblViewWareneingang.setColumnCount(4)
        self.ui.tblViewWareneingang.setRowCount(50)
        # Header Wareneingang
        self.ui.tblViewWareneingang.setHorizontalHeaderLabels(horHeader)
        self.ui.tblViewWareneingang.verticalHeader().setVisible(False)

        self.ui.tblViewLager.setColumnCount(4)
        self.ui.tblViewLager.setRowCount(50)
        # Header Lager
        self.ui.tblViewLager.setHorizontalHeaderLabels(horHeader)
        self.ui.tblViewLager.verticalHeader().setVisible(False)

        self.ui.tblViewMontage.setColumnCount(4)
        self.ui.tblViewMontage.setRowCount(50)
        # Header Montage
        self.ui.tblViewMontage.setHorizontalHeaderLabels(horHeader)
        self.ui.tblViewMontage.verticalHeader().setVisible(False)

        self.ui.tblViewFertiteile.setColumnCount(4)
        self.ui.tblViewFertiteile.setRowCount(50)
        # Header Fertigteile
        self.ui.tblViewFertiteile.setHorizontalHeaderLabels(horHeader)
        self.ui.tblViewFertiteile.verticalHeader().setVisible(False)

        for x in range(4):
            y = 295
            self.ui.tblViewWareneingang.setColumnWidth(x, y)
            self.ui.tblViewLager.setColumnWidth(x, y)
            self.ui.tblViewMontage.setColumnWidth(x, y)
            self.ui.tblViewFertiteile.setColumnWidth(x, y)

        # ------------ Button def ------------#
        self.ui.btnQuit.clicked.connect(self.close_programm)

        #------------ Threads starten ------------#
        t_w = threading.Thread(target=self.table_refresh)
        t_w.deamon = True
        t_w.start()



    def table_refresh(self):

        while True:

            # ------------ Wareneingang ------------ #
            # Cursor deffinieren
            cursor = connection.cursor()
            query = 'SELECT * FROM wareneingang'
            cursor.execute(query)

            # Einträge in Tabelle schreiben
            x = 0
            y = 0
            i = 1

            self.ui.tblViewWareneingang.clear()

            for row in cursor.fetchall():

                id = str(row[0])
                teil = str(row[1])
                rfid = str(row[2])
                timestamp = str(row[3])

                dictionaryTable = {id: [teil, rfid, timestamp]}

                for key, value in dictionaryTable.items():

                    self.ui.tblViewWareneingang.setItem(x, y, QTableWidgetItem(str(i)))
                    y += 1

                    self.ui.tblViewWareneingang.setItem(x, y, QTableWidgetItem(value[0]))
                    y += 1

                    self.ui.tblViewWareneingang.setItem(x, y, QTableWidgetItem(value[1]))
                    y += 1

                    self.ui.tblViewWareneingang.setItem(x, y, QTableWidgetItem(value[2]))
                    i += 1
                    y = 0
                    x += 1

            connection.commit()
            cursor.close()
            print("Fred Wareneingang")

            # ------------ Lager ------------ #
            # Cursor deffinieren
            cursor_lager = connection.cursor()
            query = 'SELECT * FROM lager'
            cursor_lager.execute(query)

            # Einträge in Tabelle schreiben
            x = 0
            y = 0
            i = 1

            self.ui.tblViewLager.clear()

            for row in cursor_lager.fetchall():

                id = str(row[0])
                teil = str(row[1])
                rfid = str(row[2])
                timestamp = str(row[3])

                dictionaryTable = {id: [teil, rfid, timestamp]}

                for key, value in dictionaryTable.items():
                    self.ui.tblViewLager.setItem(x, y, QTableWidgetItem(str(i)))
                    y += 1

                    self.ui.tblViewLager.setItem(x, y, QTableWidgetItem(value[0]))
                    y += 1

                    self.ui.tblViewLager.setItem(x, y, QTableWidgetItem(value[1]))
                    y += 1

                    self.ui.tblViewLager.setItem(x, y, QTableWidgetItem(value[2]))
                    i += 1
                    y = 0
                    x += 1

            connection.commit()
            cursor_lager.close()
            print("Fred Lager")

            # ------------ Montage ------------ #
            # Cursor deffinieren
            cursor_montage = connection.cursor()
            query = 'SELECT * FROM montage'
            cursor_montage.execute(query)

            # Einträge in Tabelle schreiben
            x = 0
            y = 0
            i = 1

            self.ui.tblViewMontage.clear()

            for row in cursor_montage.fetchall():

                id = str(row[0])
                teil = str(row[1])
                rfid = str(row[2])
                timestamp = str(row[3])

                dictionaryTable = {id: [teil, rfid, timestamp]}

                for key, value in dictionaryTable.items():
                    self.ui.tblViewMontage.setItem(x, y, QTableWidgetItem(str(i)))
                    y += 1

                    self.ui.tblViewMontage.setItem(x, y, QTableWidgetItem(value[0]))
                    y += 1

                    self.ui.tblViewMontage.setItem(x, y, QTableWidgetItem(value[1]))
                    y += 1

                    self.ui.tblViewMontage.setItem(x, y, QTableWidgetItem(value[2]))
                    i += 1
                    y = 0
                    x += 1

            connection.commit()
            cursor_montage.close()
            print("Fred Montage")

            # ------------ Fertigteile ------------ #
            # Cursor deffinieren
            cursor_fertigteile = connection.cursor()
            query = 'SELECT * FROM fertigteil'
            cursor_fertigteile.execute(query)

            # Einträge in Tabelle schreiben
            x = 0
            y = 0
            i = 1

            self.ui.tblViewFertiteile.clear()

            for row in cursor_fertigteile.fetchall():

                id = str(row[0])
                teil = str(row[1])
                rfid = str(row[2])
                timestamp = str(row[3])

                dictionaryTable = {id: [teil, rfid, timestamp]}

                for key, value in dictionaryTable.items():
                    self.ui.tblViewFertiteile.setItem(x, y, QTableWidgetItem(str(i)))
                    y += 1

                    self.ui.tblViewFertiteile.setItem(x, y, QTableWidgetItem(value[0]))
                    y += 1

                    self.ui.tblViewFertiteile.setItem(x, y, QTableWidgetItem(value[1]))
                    y += 1

                    self.ui.tblViewFertiteile.setItem(x, y, QTableWidgetItem(value[2]))
                    i += 1
                    y = 0
                    x += 1

            connection.commit()
            cursor_fertigteile.close()
            print("Fred Fertigteil")
            time.sleep(1)

    def close_programm(self):
        sys.exit(0)
