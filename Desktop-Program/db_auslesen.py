# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_logo_backup.ui'
#
# Created: Mon May  1 15:20:29 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DatabaseOverview(object):
    def setupUi(self, DatabaseOverview):
        DatabaseOverview.setObjectName("DatabaseOverview")
        DatabaseOverview.resize(1800, 900)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(DatabaseOverview)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(DatabaseOverview)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizLayTitles = QtWidgets.QHBoxLayout()
        self.horizLayTitles.setContentsMargins(-1, 25, -1, -1)
        self.horizLayTitles.setObjectName("horizLayTitles")
        self.horizLayWareneingang = QtWidgets.QHBoxLayout()
        self.horizLayWareneingang.setObjectName("horizLayWareneingang")
        self.lblImgWareneingang = QtWidgets.QLabel(DatabaseOverview)
        self.lblImgWareneingang.setText("")
        self.lblImgWareneingang.setObjectName("lblImgWareneingang")
        self.horizLayWareneingang.addWidget(self.lblImgWareneingang)
        self.lblWareneingang = QtWidgets.QLabel(DatabaseOverview)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblWareneingang.setFont(font)
        self.lblWareneingang.setObjectName("lblWareneingang")
        self.horizLayWareneingang.addWidget(self.lblWareneingang)
        spacerItem = QtWidgets.QSpacerItem(684, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizLayWareneingang.addItem(spacerItem)
        self.horizLayTitles.addLayout(self.horizLayWareneingang)
        self.horizLayLager = QtWidgets.QHBoxLayout()
        self.horizLayLager.setObjectName("horizLayLager")
        self.lblImgLager = QtWidgets.QLabel(DatabaseOverview)
        self.lblImgLager.setText("")
        self.lblImgLager.setObjectName("lblImgLager")
        self.horizLayLager.addWidget(self.lblImgLager)
        self.lblLager = QtWidgets.QLabel(DatabaseOverview)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblLager.setFont(font)
        self.lblLager.setObjectName("lblLager")
        self.horizLayLager.addWidget(self.lblLager)
        spacerItem1 = QtWidgets.QSpacerItem(770, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizLayLager.addItem(spacerItem1)
        self.horizLayTitles.addLayout(self.horizLayLager)
        self.verticalLayout_3.addLayout(self.horizLayTitles)
        self.horizLayTables = QtWidgets.QHBoxLayout()
        self.horizLayTables.setObjectName("horizLayTables")
        self.tblViewWareneingang = QtWidgets.QTableWidget(DatabaseOverview)
        self.tblViewWareneingang.setAutoFillBackground(False)
        self.tblViewWareneingang.setObjectName("tblViewWareneingang")
        self.tblViewWareneingang.setColumnCount(0)
        self.tblViewWareneingang.setRowCount(0)

        self.horizLayTables.addWidget(self.tblViewWareneingang)
        self.tblViewLager = QtWidgets.QTableWidget(DatabaseOverview)
        self.tblViewLager.setObjectName("tblViewLager")
        self.tblViewLager.setColumnCount(0)
        self.tblViewLager.setRowCount(0)
        self.horizLayTables.addWidget(self.tblViewLager)
        self.verticalLayout_3.addLayout(self.horizLayTables)
        self.horizLayTitles_2 = QtWidgets.QHBoxLayout()
        self.horizLayTitles_2.setContentsMargins(-1, 15, -1, -1)
        self.horizLayTitles_2.setObjectName("horizLayTitles_2")
        self.horizLayMontage = QtWidgets.QHBoxLayout()
        self.horizLayMontage.setObjectName("horizLayMontage")
        self.lblImgMontage = QtWidgets.QLabel(DatabaseOverview)
        self.lblImgMontage.setText("")
        self.lblImgMontage.setObjectName("lblImgMontage")
        self.horizLayMontage.addWidget(self.lblImgMontage)
        self.lblMontage = QtWidgets.QLabel(DatabaseOverview)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblMontage.setFont(font)
        self.lblMontage.setObjectName("lblMontage")
        self.horizLayMontage.addWidget(self.lblMontage)
        spacerItem2 = QtWidgets.QSpacerItem(740, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizLayMontage.addItem(spacerItem2)
        self.horizLayTitles_2.addLayout(self.horizLayMontage)
        self.horizLayFertigteile = QtWidgets.QHBoxLayout()
        self.horizLayFertigteile.setObjectName("horizLayFertigteile")
        self.lblImgFertigteile = QtWidgets.QLabel(DatabaseOverview)
        self.lblImgFertigteile.setText("")
        self.lblImgFertigteile.setObjectName("lblImgFertigteile")
        self.horizLayFertigteile.addWidget(self.lblImgFertigteile)
        self.lblFertigteile = QtWidgets.QLabel(DatabaseOverview)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblFertigteile.setFont(font)
        self.lblFertigteile.setObjectName("lblFertigteile")
        self.horizLayFertigteile.addWidget(self.lblFertigteile)
        spacerItem3 = QtWidgets.QSpacerItem(723, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizLayFertigteile.addItem(spacerItem3)
        self.horizLayTitles_2.addLayout(self.horizLayFertigteile)
        self.verticalLayout_3.addLayout(self.horizLayTitles_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tblViewMontage = QtWidgets.QTableWidget(DatabaseOverview)
        self.tblViewMontage.setObjectName("tblViewMontage")
        self.tblViewMontage.setColumnCount(0)
        self.tblViewMontage.setRowCount(0)
        self.horizontalLayout.addWidget(self.tblViewMontage)
        self.tblViewFertiteile = QtWidgets.QTableWidget(DatabaseOverview)
        self.tblViewFertiteile.setEnabled(True)
        self.tblViewFertiteile.setObjectName("tblViewFertiteile")
        self.tblViewFertiteile.setColumnCount(0)
        self.tblViewFertiteile.setRowCount(0)
        self.horizontalLayout.addWidget(self.tblViewFertiteile)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.btnQuit = QtWidgets.QPushButton(DatabaseOverview)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnQuit.setFont(font)
        self.btnQuit.setObjectName("btnQuit")
        self.verticalLayout_3.addWidget(self.btnQuit)

        self.retranslateUi(DatabaseOverview)
        QtCore.QMetaObject.connectSlotsByName(DatabaseOverview)

    def retranslateUi(self, DatabaseOverview):
        _translate = QtCore.QCoreApplication.translate
        DatabaseOverview.setWindowTitle(_translate("DatabaseOverview", "Database Overview"))
        self.label.setText(_translate("DatabaseOverview", "Teilebewegung"))
        self.lblWareneingang.setText(_translate("DatabaseOverview", "Wareneingang:"))
        self.lblLager.setText(_translate("DatabaseOverview", "Lager:"))
        self.tblViewWareneingang.setToolTip(_translate("DatabaseOverview", "wareneingang"))
        self.tblViewLager.setToolTip(_translate("DatabaseOverview", "lager"))
        self.lblMontage.setText(_translate("DatabaseOverview", "Montage:"))
        self.lblFertigteile.setText(_translate("DatabaseOverview", "Fertigteile:"))
        self.tblViewMontage.setToolTip(_translate("DatabaseOverview", "montage"))
        self.tblViewFertiteile.setToolTip(_translate("DatabaseOverview", "fertigteile"))
        self.btnQuit.setText(_translate("DatabaseOverview", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DatabaseOverview = QtWidgets.QWidget()
    ui = Ui_DatabaseOverview()
    ui.setupUi(DatabaseOverview)
    DatabaseOverview.show()
    sys.exit(app.exec_())

