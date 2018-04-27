#!/usr/bin/python3

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mainWindow import MainWindow

def main():
    app = QtWidgets.QApplication (sys.argv)
    m = MainWindow ()
    m.show ()
    sys.exit (app.exec_ () )

if __name__ == '__main__':
    main ()
