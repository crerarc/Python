#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#  note_finder.py
# 
#  Copyright 2022 Crerar Christie <crerarc03@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>


# Form implementation generated from reading ui file 'note_finder5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


import note_finder_rc
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 166)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/1024px-Musical_note.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_string = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_string.setFont(font)
        self.label_string.setObjectName("label_string")
        self.gridLayout_2.addWidget(self.label_string, 0, 0, 1, 1)
        self.combBox_str1 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_str1.setObjectName("combBox_str1")
        self.gridLayout_2.addWidget(self.combBox_str1, 0, 1, 1, 1)
        self.combBox_str2 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_str2.setObjectName("combBox_str2")
        self.gridLayout_2.addWidget(self.combBox_str2, 0, 2, 1, 1)
        self.combBox_str3 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_str3.setObjectName("combBox_str3")
        self.gridLayout_2.addWidget(self.combBox_str3, 0, 3, 1, 1)
        self.combBox_str4 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_str4.setObjectName("combBox_str4")
        self.gridLayout_2.addWidget(self.combBox_str4, 0, 4, 1, 1)
        self.combBox_str5 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_str5.setObjectName("combBox_str5")
        self.gridLayout_2.addWidget(self.combBox_str5, 0, 5, 1, 1)
        self.combBox_str6 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_str6.setObjectName("combBox_str6")
        self.gridLayout_2.addWidget(self.combBox_str6, 0, 6, 1, 1)
        self.label_fret = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_fret.setFont(font)
        self.label_fret.setObjectName("label_fret")
        self.gridLayout_2.addWidget(self.label_fret, 1, 0, 1, 1)
        self.combBox_frt1 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_frt1.setObjectName("combBox_frt1")
        self.gridLayout_2.addWidget(self.combBox_frt1, 1, 1, 1, 1)
        self.combBox_frt2 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_frt2.setObjectName("combBox_frt2")
        self.gridLayout_2.addWidget(self.combBox_frt2, 1, 2, 1, 1)
        self.combBox_frt3 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_frt3.setObjectName("combBox_frt3")
        self.gridLayout_2.addWidget(self.combBox_frt3, 1, 3, 1, 1)
        self.combBox_frt4 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_frt4.setObjectName("combBox_frt4")
        self.gridLayout_2.addWidget(self.combBox_frt4, 1, 4, 1, 1)
        self.combBox_frt5 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_frt5.setObjectName("combBox_frt5")
        self.gridLayout_2.addWidget(self.combBox_frt5, 1, 5, 1, 1)
        self.combBox_frt6 = QtWidgets.QComboBox(self.centralwidget)
        self.combBox_frt6.setObjectName("combBox_frt6")
        self.gridLayout_2.addWidget(self.combBox_frt6, 1, 6, 1, 1)
        self.label_note = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_note.setFont(font)
        self.label_note.setObjectName("label_note")
        self.gridLayout_2.addWidget(self.label_note, 2, 0, 1, 1)
        self.label_note1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_note1.setFont(font)
        self.label_note1.setObjectName("label_note1")
        self.gridLayout_2.addWidget(self.label_note1, 2, 1, 1, 1)
        self.label_note2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_note2.setFont(font)
        self.label_note2.setObjectName("label_note2")
        self.gridLayout_2.addWidget(self.label_note2, 2, 2, 1, 1)
        self.label_note3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_note3.setFont(font)
        self.label_note3.setObjectName("label_note3")
        self.gridLayout_2.addWidget(self.label_note3, 2, 3, 1, 1)
        self.label_note4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_note4.setFont(font)
        self.label_note4.setObjectName("label_note4")
        self.gridLayout_2.addWidget(self.label_note4, 2, 4, 1, 1)
        self.label_note5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_note5.setFont(font)
        self.label_note5.setObjectName("label_note5")
        self.gridLayout_2.addWidget(self.label_note5, 2, 5, 1, 1)
        self.label_note6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_note6.setFont(font)
        self.label_note6.setObjectName("label_note6")
        self.gridLayout_2.addWidget(self.label_note6, 2, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)

        # Set Attributes
        self.label_note1.setStyleSheet("color: #0000ff")
        self.label_note2.setStyleSheet("color: #55aaff")
        self.label_note3.setStyleSheet("color: #55aa00")
        self.label_note4.setStyleSheet("color: #ffaa00")
        self.label_note5.setStyleSheet("color: #ff0000")
        self.label_note6.setStyleSheet("color: #550000")

        # Add strings to comb box
        string_list = [str(i) for i in range(1, 7)]
        self.combBox_str1.addItems(string_list)
        self.combBox_str2.addItems(string_list)
        self.combBox_str3.addItems(string_list)
        self.combBox_str4.addItems(string_list)
        self.combBox_str5.addItems(string_list)
        self.combBox_str6.addItems(string_list)

        # Add frets to comb box
        fret_list = [str(i) for i in range(0,25)]
        self.combBox_frt1.addItems(fret_list)
        self.combBox_frt2.addItems(fret_list)
        self.combBox_frt3.addItems(fret_list)
        self.combBox_frt4.addItems(fret_list)
        self.combBox_frt5.addItems(fret_list)
        self.combBox_frt6.addItems(fret_list)

   # Combo slots
        self.combBox_str1.activated[str].connect(self.find_note1)
        self.combBox_frt1.activated[str].connect(self.find_note1)
        self.combBox_str2.activated[str].connect(self.find_note2)
        self.combBox_frt2.activated[str].connect(self.find_note2)
        self.combBox_str3.activated[str].connect(self.find_note3)
        self.combBox_frt3.activated[str].connect(self.find_note3)
        self.combBox_str4.activated[str].connect(self.find_note4)
        self.combBox_frt4.activated[str].connect(self.find_note4)
        self.combBox_str5.activated[str].connect(self.find_note5)
        self.combBox_frt5.activated[str].connect(self.find_note5)
        self.combBox_str6.activated[str].connect(self.find_note6)
        self.combBox_frt6.activated[str].connect(self.find_note6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Combo box actions
    def find_note1(self):
        fret = int(self.combBox_frt1.currentText())
        strg = int(self.combBox_str1.currentText())
        self.label_note1.setText(str(noteid(fret, strg)))
    
    def find_note2(self):
        fret = int(self.combBox_frt2.currentText())
        strg = int(self.combBox_str2.currentText())
        self.label_note2.setText(str(noteid(fret, strg)))
    
    def find_note3(self):
        fret = int(self.combBox_frt3.currentText())
        strg = int(self.combBox_str3.currentText())
        self.label_note3.setText(str(noteid(fret, strg)))
    
    def find_note4(self):
        fret = int(self.combBox_frt4.currentText())
        strg = int(self.combBox_str4.currentText())
        self.label_note4.setText(str(noteid(fret, strg)))

    def find_note5(self):
        fret = int(self.combBox_frt5.currentText())
        strg = int(self.combBox_str5.currentText())
        self.label_note5.setText(str(noteid(fret, strg)))
    
    def find_note6(self):
        fret = int(self.combBox_frt6.currentText())
        strg = int(self.combBox_str6.currentText())
        self.label_note6.setText(str(noteid(fret, strg)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Note Finder"))
        self.label_string.setText(_translate("MainWindow", "String ->"))
        self.label_fret.setText(_translate("MainWindow", "Fret ->"))
        self.label_note.setText(_translate("MainWindow", "Note ->"))
        self.label_note1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">E 4</span></p></body></html>"))
        self.label_note2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#55aaff;\">E 4</span></p></body></html>"))
        self.label_note3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#55aa00;\">E 4</span></p></body></html>"))
        self.label_note4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffaa00;\">E 4</span></p></body></html>"))
        self.label_note5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">E 4</span></p></body></html>"))
        self.label_note6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#550000;\">E 4</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.triggered.connect(app.exit)


def noteid(fret: int, strng: int) -> str:
    """Returns note on string 'strng' at fret 'fret'

    Args:
        strng (str): Chosen string
        fret (int) : Chosen fret position

    Returns:
        (str): f string compound of note and octave
    """

    # Standard tuning, string-note: 1-E4 2-3 3-G3 4-D3 5-A2 6-E2
    # Take range to start at c2, and give it ordinal #1, etc
    tune_std = {1:28, 2:23, 3:19, 4:14, 5:9, 6:4}
    notes = {0:'C', 1:'C#', 2:'D', 3:'D#', 4:'E', 5:'F', 6:'F#', 7:'G', 8:'G#', 9:'A', 10:'A#', 11:'B'}
    octave = {0:2, 1:3, 2:4, 3:5, 4:6}
    this_note_index = tune_std[strng] + fret
    this_octave = octave[this_note_index // 12]
    this_note = notes[this_note_index % 12]

    return f"{this_note}{this_octave}"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

