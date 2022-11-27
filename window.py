# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1301, 920)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Theico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(560, 20, 711, 861))
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(540, 20, 20, 861))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(60, 100, 451, 591))
        self.listView.setStyleSheet("")
        self.listView.setObjectName("listView")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(80, 120, 411, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 30, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(100, 30, 211, 21))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton.setGeometry(QtCore.QRect(330, 30, 47, 21))
        self.toolButton.setObjectName("toolButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(80, 190, 411, 431))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 111, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton.setGeometry(QtCore.QRect(110, 89, 41, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 90, 41, 19))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_3.setGeometry(QtCore.QRect(250, 90, 41, 19))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_4.setGeometry(QtCore.QRect(320, 90, 41, 19))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(1, 140, 111, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(191, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(1, 190, 91, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(191, 191, 91, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(20, 240, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(191, 240, 91, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(20, 290, 72, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(191, 290, 101, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(0, 340, 111, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(190, 340, 101, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(0, 390, 111, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(201, 390, 81, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 290, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 340, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(110, 390, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(290, 240, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(290, 290, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(290, 340, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(290, 390, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(290, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(110, 240, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_14.setGeometry(QtCore.QRect(110, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(60, 710, 451, 131))
        self.listView_2.setObjectName("listView_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(580, 30, 681, 841))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listView_4 = QtWidgets.QListView(self.tab)
        self.listView_4.setGeometry(QtCore.QRect(10, 570, 651, 241))
        self.listView_4.setObjectName("listView_4")
        self.listView_3 = QtWidgets.QListView(self.tab)
        self.listView_3.setGeometry(QtCore.QRect(10, 10, 651, 551))
        self.listView_3.setObjectName("listView_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listView_6 = QtWidgets.QListView(self.tab_2)
        self.listView_6.setGeometry(QtCore.QRect(10, 10, 651, 261))
        self.listView_6.setObjectName("listView_6")
        self.listView_7 = QtWidgets.QListView(self.tab_2)
        self.listView_7.setGeometry(QtCore.QRect(10, 280, 651, 261))
        self.listView_7.setObjectName("listView_7")
        self.listView_8 = QtWidgets.QListView(self.tab_2)
        self.listView_8.setGeometry(QtCore.QRect(10, 550, 651, 261))
        self.listView_8.setObjectName("listView_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 640, 93, 29))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 640, 93, 29))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(50, 30, 271, 61))
        self.label_18.setText("")
        # self.label_18.setPixmap(QtGui.QPixmap("logo_white.ico"))
        self.label_18.setObjectName("label_18")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 20, 511, 861))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 800, 93, 29))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 640, 93, 29))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 800, 93, 29))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 800, 93, 29))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(80, 720, 411, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_23 = QtWidgets.QLabel(self.groupBox_5)
        self.label_23.setGeometry(QtCore.QRect(10, 30, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_16.setGeometry(QtCore.QRect(100, 30, 211, 21))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_5)
        self.toolButton_2.setGeometry(QtCore.QRect(330, 30, 47, 21))
        self.toolButton_2.setObjectName("toolButton_2")
        self.textBrowser_2.raise_()
        self.textBrowser.raise_()
        self.line.raise_()
        self.listView.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.listView_2.raise_()
        self.tabWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_18.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.groupBox_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1301, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_S = QtWidgets.QMenu(self.menuFile)
        self.menu_S.setObjectName("menu_S")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menu_N = QtWidgets.QMenu(self.menuEdit)
        self.menu_N.setObjectName("menu_N")
        self.menuqq = QtWidgets.QMenu(self.menubar)
        self.menuqq.setObjectName("menuqq")
        self.menu = QtWidgets.QMenu(self.menuqq)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuqq)
        self.menu_2.setObjectName("menu_2")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menubar)
        self.action11 = QtWidgets.QAction(MainWindow)
        self.action11.setObjectName("action11")
        self.action11_2 = QtWidgets.QAction(MainWindow)
        self.action11_2.setObjectName("action11_2")
        self.action11_3 = QtWidgets.QAction(MainWindow)
        self.action11_3.setObjectName("action11_3")
        self.action11_5 = QtWidgets.QAction(MainWindow)
        self.action11_5.setObjectName("action11_5")
        self.action11_6 = QtWidgets.QAction(MainWindow)
        self.action11_6.setObjectName("action11_6")
        self.action11_7 = QtWidgets.QAction(MainWindow)
        self.action11_7.setObjectName("action11_7")
        self.action11_8 = QtWidgets.QAction(MainWindow)
        self.action11_8.setObjectName("action11_8")
        self.actiontui = QtWidgets.QAction(MainWindow)
        self.actiontui.setObjectName("actiontui")
        self.action11_9 = QtWidgets.QAction(MainWindow)
        self.action11_9.setObjectName("action11_9")
        self.action11_11 = QtWidgets.QAction(MainWindow)
        self.action11_11.setObjectName("action11_11")
        self.action111 = QtWidgets.QAction(MainWindow)
        self.action111.setObjectName("action111")
        self.actionm1 = QtWidgets.QAction(MainWindow)
        self.actionm1.setObjectName("actionm1")
        self.action11_12 = QtWidgets.QAction(MainWindow)
        self.action11_12.setObjectName("action11_12")
        self.action1_2 = QtWidgets.QAction(MainWindow)
        self.action1_2.setObjectName("action1_2")
        self.action11_14 = QtWidgets.QAction(MainWindow)
        self.action11_14.setObjectName("action11_14")
        self.action11_15 = QtWidgets.QAction(MainWindow)
        self.action11_15.setObjectName("action11_15")
        self.actionxi = QtWidgets.QAction(MainWindow)
        self.actionxi.setObjectName("actionxi")
        self.actionding = QtWidgets.QAction(MainWindow)
        self.actionding.setObjectName("actionding")
        self.actionguanyu = QtWidgets.QAction(MainWindow)
        self.actionguanyu.setObjectName("actionguanyu")
        self.actionqq = QtWidgets.QAction(MainWindow)
        self.actionqq.setObjectName("actionqq")
        self.action12 = QtWidgets.QAction(MainWindow)
        self.action12.setObjectName("action12")
        self.action11_13 = QtWidgets.QAction(MainWindow)
        self.action11_13.setObjectName("action11_13")
        self.action22 = QtWidgets.QAction(MainWindow)
        self.action22.setObjectName("action22")
        self.actionimport1 = QtWidgets.QAction(MainWindow)
        self.actionimport1.setObjectName("actionimport1")
        self.actionimport2 = QtWidgets.QAction(MainWindow)
        self.actionimport2.setObjectName("actionimport2")
        self.actionji = QtWidgets.QAction(MainWindow)
        self.actionji.setObjectName("actionji")
        self.actionqing = QtWidgets.QAction(MainWindow)
        self.actionqing.setObjectName("actionqing")
        self.menu_S.addAction(self.actionimport1)
        self.menu_S.addAction(self.actionimport2)
        self.menuFile.addAction(self.action11_2)
        self.menuFile.addAction(self.action11_3)
        self.menuFile.addAction(self.menu_S.menuAction())
        self.menuFile.addAction(self.action11_5)
        self.menuFile.addAction(self.action11_6)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action11_8)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actiontui)
        self.menu_N.addAction(self.action11_13)
        self.menu_N.addAction(self.action22)
        self.menuEdit.addAction(self.action11_9)
        self.menuEdit.addAction(self.actionji)
        self.menuEdit.addAction(self.menu_N.menuAction())
        self.menuEdit.addAction(self.actionqing)
        self.menu.addAction(self.action11_11)
        self.menu.addAction(self.action111)
        self.menu_2.addAction(self.actionm1)
        self.menu_2.addAction(self.action11_12)
        self.menuqq.addAction(self.menu.menuAction())
        self.menuqq.addAction(self.menu_2.menuAction())
        self.menu_H.addAction(self.actionguanyu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuqq.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())

        self.retranslateUi(MainWindow)

        self.toolButton.clicked.connect(self.find_file)
        self.pushButton.clicked.connect(self.calculate)
        self.pushButton_2.clicked.connect(self.output_data)
        self.pushButton_3.clicked.connect(self.accumulate)
        self.toolButton_2.clicked.connect(self.find_file_1)
        self.pushButton_4.clicked.connect(self.clear)
        self.pushButton_5.clicked.connect(self.clear_1)
        self.pushButton_6.clicked.connect(self.output_data_1)
        self.radioButton.clicked.connect(self.ICASE_1)
        self.radioButton_2.clicked.connect(self.ICASE_2)
        self.radioButton_3.clicked.connect(self.ICASE_3)
        self.radioButton_4.clicked.connect(self.ICASE_4)

        self.action111.triggered.connect(self.language_change_EN)  # 英文
        self.action11_11.triggered.connect(self.language_change_ZN)  # 中文

        self.actionimport1.triggered.connect(self.find_file)  # 找文件
        self.actionimport2.triggered.connect(self.find_file_1)  # 找文件
        self.actiontui.triggered.connect(QtCore.QCoreApplication.exit)  # 退出

        self.action11_9.triggered.connect(self.calculate)  # 开始计算
        self.actionji.triggered.connect(self.accumulate)  # 积分
        self.action11_13.triggered.connect(self.output_data)  # 导出数据
        self.action22.triggered.connect(self.output_data_1)  # 导出数据
        self.actionqing.triggered.connect(self.clear)     # 清除曲线
        self.actionqing.triggered.connect(self.clear_1)    # 清除曲线
        self.actionm1.triggered.connect(self.Theme_change_light)   # 切换为明亮主题
        self.action11_12.triggered.connect(self.Theme_change_dark)  # 切换为灰暗主题

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Specfit"))
        self.groupBox_3.setTitle(_translate("MainWindow", "目标谱"))
        self.label_17.setText(_translate("MainWindow", "文件路径"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.groupBox_4.setTitle(_translate("MainWindow", "拟合参数"))
        self.label_2.setText(_translate("MainWindow", "时程"))
        self.label_3.setText(_translate("MainWindow", "步长"))
        self.label_4.setText(_translate("MainWindow", "ICASE"))
        self.radioButton.setText(_translate("MainWindow", "1"))
        self.radioButton_2.setText(_translate("MainWindow", "2"))
        self.radioButton_3.setText(_translate("MainWindow", "3"))
        self.radioButton_4.setText(_translate("MainWindow", "4"))
        self.label_5.setText(_translate("MainWindow", "TRISE"))
        self.label_6.setText(_translate("MainWindow", "TIVL"))
        self.label_7.setText(_translate("MainWindow", "A0"))
        self.label_8.setText(_translate("MainWindow", "ALFA0"))
        self.label_9.setText(_translate("MainWindow", "BETA0"))
        self.label_10.setText(_translate("MainWindow", "IPOW"))
        self.label_11.setText(_translate("MainWindow", "GMAX"))
        self.label_12.setText(_translate("MainWindow", "持时"))
        self.label_13.setText(_translate("MainWindow", "随机数"))
        self.label_14.setText(_translate("MainWindow", "迭代数"))
        self.label_15.setText(_translate("MainWindow", "目标谱点数"))
        self.label_16.setText(_translate("MainWindow", "阻尼"))
        self.lineEdit.setText(_translate("MainWindow", "1"))
        self.lineEdit_2.setText(_translate("MainWindow", "0.01"))
        self.lineEdit_3.setText(_translate("MainWindow", "5"))
        self.lineEdit_4.setText(_translate("MainWindow", "20"))
        self.lineEdit_5.setText(_translate("MainWindow", "0.3"))
        self.lineEdit_6.setText(_translate("MainWindow", "12"))
        self.lineEdit_7.setText(_translate("MainWindow", "270"))
        self.lineEdit_8.setText(_translate("MainWindow", "0"))
        self.lineEdit_9.setText(_translate("MainWindow", "30"))
        self.lineEdit_10.setText(_translate("MainWindow", "45"))
        self.lineEdit_11.setText(_translate("MainWindow", "0.05"))
        self.lineEdit_12.setText(_translate("MainWindow", "0"))
        self.lineEdit_13.setText(_translate("MainWindow", "0"))
        self.lineEdit_14.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "设计地震动拟合"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "时程积分"))
        self.pushButton.setText(_translate("MainWindow", "开始拟合"))
        self.pushButton_2.setText(_translate("MainWindow", "导出数据"))
        self.pushButton_3.setText(_translate("MainWindow", "进行积分"))
        self.pushButton_4.setText(_translate("MainWindow", "清除曲线"))
        self.pushButton_5.setText(_translate("MainWindow", "清除曲线"))
        self.pushButton_6.setText(_translate("MainWindow", "导出数据"))
        self.groupBox_5.setTitle(_translate("MainWindow", "时程分析文件"))
        self.label_23.setText(_translate("MainWindow", "文件路径"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.menuFile.setTitle(_translate("MainWindow", "文件(F)"))
        self.menu_S.setTitle(_translate("MainWindow", "导入(&I)"))
        self.menuEdit.setTitle(_translate("MainWindow", "编辑(E)"))
        self.menu_N.setTitle(_translate("MainWindow", "导出数据(&N)"))
        self.menuqq.setTitle(_translate("MainWindow", "设置(S)"))
        self.menu.setTitle(_translate("MainWindow", "语言"))
        self.menu_2.setTitle(_translate("MainWindow", "主题"))
        self.menu_H.setTitle(_translate("MainWindow", "帮助(H)"))
        self.action11.setText(_translate("MainWindow", "新建(&N)"))
        self.action11_2.setText(_translate("MainWindow", "新建(&N)"))
        self.action11_3.setText(_translate("MainWindow", "打开(&O)"))
        self.action11_5.setText(_translate("MainWindow", "另存为(&A)"))
        self.action11_6.setText(_translate("MainWindow", "打印(&P)"))
        self.action11_7.setText(_translate("MainWindow", "保存图片(I)"))
        self.action11_8.setText(_translate("MainWindow", "清零(&R)"))
        self.actiontui.setText(_translate("MainWindow", "退出(&Q)"))
        self.action11_9.setText(_translate("MainWindow", "开始拟合(&C)"))
        self.action11_11.setText(_translate("MainWindow", "中文(Chinese)"))
        self.action111.setText(_translate("MainWindow", "英文(English)"))
        self.actionm1.setText(_translate("MainWindow", "明亮"))
        self.action11_12.setText(_translate("MainWindow", "灰暗"))
        self.action1_2.setText(_translate("MainWindow", "规范1"))
        self.action11_14.setText(_translate("MainWindow", "规范2"))
        self.action11_15.setText(_translate("MainWindow", "规范3"))
        self.actionxi.setText(_translate("MainWindow", "导入规范"))
        self.actionding.setText(_translate("MainWindow", "定义规范"))
        self.actionguanyu.setText(_translate("MainWindow", "关于Specfit"))
        self.actionqq.setText(_translate("MainWindow", "设计地震动拟合数据"))
        self.action12.setText(_translate("MainWindow", "时程积分数据"))
        self.action11_13.setText(_translate("MainWindow", "设计地震动数据"))
        self.action22.setText(_translate("MainWindow", "时程积分"))
        self.actionimport1.setText(_translate("MainWindow", "目标谱文件"))
        self.actionimport2.setText(_translate("MainWindow", "时程分析文件"))
        self.actionji.setText(_translate("MainWindow", "积分"))
        self.actionqing.setText(_translate("MainWindow", "清除曲线"))