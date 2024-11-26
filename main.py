


# This Python file uses the following encoding: utf-8
print('Starting...')
import sys,os
import csv
try:

    import numpy as np
except:
    os.system('pip install numpy')
try:

    import pandas as pd
except:
    os.system('pip install pandas')

try:

    from pyautogui import screenshot as script
except:
    os.system('pip install pyautogui')
try:

    import pyqtgraph as pg
except:
    os.system('pip install pyqtgraph')

from datetime import datetime
try:

    from PySide6.QtGui import QColor
    from PySide6.QtCore import Qt, QPropertyAnimation, QRect

    from PySide6.QtWidgets import QApplication,QVBoxLayout, QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox,QFileDialog
    # Important:
    # You need to run the following command to generate the ui_form.py file
    #     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
except:
    os.system('pip install PySide6')



    

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QComboBox,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolButton, QWidget)

class Ui_form1(object):
    def setupUi(self, form1):
        if not form1.objectName():
            form1.setObjectName(u"form1")
        form1.resize(1200, 716)
        form1.setMinimumSize(QSize(860, 437))
        form1.setMaximumSize(QSize(1200, 716))
        self.actionINR = QAction(form1)
        self.actionINR.setObjectName(u"actionINR")
        self.actionOpen = QAction(form1)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(form1)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(form1)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(form1)
        self.actionExit.setObjectName(u"actionExit")
        self.action_screenshot = QAction(form1)
        self.action_screenshot.setObjectName(u"action_screenshot")
        self.actionTable_Edit = QAction(form1)
        self.actionTable_Edit.setObjectName(u"actionTable_Edit")
        self.actionAs_CSV_Excel = QAction(form1)
        self.actionAs_CSV_Excel.setObjectName(u"actionAs_CSV_Excel")
        self.actionOpen_Directories = QAction(form1)
        self.actionOpen_Directories.setObjectName(u"actionOpen_Directories")
        self.actionLight = QAction(form1)
        self.actionLight.setObjectName(u"actionLight")
        self.actionDakr = QAction(form1)
        self.actionDakr.setObjectName(u"actionDakr")
        self.actionUSD = QAction(form1)
        self.actionUSD.setObjectName(u"actionUSD")
        self.actionClear_Data = QAction(form1)
        self.actionClear_Data.setObjectName(u"actionClear_Data")
        self.actionRefresh = QAction(form1)
        self.actionRefresh.setObjectName(u"actionRefresh")
        self.actionInfo = QAction(form1)
        self.actionInfo.setObjectName(u"actionInfo")
        self.centralwidget = QWidget(form1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1200, 800))
        self.label.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(860, 9, 331, 221))
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 371, 221))
        self.widget.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.calendarWidget = QCalendarWidget(self.widget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(0, 0, 331, 201))
        self.calendarWidget.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 11pt \"Segoe UI\";\n"
"color: rgb(49, 77, 107);\n"
"border-color: rgb(95, 95, 95);\n"
"selection-color: rgb(248, 248, 248);\n"
"gridline-color: rgb(111, 111, 111);\n"
"selection-background-color: rgb(126, 126, 126);")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textEdit_notes = QTextEdit(self.tab_2)
        self.textEdit_notes.setObjectName(u"textEdit_notes")
        self.textEdit_notes.setGeometry(QRect(0, 0, 331, 203))
        font = QFont()
        font.setPointSize(14)
        self.textEdit_notes.setFont(font)
        self.textEdit_notes.setAutoFillBackground(False)
        self.textEdit_notes.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
"color: rgb(98, 255, 156);")
        self.textEdit_notes.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_notes.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.textEdit_notes.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextEditable|Qt.TextInteractionFlag.TextEditorInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)
        self.tabWidget.addTab(self.tab_2, "")
        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(12, 35, 841, 361))
        self.widget_5.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.label_expense_record = QLabel(self.widget_5)
        self.label_expense_record.setObjectName(u"label_expense_record")
        self.label_expense_record.setGeometry(QRect(14, -4, 181, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_expense_record.setFont(font1)
        self.label_expense_record.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.label_total_expense = QLabel(self.widget_5)
        self.label_total_expense.setObjectName(u"label_total_expense")
        self.label_total_expense.setGeometry(QRect(450, 325, 231, 31))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_total_expense.setFont(font2)
        self.label_total_expense.setStyleSheet(u"color: rgb(107, 139, 255);")
        self.label_total_spends = QLabel(self.widget_5)
        self.label_total_spends.setObjectName(u"label_total_spends")
        self.label_total_spends.setGeometry(QRect(682, 331, 151, 21))
        self.label_total_spends.setFont(font2)
        self.label_total_spends.setStyleSheet(u"color: rgb(255, 133, 192);")
        self.tableWidget_1 = QTableWidget(self.widget_5)
        if (self.tableWidget_1.columnCount() < 7):
            self.tableWidget_1.setColumnCount(7)
        font3 = QFont()
        font3.setPointSize(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tableWidget_1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget_1.setObjectName(u"tableWidget_1")
        self.tableWidget_1.setGeometry(QRect(10, 27, 821, 301))
        self.tableWidget_1.setFont(font2)
        self.tableWidget_1.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
"border-color: rgb(130, 255, 213);\n"
"alternate-background-color: rgb(137, 143, 255);\n"
"\n"
"selection-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(97, 46, 46);\n"
"color: rgb(255, 193, 106);")
        self.tableWidget_1.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_1.setFrameShadow(QFrame.Shadow.Plain)
        self.tableWidget_1.setLineWidth(1)
        self.tableWidget_1.setMidLineWidth(0)
        self.tableWidget_1.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget_1.setAlternatingRowColors(True)
        self.tableWidget_1.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.tableWidget_1.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_1.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tableWidget_1.setShowGrid(True)
        self.tableWidget_1.setGridStyle(Qt.PenStyle.DashLine)
        self.tableWidget_1.setSortingEnabled(False)
        self.tableWidget_1.setRowCount(0)
        self.tableWidget_1.setColumnCount(7)
        self.tableWidget_1.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_1.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget_1.horizontalHeader().setDefaultSectionSize(106)
        self.tableWidget_1.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_1.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_1.verticalHeader().setStretchLastSection(False)
        self.lineEdit_spend = QLineEdit(self.widget_5)
        self.lineEdit_spend.setObjectName(u"lineEdit_spend")
        self.lineEdit_spend.setGeometry(QRect(12, 331, 121, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_spend.sizePolicy().hasHeightForWidth())
        self.lineEdit_spend.setSizePolicy(sizePolicy)
        self.lineEdit_spend.setMinimumSize(QSize(0, 0))
        self.lineEdit_spend.setMaximumSize(QSize(1920, 70))
        self.lineEdit_spend.setFont(font)
        self.lineEdit_spend.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_spend.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(83, 248, 195);asd")
        self.lineEdit_spend.setMaxLength(1000)
        self.lineEdit_spend.setFrame(False)
        self.lineEdit_spend.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_spend.setCursorPosition(0)
        self.lineEdit_spend.setDragEnabled(True)
        self.lineEdit_spend.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_spend.setClearButtonEnabled(False)
        self.toolButton_save1 = QToolButton(self.widget_5)
        self.toolButton_save1.setObjectName(u"toolButton_save1")
        self.toolButton_save1.setGeometry(QRect(380, 329, 61, 26))
        self.toolButton_save1.setFont(font1)
        self.toolButton_save1.setStyleSheet(u"background-color: rgb(98, 255, 156);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_item = QLineEdit(self.widget_5)
        self.lineEdit_item.setObjectName(u"lineEdit_item")
        self.lineEdit_item.setGeometry(QRect(137, 331, 111, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_item.sizePolicy().hasHeightForWidth())
        self.lineEdit_item.setSizePolicy(sizePolicy)
        self.lineEdit_item.setMinimumSize(QSize(0, 0))
        self.lineEdit_item.setMaximumSize(QSize(1920, 70))
        self.lineEdit_item.setFont(font)
        self.lineEdit_item.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_item.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(83, 248, 195);asd")
        self.lineEdit_item.setMaxLength(1000)
        self.lineEdit_item.setFrame(False)
        self.lineEdit_item.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_item.setCursorPosition(0)
        self.lineEdit_item.setDragEnabled(True)
        self.lineEdit_item.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_item.setClearButtonEnabled(False)
        self.lineEdit_reciepent = QLineEdit(self.widget_5)
        self.lineEdit_reciepent.setObjectName(u"lineEdit_reciepent")
        self.lineEdit_reciepent.setGeometry(QRect(253, 331, 121, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_reciepent.sizePolicy().hasHeightForWidth())
        self.lineEdit_reciepent.setSizePolicy(sizePolicy)
        self.lineEdit_reciepent.setMinimumSize(QSize(0, 0))
        self.lineEdit_reciepent.setMaximumSize(QSize(1920, 70))
        self.lineEdit_reciepent.setFont(font)
        self.lineEdit_reciepent.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_reciepent.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(83, 248, 195);asd")
        self.lineEdit_reciepent.setMaxLength(1000)
        self.lineEdit_reciepent.setFrame(False)
        self.lineEdit_reciepent.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_reciepent.setCursorPosition(0)
        self.lineEdit_reciepent.setDragEnabled(True)
        self.lineEdit_reciepent.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_reciepent.setClearButtonEnabled(False)
        self.toolButton_del_row = QToolButton(self.widget_5)
        self.toolButton_del_row.setObjectName(u"toolButton_del_row")
        self.toolButton_del_row.setGeometry(QRect(802, 1, 31, 26))
        font4 = QFont()
        font4.setPointSize(20)
        self.toolButton_del_row.setFont(font4)
        self.toolButton_del_row.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 0, 0);")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(16, -1, 161, 31))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(860, 239, 331, 185))
        self.textEdit.setStyleSheet(u"background-color: rgb(31, 31, 49);")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setLineWidth(0)
        self.textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(1042, 366, 131, 51))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_name.setFont(font5)
        self.label_name.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_name.setWordWrap(True)
        self.label_income = QLabel(self.centralwidget)
        self.label_income.setObjectName(u"label_income")
        self.label_income.setGeometry(QRect(970, 286, 108, 20))
        self.label_income.setFont(font5)
        self.label_income.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.label_expense = QLabel(self.centralwidget)
        self.label_expense.setObjectName(u"label_expense")
        self.label_expense.setGeometry(QRect(970, 306, 108, 20))
        self.label_expense.setFont(font5)
        self.label_expense.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.label_savings = QLabel(self.centralwidget)
        self.label_savings.setObjectName(u"label_savings")
        self.label_savings.setGeometry(QRect(970, 326, 108, 20))
        self.label_savings.setFont(font5)
        self.label_savings.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.label_gains = QLabel(self.centralwidget)
        self.label_gains.setObjectName(u"label_gains")
        self.label_gains.setGeometry(QRect(970, 346, 108, 20))
        self.label_gains.setFont(font5)
        self.label_gains.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(12, 432, 841, 244))
        self.widget_6.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.label_extra_gains = QLabel(self.widget_6)
        self.label_extra_gains.setObjectName(u"label_extra_gains")
        self.label_extra_gains.setGeometry(QRect(14, -4, 181, 31))
        self.label_extra_gains.setFont(font1)
        self.label_extra_gains.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.label_monthly_gains = QLabel(self.widget_6)
        self.label_monthly_gains.setObjectName(u"label_monthly_gains")
        self.label_monthly_gains.setGeometry(QRect(450, 207, 201, 31))
        self.label_monthly_gains.setFont(font2)
        self.label_monthly_gains.setStyleSheet(u"color: rgb(107, 139, 255);")
        self.label_total_gains = QLabel(self.widget_6)
        self.label_total_gains.setObjectName(u"label_total_gains")
        self.label_total_gains.setGeometry(QRect(660, 212, 171, 21))
        self.label_total_gains.setFont(font2)
        self.label_total_gains.setStyleSheet(u"color: rgb(174, 255, 82);")
        self.tableWidget_2 = QTableWidget(self.widget_6)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        if (self.tableWidget_2.rowCount() < 12):
            self.tableWidget_2.setRowCount(12)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 27, 821, 181))
        self.tableWidget_2.setFont(font2)
        self.tableWidget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
"border-color: rgb(130, 255, 213);\n"
"alternate-background-color: rgb(137, 143, 255);\n"
"selection-background-color: rgb(75, 251, 175);\n"
"selection-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(29, 75, 46);\n"
"color: rgb(75, 251, 175);")
        self.tableWidget_2.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_2.setFrameShadow(QFrame.Shadow.Plain)
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setMidLineWidth(0)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.PenStyle.DashLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setRowCount(12)
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(106)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.lineEdit_get = QLineEdit(self.widget_6)
        self.lineEdit_get.setObjectName(u"lineEdit_get")
        self.lineEdit_get.setGeometry(QRect(12, 213, 121, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_get.sizePolicy().hasHeightForWidth())
        self.lineEdit_get.setSizePolicy(sizePolicy)
        self.lineEdit_get.setMinimumSize(QSize(0, 0))
        self.lineEdit_get.setMaximumSize(QSize(1920, 70))
        self.lineEdit_get.setFont(font)
        self.lineEdit_get.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_get.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(83, 248, 195);asd")
        self.lineEdit_get.setMaxLength(1000)
        self.lineEdit_get.setFrame(False)
        self.lineEdit_get.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_get.setCursorPosition(0)
        self.lineEdit_get.setDragEnabled(True)
        self.lineEdit_get.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_get.setClearButtonEnabled(False)
        self.toolButton_save2 = QToolButton(self.widget_6)
        self.toolButton_save2.setObjectName(u"toolButton_save2")
        self.toolButton_save2.setGeometry(QRect(380, 211, 61, 26))
        self.toolButton_save2.setFont(font1)
        self.toolButton_save2.setStyleSheet(u"background-color: rgb(98, 255, 156);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_for_what = QLineEdit(self.widget_6)
        self.lineEdit_for_what.setObjectName(u"lineEdit_for_what")
        self.lineEdit_for_what.setGeometry(QRect(137, 213, 111, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_for_what.sizePolicy().hasHeightForWidth())
        self.lineEdit_for_what.setSizePolicy(sizePolicy)
        self.lineEdit_for_what.setMinimumSize(QSize(0, 0))
        self.lineEdit_for_what.setMaximumSize(QSize(1920, 70))
        self.lineEdit_for_what.setFont(font)
        self.lineEdit_for_what.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_for_what.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(83, 248, 195);asd")
        self.lineEdit_for_what.setMaxLength(1000)
        self.lineEdit_for_what.setFrame(False)
        self.lineEdit_for_what.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_for_what.setCursorPosition(0)
        self.lineEdit_for_what.setDragEnabled(True)
        self.lineEdit_for_what.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_for_what.setClearButtonEnabled(False)
        self.lineEdit_giver = QLineEdit(self.widget_6)
        self.lineEdit_giver.setObjectName(u"lineEdit_giver")
        self.lineEdit_giver.setGeometry(QRect(253, 213, 121, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_giver.sizePolicy().hasHeightForWidth())
        self.lineEdit_giver.setSizePolicy(sizePolicy)
        self.lineEdit_giver.setMinimumSize(QSize(0, 0))
        self.lineEdit_giver.setMaximumSize(QSize(1920, 70))
        self.lineEdit_giver.setFont(font)
        self.lineEdit_giver.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_giver.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(83, 248, 195);asd")
        self.lineEdit_giver.setMaxLength(1000)
        self.lineEdit_giver.setFrame(False)
        self.lineEdit_giver.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_giver.setCursorPosition(0)
        self.lineEdit_giver.setDragEnabled(True)
        self.lineEdit_giver.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_giver.setClearButtonEnabled(False)
        self.toolButton_del_row_2 = QToolButton(self.widget_6)
        self.toolButton_del_row_2.setObjectName(u"toolButton_del_row_2")
        self.toolButton_del_row_2.setGeometry(QRect(802, 0, 31, 26))
        self.toolButton_del_row_2.setFont(font4)
        self.toolButton_del_row_2.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 0, 0);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1070, 290, 70, 70))
        self.label_2.setPixmap(QPixmap(u"pprofile2.png"))
        self.label_2.setScaledContents(True)
        self.lineEdit_income = QLineEdit(self.centralwidget)
        self.lineEdit_income.setObjectName(u"lineEdit_income")
        self.lineEdit_income.setGeometry(QRect(518, 5, 161, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_income.sizePolicy().hasHeightForWidth())
        self.lineEdit_income.setSizePolicy(sizePolicy)
        self.lineEdit_income.setMinimumSize(QSize(0, 0))
        self.lineEdit_income.setMaximumSize(QSize(1920, 70))
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(True)
        self.lineEdit_income.setFont(font6)
        self.lineEdit_income.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_income.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(255, 170, 0);")
        self.lineEdit_income.setMaxLength(1000)
        self.lineEdit_income.setFrame(False)
        self.lineEdit_income.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_income.setCursorPosition(1)
        self.lineEdit_income.setDragEnabled(True)
        self.lineEdit_income.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_income.setClearButtonEnabled(False)
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(769, 5, 81, 26))
        font7 = QFont()
        font7.setPointSize(10)
        self.comboBox_3.setFont(font7)
        self.comboBox_3.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(98, 255, 156);")
        self.comboBox_3.setFrame(False)
        self.lineEdit_calc = QLineEdit(self.centralwidget)
        self.lineEdit_calc.setObjectName(u"lineEdit_calc")
        self.lineEdit_calc.setGeometry(QRect(633, 402, 221, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_calc.sizePolicy().hasHeightForWidth())
        self.lineEdit_calc.setSizePolicy(sizePolicy)
        self.lineEdit_calc.setMinimumSize(QSize(0, 0))
        self.lineEdit_calc.setMaximumSize(QSize(1920, 70))
        self.lineEdit_calc.setFont(font6)
        self.lineEdit_calc.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_calc.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(255, 170, 0);")
        self.lineEdit_calc.setMaxLength(1000)
        self.lineEdit_calc.setFrame(False)
        self.lineEdit_calc.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_calc.setCursorPosition(0)
        self.lineEdit_calc.setDragEnabled(True)
        self.lineEdit_calc.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_calc.setClearButtonEnabled(False)
        self.label_calc = QLabel(self.centralwidget)
        self.label_calc.setObjectName(u"label_calc")
        self.label_calc.setGeometry(QRect(398, 398, 231, 31))
        self.label_calc.setFont(font2)
        self.label_calc.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.label_calc.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.toolButton_set = QToolButton(self.centralwidget)
        self.toolButton_set.setObjectName(u"toolButton_set")
        self.toolButton_set.setGeometry(QRect(694, 4, 61, 26))
        self.toolButton_set.setFont(font1)
        self.toolButton_set.setStyleSheet(u"background-color: rgb(98, 255, 156);\n"
"color: rgb(0, 0, 0);")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(356, -1, 161, 31))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.lineEdit_income0 = QLineEdit(self.centralwidget)
        self.lineEdit_income0.setObjectName(u"lineEdit_income0")
        self.lineEdit_income0.setGeometry(QRect(183, 5, 161, 25))
        sizePolicy.setHeightForWidth(self.lineEdit_income0.sizePolicy().hasHeightForWidth())
        self.lineEdit_income0.setSizePolicy(sizePolicy)
        self.lineEdit_income0.setMinimumSize(QSize(0, 0))
        self.lineEdit_income0.setMaximumSize(QSize(1920, 70))
        self.lineEdit_income0.setFont(font6)
        self.lineEdit_income0.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_income0.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(255, 170, 0);")
        self.lineEdit_income0.setMaxLength(1000)
        self.lineEdit_income0.setFrame(False)
        self.lineEdit_income0.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_income0.setCursorPosition(1)
        self.lineEdit_income0.setDragEnabled(True)
        self.lineEdit_income0.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_income0.setClearButtonEnabled(False)
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(860, 432, 331, 241))
        self.tabWidget_2.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget_2.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget_2.setDocumentMode(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.widget_graph = QWidget(self.tab_5)
        self.widget_graph.setObjectName(u"widget_graph")
        self.widget_graph.setGeometry(QRect(0, -10, 331, 241))
        self.widget_graph.setStyleSheet(u"background-color: rgb(28, 28, 28);")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.widget_graph_2 = QWidget(self.tab_6)
        self.widget_graph_2.setObjectName(u"widget_graph_2")
        self.widget_graph_2.setGeometry(QRect(0, 0, 331, 241))
        self.widget_graph_2.setStyleSheet(u"background-color: rgb(28, 28, 28);")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.toolButton_expand = QToolButton(self.centralwidget)
        self.toolButton_expand.setObjectName(u"toolButton_expand")
        self.toolButton_expand.setGeometry(QRect(694, 36, 61, 26))
        self.toolButton_expand.setFont(font1)
        self.toolButton_expand.setStyleSheet(u"background-color: rgb(137, 143, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_date = QLabel(self.centralwidget)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(30, 396, 181, 31))
        self.label_date.setFont(font2)
        self.label_date.setStyleSheet(u"color: rgb(107, 139, 255);")
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(10, 40, 840, 356))
        self.label_image.setPixmap(QPixmap(u"back3.jpg"))
        self.label_image.setScaledContents(True)
        self.lineEdit_admin_name = QLineEdit(self.centralwidget)
        self.lineEdit_admin_name.setObjectName(u"lineEdit_admin_name")
        self.lineEdit_admin_name.setGeometry(QRect(30, 344, 331, 31))
        sizePolicy.setHeightForWidth(self.lineEdit_admin_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_admin_name.setSizePolicy(sizePolicy)
        self.lineEdit_admin_name.setMinimumSize(QSize(0, 0))
        self.lineEdit_admin_name.setMaximumSize(QSize(1920, 70))
        self.lineEdit_admin_name.setFont(font)
        self.lineEdit_admin_name.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_admin_name.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"alternate-background-color: rgb(225, 225, 225);\n"
"selection-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(83, 248, 195);asd")
        self.lineEdit_admin_name.setMaxLength(1000)
        self.lineEdit_admin_name.setFrame(False)
        self.lineEdit_admin_name.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_admin_name.setCursorPosition(0)
        self.lineEdit_admin_name.setDragEnabled(True)
        self.lineEdit_admin_name.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_admin_name.setClearButtonEnabled(False)
        self.label_profile = QLabel(self.centralwidget)
        self.label_profile.setObjectName(u"label_profile")
        self.label_profile.setGeometry(QRect(94, 94, 211, 211))
        self.label_profile.setPixmap(QPixmap(u"pprofile2.png"))
        self.label_profile.setScaledContents(True)
        self.label_trans = QLabel(self.centralwidget)
        self.label_trans.setObjectName(u"label_trans")
        self.label_trans.setGeometry(QRect(22, 51, 351, 334))
        self.label_trans.setStyleSheet(u"background-color: rgba(0, 0, 0,0.5);")
        form1.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.tabWidget.raise_()
        self.widget_5.raise_()
        self.textEdit.raise_()
        self.label_name.raise_()
        self.label_income.raise_()
        self.label_expense.raise_()
        self.label_savings.raise_()
        self.label_gains.raise_()
        self.widget_6.raise_()
        self.label_2.raise_()
        self.comboBox_3.raise_()
        self.lineEdit_calc.raise_()
        self.label_calc.raise_()
        self.tabWidget_2.raise_()
        self.toolButton_expand.raise_()
        self.label_date.raise_()
        self.label_image.raise_()
        self.label_13.raise_()
        self.lineEdit_income0.raise_()
        self.label_14.raise_()
        self.lineEdit_income.raise_()
        self.toolButton_set.raise_()
        self.label_trans.raise_()
        self.label_profile.raise_()
        self.lineEdit_admin_name.raise_()
        self.menubar = QMenuBar(form1)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 33))
        self.menubar.setFont(font7)
        self.menubar.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
"border-color: rgb(130, 255, 213);\n"
"alternate-background-color: rgb(137, 143, 255);\n"
"selection-color: rgb(98, 255, 156);\n"
"selection-background-color: rgb(49, 49, 49);\n"
"gridline-color: rgb(97, 46, 46);\n"
"color: rgb(172, 161, 255);")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuExport = QMenu(self.menubar)
        self.menuExport.setObjectName(u"menuExport")
        self.menuSnap = QMenu(self.menubar)
        self.menuSnap.setObjectName(u"menuSnap")
        self.menuDark = QMenu(self.menubar)
        self.menuDark.setObjectName(u"menuDark")
        self.menuCurrency = QMenu(self.menubar)
        self.menuCurrency.setObjectName(u"menuCurrency")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuAbout.setFont(font1)
        form1.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuSnap.menuAction())
        self.menubar.addAction(self.menuDark.menuAction())
        self.menubar.addAction(self.menuCurrency.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionTable_Edit)
        self.menuEdit.addAction(self.actionClear_Data)
        self.menuExport.addAction(self.actionAs_CSV_Excel)
        self.menuSnap.addSeparator()
        self.menuSnap.addAction(self.action_screenshot)
        self.menuSnap.addAction(self.actionOpen_Directories)
        self.menuDark.addAction(self.actionLight)
        self.menuDark.addAction(self.actionDakr)
        self.menuCurrency.addAction(self.actionINR)
        self.menuCurrency.addAction(self.actionUSD)
        self.menuAbout.addAction(self.actionInfo)

        self.retranslateUi(form1)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(form1)
    # setupUi

    def retranslateUi(self, form1):
        form1.setWindowTitle(QCoreApplication.translate("form1", u"Finance Flow v1.1", None))
        self.actionINR.setText(QCoreApplication.translate("form1", u"INR", None))
        self.actionOpen.setText(QCoreApplication.translate("form1", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("form1", u"Save Settings", None))
        self.actionSave_As.setText(QCoreApplication.translate("form1", u"Save Notes", None))
        self.actionExit.setText(QCoreApplication.translate("form1", u"Exit", None))
        self.action_screenshot.setText(QCoreApplication.translate("form1", u"ScreenShot", None))
        self.actionTable_Edit.setText(QCoreApplication.translate("form1", u"Table Edit", None))
        self.actionAs_CSV_Excel.setText(QCoreApplication.translate("form1", u"As CSV/Excel", None))
        self.actionOpen_Directories.setText(QCoreApplication.translate("form1", u"Open Directory", None))
        self.actionLight.setText(QCoreApplication.translate("form1", u"Light", None))
        self.actionDakr.setText(QCoreApplication.translate("form1", u"Dark", None))
        self.actionUSD.setText(QCoreApplication.translate("form1", u"USD", None))
        self.actionClear_Data.setText(QCoreApplication.translate("form1", u"Reset Data", None))
        self.actionRefresh.setText(QCoreApplication.translate("form1", u"Refresh", None))
        self.actionInfo.setText(QCoreApplication.translate("form1", u"Info", None))
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("form1", u"Calender", None))
        self.textEdit_notes.setHtml(QCoreApplication.translate("form1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_notes.setPlaceholderText(QCoreApplication.translate("form1", u"Type or Just Drag and Drop the websites content here...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("form1", u"Notes", None))
        self.label_expense_record.setText(QCoreApplication.translate("form1", u"Expenses Record:-", None))
        self.label_total_expense.setText(QCoreApplication.translate("form1", u"Total monthly Expense = ", None))
        self.label_total_spends.setText(QCoreApplication.translate("form1", u"0", None))
        ___qtablewidgetitem = self.tableWidget_1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("form1", u"SPEND/-", None));
        ___qtablewidgetitem1 = self.tableWidget_1.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("form1", u"Item/Purpose", None));
        ___qtablewidgetitem2 = self.tableWidget_1.horizontalHeaderItem(4)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("form1", u"Reciepent", None));
        ___qtablewidgetitem3 = self.tableWidget_1.horizontalHeaderItem(6)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("form1", u"Time", None));
        self.lineEdit_spend.setText("")
        self.lineEdit_spend.setPlaceholderText(QCoreApplication.translate("form1", u"Spend/-", None))
        self.toolButton_save1.setText(QCoreApplication.translate("form1", u"Save", None))
        self.lineEdit_item.setText("")
        self.lineEdit_item.setPlaceholderText(QCoreApplication.translate("form1", u"Item...", None))
        self.lineEdit_reciepent.setText("")
        self.lineEdit_reciepent.setPlaceholderText(QCoreApplication.translate("form1", u"Recipient..", None))
        self.toolButton_del_row.setText(QCoreApplication.translate("form1", u"-", None))
        self.label_13.setText(QCoreApplication.translate("form1", u"Monthly Income:", None))
        self.textEdit.setHtml(QCoreApplication.translate("form1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#53f8c3;\"># Monthly Summary Report</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; col"
                        "or:#898fff;\">1. Total Income</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">2. Total Expense</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">3. Net Savings</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">4. Extra Gains</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">5. Miscellaneous Expense</span></p></body></html>", None))
        self.label_name.setText(QCoreApplication.translate("form1", u"Abhishek Verma", None))
        self.label_income.setText(QCoreApplication.translate("form1", u"64000/-", None))
        self.label_expense.setText(QCoreApplication.translate("form1", u"45000", None))
        self.label_savings.setText(QCoreApplication.translate("form1", u"15000", None))
        self.label_gains.setText(QCoreApplication.translate("form1", u"4000", None))
        self.label_extra_gains.setText(QCoreApplication.translate("form1", u"Extra Gains Records:-", None))
        self.label_monthly_gains.setText(QCoreApplication.translate("form1", u"Total monthly Gains = ", None))
        self.label_total_gains.setText(QCoreApplication.translate("form1", u"1600/-", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("form1", u"RECIEVED/-", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("form1", u"Item/N/A", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("form1", u"Payer/Giver", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("form1", u"Time", None));
        self.lineEdit_get.setText("")
        self.lineEdit_get.setPlaceholderText(QCoreApplication.translate("form1", u"Get/-", None))
        self.toolButton_save2.setText(QCoreApplication.translate("form1", u"Save", None))
        self.lineEdit_for_what.setText("")
        self.lineEdit_for_what.setPlaceholderText(QCoreApplication.translate("form1", u"for what...", None))
        self.lineEdit_giver.setText("")
        self.lineEdit_giver.setPlaceholderText(QCoreApplication.translate("form1", u"Giver...", None))
        self.toolButton_del_row_2.setText(QCoreApplication.translate("form1", u"-", None))
        self.label_2.setText("")
        self.lineEdit_income.setText(QCoreApplication.translate("form1", u"0", None))
        self.lineEdit_income.setPlaceholderText(QCoreApplication.translate("form1", u"Spend/-", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("form1", u"  Monthly", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("form1", u"  Weekly", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("form1", u"  Yearly", None))

        self.lineEdit_calc.setText("")
        self.lineEdit_calc.setPlaceholderText(QCoreApplication.translate("form1", u"Use Numkeys...", None))
        self.label_calc.setText(QCoreApplication.translate("form1", u"Calc :", None))
        self.toolButton_set.setText(QCoreApplication.translate("form1", u"Set", None))
        self.label_14.setText(QCoreApplication.translate("form1", u"Current Income:", None))
        self.lineEdit_income0.setText(QCoreApplication.translate("form1", u"0", None))
        self.lineEdit_income0.setPlaceholderText(QCoreApplication.translate("form1", u"Spend/-", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("form1", u"Remaining income", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("form1", u"Extra Gains", None))
        self.toolButton_expand.setText(QCoreApplication.translate("form1", u"Layout", None))
        self.label_date.setText(QCoreApplication.translate("form1", u"Date:- 26/01/2001", None))
        self.label_image.setText("")
        self.lineEdit_admin_name.setText("")
        self.lineEdit_admin_name.setPlaceholderText(QCoreApplication.translate("form1", u"Enter admin name ...", None))
        self.label_profile.setText("")
        self.label_trans.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("form1", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("form1", u"Edit", None))
        self.menuExport.setTitle(QCoreApplication.translate("form1", u"Export", None))
        self.menuSnap.setTitle(QCoreApplication.translate("form1", u"Snap", None))
        self.menuDark.setTitle(QCoreApplication.translate("form1", u"Theme", None))
        self.menuCurrency.setTitle(QCoreApplication.translate("form1", u"Currency", None))
        self.menuHelp.setTitle(QCoreApplication.translate("form1", u"Help", None))
        self.menuAbout.setTitle(QCoreApplication.translate("form1", u"About", None))
    # retranslateUi


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextEdit,
    QWidget)

class Ui_about(object):
    def setupUi(self, about):
        if not about.objectName():
            about.setObjectName(u"about")
        about.resize(670, 500)
        self.textEdit_about = QTextEdit(about)
        self.textEdit_about.setObjectName(u"textEdit_about")
        self.textEdit_about.setGeometry(QRect(0, 0, 670, 500))
        self.textEdit_about.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.textEdit_about.setReadOnly(True)
        self.textEdit_about.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.retranslateUi(about)

        QMetaObject.connectSlotsByName(about)
    # setupUi

    def retranslateUi(self, about):
        about.setWindowTitle(QCoreApplication.translate("about", u"About", None))
        self.textEdit_about.setHtml(QCoreApplication.translate("about", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700; color:#40ffb9;\">About Finance Flow</span></h1>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#40ffb9;\">Overview</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#a58fff;\">Welcome to </span><span style=\" font-size:11pt; font-weight:700; color:#a58fff;\">Finance Flow</span><span style=\" font-size:11pt; color:#a58fff;\"> \u2013 your ultimate companion for managing and tracking personal expenses effortlessly. Designed with simplicity and functionality in mind, Finance Flow helps you keep a detailed record of your spending, visualize your financial health, and make informed decisions about your money.</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#40ffb9;\">Features</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; "
                        "font-weight:700; color:#a58fff;\">Expense Tracking</span><span style=\" font-size:11pt; color:#a58fff;\">: Easily enter and categorize your expenses. Record details about the purpose, recipient, and amount spent.</span></li>\n"
"<li style=\" font-size:11pt; color:#a58fff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Notes and Data Entry</span>: Add insightful notes to each entry for better tracking and future reference.</li>\n"
"<li style=\" font-size:11pt; color:#a58fff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Data Visualization</span>: Visualize your financial data with interactive bar plots using pyqtgraph, helping you understand your remaining income and overall spending patterns.</li>\n"
"<li style=\" font-size:11pt; color:#a58fff;\" style=\" margin-top:0px; margin-bottom:12px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Customizable Tables</span>: Manage and review your data with user-friendly tables that adapt to your needs.</li></ul>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#40ffb9;\">Why Choose Finance Flow?</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#a58fff;\">Intuitive Interface</span><span style=\" font-size:11pt; color:#a58fff;\">: Designed with user experience in mind, Finance Flow makes it easy to navigate and manage your finances without hassle.</span></li>\n"
"<li style=\" font-size:11pt; color:#a58fff;\" style=\" mar"
                        "gin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Comprehensive Tracking</span>: From daily expenses to long-term spending habits, Finance Flow gives you a complete overview of your financial situation.</li>\n"
"<li style=\" font-size:11pt; color:#a58fff;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Visual Insights</span>: Leverage powerful visualizations to quickly grasp your financial status and make proactive decisions.</li></ul>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#40ffb9;\">Version</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margi"
                        "n-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#a58fff;\">Current Version</span><span style=\" font-size:11pt; color:#a58fff;\">: 1.1</span></li></ul>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#40ffb9;\">Developer Information</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#a58fff;\">Finance Flow</span><span style=\" font-size:11pt; color:#a58fff;\"> is developed by </span><span style=\" font-size:11pt; font-weight:700; color:#a58fff;\">Abhishek Verma</span><span style=\" font-size:11pt; color:#a58fff;\">, a BTech graduate and software engineer currently studying in the 4th semester of his BTech program. Abhishek is dedicated to creating practical solut"
                        "ions that simplify everyday tasks and enhance user experience.</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#40ffb9;\">How It Works</span></h2>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; color:#a58fff;\">Data Entry</span><span style=\" font-size:11pt; color:#a58fff;\">: Input your expense data including categories, purposes, and recipients.</span></li>\n"
"<li style=\" font-size:11pt; color:#a58fff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Organize &amp; Analyze</span>: Use the built-in tables to organize your "
                        "entries and add notes for better tracking.</li>\n"
"<li style=\" font-size:11pt; color:#a58fff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Visualize</span>: Review your remaining income and spending patterns through interactive graphs.</li>\n"
"<li style=\" font-size:11pt; color:#a58fff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Manage</span>: Edit, update, or delete entries as needed to keep your records accurate and up-to-date.</li>\n"
"<li style=\" font-size:11pt; color:#a58fff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Calculator</span>: calculate datas easily using keyboard input, just type expressions.</li>\n"
"<li style=\" font-size:11pt; color:#a58fff;\" style=\" margin-top"
                        ":0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Calender</span>: calender is present in the same window.</li></ol>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#40ffb9;\">Support</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#a58fff;\">If you have any questions or need assistance with Finance Flow, please reach out to our support team at support at abhishek639679@gmail.com . We're here to help!</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#40ffb9;\">Feedback</span></h2>\n"
"<p style=\" margin-top:12px; margin-bott"
                        "om:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#a58fff;\">We value your feedback! Share your thoughts or suggestions with us at abhishek639679@gmail.com to help us improve and enhance your experience.</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#40ffb9;\">Connect with Us</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#a58fff;\">Follow us on social media to stay updated on the latest news, updates, and tips related to Finance Flow:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\"><span style=\" font-size:11pt; color:#4affba;\">https://abhi639679.wixsite.com/abhishek</span></li>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:11pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#4affba;\">https://www.instagram.com/abhiiverma007/</span></li></ul>\n"
"<li style=\" font-size:11pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#4affba;\">https://www.linkedin.com/in/abhishek-verma-11729123a/</span></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#a58fff;\">Thank you for choosing Finance Flow. We hope it makes managing your finances as smooth and stress-free as possible!</span><"
                        "/p></body></html>", None))
    # retranslateUi




import json

import numpy as np
import pandas as pd
from pyautogui import screenshot as script
import pyqtgraph as pg
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, QPropertyAnimation, QRect
from PySide6.QtWidgets import QApplication,QVBoxLayout, QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox,QFileDialog

current_date = datetime.now()

# Format the date as "Aug2024_spends"
#file_name = current_date.strftime("%b%Y") + "_spends.csv"


k0 = 0
l0 = 0
y1_income = []

win_width = 860
win_height = 437


filename = current_date.strftime("%b%Y") + "_spends.csv"

file_exists = os.path.isfile(filename)
if not file_exists:
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['spend','for','item','to','reciepent','in','datetime','curr_income'])


filename2 = current_date.strftime("%b%Y") + "_gains.csv"
file_exists2 = os.path.isfile(filename2)
if not file_exists2:
    with open(filename2, mode='w', newline='') as file2:
        writer2 = csv.writer(file2)
        writer2.writerow(['gains','for','item','to','payer','in','datetime','curr_gain'])





data1 = {
            "current_income": '0',
            "total_spends":'0',
            "monthly_income":'0',
            "previous_note": "",
            "total_gains": "0",
            "screen_width":"860",
            "screen_height":"437",
            "others_show":False,
            "others_hide":True,
            "admin_name":'Admin'
        }

filename1 = "settings.json" 
file_exists1 = os.path.isfile(filename1)
if not file_exists1:
        
    with open(filename1, "w") as json_file1:
        json.dump(data1, json_file1, indent=4)



def spend_save(data1):
    global total_spends
   
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
      
            
        writer.writerow(data1)

    df = pd.read_csv(filename)
    total_spends = df['spend'].sum()
    widget.form.label_total_spends.setText(str(total_spends))

def gain_save(data2):
    global total_gains
    
    file_exists2 = os.path.isfile(filename2)

    with open(filename2, mode='a', newline='') as file2:
        writer2 = csv.writer(file2)
      
            
        writer2.writerow(data2)

    df2 = pd.read_csv(filename2)
    total_gains = df2['gains'].sum()
    widget.form.label_total_gains.setText(str(total_gains))


with open("settings.json", "r") as json_file:
    data_json7 = json.load(json_file)

    


class window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_form1()
        self.form.setupUi(self)
        print(os.system('cls'))
        self.resize(int(data_json7['screen_width']),int(data_json7["screen_height"]))
        print('Welcome to the Finance Flow ~')
        #self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.form.tableWidget_1.setColumnWidth(0, 150)
        self.form.tableWidget_1.setColumnWidth(1, 10)
        self.form.tableWidget_1.setColumnWidth(2, 140)
        self.form.tableWidget_1.setColumnWidth(3, 10)
        self.form.tableWidget_1.setColumnWidth(4, 170)
        self.form.tableWidget_1.setColumnWidth(5, 10)
        self.form.tableWidget_1.setColumnWidth(6, 200)

        self.form.tableWidget_2.setColumnWidth(0, 150)
        self.form.tableWidget_2.setColumnWidth(1, 10)
        self.form.tableWidget_2.setColumnWidth(2, 140)
        self.form.tableWidget_2.setColumnWidth(3, 10)
        self.form.tableWidget_2.setColumnWidth(4, 170)
        self.form.tableWidget_2.setColumnWidth(5, 10)
        self.form.tableWidget_2.setColumnWidth(6, 200)
        self.form.label_date.setText(current_date.strftime("Date: %d/%m/%Y"))

        layout = QVBoxLayout()
        self.form.widget_graph.setLayout(layout)
        # Create a PlotWidget

        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)
        self.plot_widget.setBackground((28, 28, 28))


        layout2 = QVBoxLayout()
        self.form.widget_graph_2.setLayout(layout2)
        self.plot_widget2 = pg.PlotWidget()
        layout2.addWidget(self.plot_widget2)
        self.plot_widget2.setBackground((28, 28, 28))

        #self.plot_widget.setLabel('left', 'Expense')  # Y-axis
        #self.plot_widget.setLabel('bottom', 'Days')   # X-axis
        self.form.lineEdit_calc.returnPressed.connect(self.calc)
        #self.graph_plotter(0,0)
        self.form.toolButton_save1.clicked.connect(self.plot_red_bar)
        self.form.toolButton_save2.clicked.connect(self.plot_blue_bar)
        self.form.toolButton_del_row.clicked.connect(self.delete_row)
        self.form.actionSave.triggered.connect(self.save_settings)
        self.form.actionRefresh.triggered.connect(self.refresher)
        self.form.toolButton_set.clicked.connect(self.hider)
        self.form.actionSave_As.triggered.connect(self.save_notes)
        self.form.action_screenshot.triggered.connect(self.snap_save)
        self.form.actionExit.triggered.connect(self.closer)
        self.form.toolButton_del_row_2.clicked.connect(self.delete_row2)
        self.form.toolButton_expand.clicked.connect(self.hider)
        self.form.actionInfo.triggered.connect(self.info)

        self.bars = []
        self.index = 0
        self.bars2 = []
        self.index2 = 0

        self.load_csv1(filename)
        self.load_csv2(filename2)
        self.refresher()
    
    def info(self):
        global k1
        k1 = about_form()
        k1.show()

        
    def hider(self):
        global win_width,win_height

        k_name = self.form.lineEdit_admin_name.text()
        self.form.label_name.setText(k_name)
        
        self.animation = QPropertyAnimation(self, b"geometry")
            # Set the duration of the animation (1000 ms = 1 second)
        self.animation.setDuration(200)

        
        if self.width()>990:

            
            # Set the start and end geometry
            start_geometry = QRect(self.x(), self.y()+30, self.width(), self.height())  # Initial size
            end_geometry = QRect(self.x(), self.y()+30, 860, 716)   # Final size
            #self.resize(860,437)
            win_width,win_height = 860,716
            
            self.save_settings()
        elif self.height()<440 and self.width()<990:

            start_geometry = QRect(self.x(), self.y()+30, self.width(), self.height())  # Initial size
            end_geometry = QRect(self.x(), self.y()+30, 1200, 716)   # Final size
            #self.resize(860,437)
            win_width,win_height = 1200,716
            self.save_settings()
        else:
            start_geometry = QRect(self.x(), self.y()+30, self.width(), self.height())  # Initial size
            end_geometry = QRect(self.x(), self.y()+30, 860, 437)
            #self.resize(1200,716)
            win_width,win_height = 860,437
            self.save_settings()


        self.animation.setStartValue(start_geometry)
        self.animation.setEndValue(end_geometry)
        self.animation.start()

      


    def closer(self):
        QApplication.exit()

    def snap_save(self):
        
        save_path = r'snap\\'
        now1 = datetime.now().strftime('%d%b%y_%H%M')
    
       
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        screenshot = script()
        screenshot.save(os.path.join(save_path, f'{now1}.jpg'))
        
    def save_notes(self):
        html_content = self.form.textEdit_notes.toPlainText()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Text File", "", "TEXT Files (*.txt)")
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(html_content)
                #self.form_notes.label.setText('Html Docs Saved.')
                #QMessageBox.information(self, "Saved", "HTML content saved successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save HTML content: {e}")
                #self.form_notes.label.setText('Html Docs Failed to save.')

    def plotter(self):
        k1 = pd.read_csv(filename)
        y2 = k1['curr_income']

        if len(y2)!=0:
            self.index = y2
            x1 = [p for p in range(len(y2))]
            
    
        
            # Plotting the bar
            bar = pg.BarGraphItem(x=x1, height=y2, width=0.6, brush=QColor(255, 170, 0))
            self.plot_widget.addItem(bar)
            #self.bars.append(bar)


        k2 = pd.read_csv(filename2)
        y3 = k2['curr_gain']

        if len(y3)!=0:
            self.index2 = y3
            x2 = [p2 for p2 in range(len(y3))]
            
    
        
            # Plotting the bar
            bar2 = pg.BarGraphItem(x=x2, height=y3, width=0.6, brush=QColor(98, 255, 156))
            self.plot_widget2.addItem(bar2)
            #self.bars.append(bar)


    def refresher(self):
        global current_income,total_spends,win_width,win_height
        #global data_json
        
      
        with open("settings.json", "r") as json_file:
            data_json = json.load(json_file) 

        self.form.lineEdit_income.setText(data_json['current_income'])
        self.form.label_total_spends.setText(data_json['total_spends'])
        self.form.lineEdit_income0.setText(data_json['monthly_income'])
        self.form.textEdit_notes.setText(data_json['previous_note'])
        self.form.label_total_gains.setText(data_json['total_gains'])

        self.form.label_income.setText(data_json['monthly_income'])
        self.form.label_expense.setText(data_json['total_spends'])
        self.form.label_savings.setText(str(int(data_json['current_income'])-int(data_json['total_spends'])))
        self.form.label_gains.setText(data_json['total_gains'])
        self.form.label_name.setText(data_json["admin_name"])
        

        current_income = self.form.lineEdit_income.text()
        total_spends = data_json['total_spends']

        win_width = int(data_json['screen_width'])
        win_height = int(data_json['screen_height'])

        self.form.lineEdit_spend.setVisible(data_json['others_show'])
        self.form.lineEdit_item.setVisible(data_json['others_show'])
        self.form.lineEdit_reciepent.setVisible(data_json['others_show'])
        self.form.widget_5.setVisible(data_json['others_show'])
        self.form.toolButton_expand.setVisible(data_json['others_show'])
        
        self.form.label_image.setVisible(data_json['others_hide'])
        self.form.toolButton_set.setVisible(data_json['others_hide'])
        self.form.label_profile.setVisible(data_json['others_hide'])
        self.form.lineEdit_admin_name.setVisible(data_json['others_hide'])
        self.form.label_trans.setVisible(data_json['others_hide'])
        

        if data_json['others_hide']==False:
            self.form.toolButton_expand.move(694,4)


        self.plotter()

    def save_settings(self):

        data = {
        
            "current_income": str(self.form.lineEdit_income.text()),
            "total_spends": str(self.form.label_total_spends.text()),
            "monthly_income":str(self.form.lineEdit_income0.text()),
            "previous_note": str(self.form.textEdit_notes.toPlainText()),
            "total_gains": str(self.form.label_total_gains.text()),
            "screen_width": win_width,
            "screen_height": win_height,
            "others_show":True,
            "others_hide":False,
            "admin_name":str(self.form.label_name.text())
           
        }

        # Saving the dictionary as a JSON file
        with open("settings.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Data saved to data.json")
        self.refresher()

    def delete_row_from_csv(self, index1):
        file_path = filename
        index_from_end = index1+1
        # Read the content of the CSV file into a list
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Calculate the actual index from the start
        row_index = len(rows) - index_from_end

        # Check if the row index is valid
        if row_index < 1 or row_index >= len(rows):
            QMessageBox.warning(self, "No Selection", "Please select a Valid row to delete.")
            return

        item10 = self.form.tableWidget_1.item(index1, 0) 
    
        currincome = int(self.form.lineEdit_income.text())
        item_val = int(item10.text())
        new_income = currincome + item_val

        self.form.lineEdit_income.setText(str(new_income))
        # Delete the row at the calculated index
        del rows[row_index]

        # Write the modified rows back to the CSV file
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        #print(f"Row {index_from_end} from the end deleted successfully.")
      
        self.save_settings()

        

    def delete_row(self):
        # Get the selected row
        selected_row = self.form.tableWidget_1.currentRow()
       
        if selected_row >-1:  # -1 means no selection
            # Confirm the deletion
            reply = QMessageBox.question(self, 'Delete Row', 
                                         "Are you sure you want to delete the selected row?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Remove the selected row
                
                self.delete_row_from_csv(selected_row)
                self.form.tableWidget_1.removeRow(selected_row)
        else:
            QMessageBox.warning(self, "No Selection", "Please select a row to delete.")

    #---------------------------------------------------------------------------
    def delete_row_from_csv2(self, index2):
        file_path2 = filename2
        index_from_end2 = index2+1
        # Read the content of the CSV file into a list
        with open(file_path2, 'r', newline='') as file2:
            reader2 = csv.reader(file2)
            rows2 = list(reader2)

        # Calculate the actual index from the start
        row_index2 = len(rows2) - index_from_end2

        # Check if the row index is valid
        if row_index2 < 1 or row_index2 >= len(rows2):
            QMessageBox.warning(self, "No Selection", "Please select a Valid row to delete.")
            return

        item12 = self.form.tableWidget_2.item(index2, 0) 
    
        currincome2 = int(self.form.lineEdit_income.text())
        item_val2 = int(item12.text())
        new_income2 = currincome2 + item_val2

        #self.form.lineEdit_income.setText(str(new_income2))
        # Delete the row at the calculated index
        del rows2[row_index2]

        # Write the modified rows back to the CSV file
        with open(file_path2, 'w', newline='') as file2:
            writer2 = csv.writer(file2)
            writer2.writerows(rows2)

        #print(f"Row {index_from_end2} from the end deleted successfully.")
      
        self.save_settings()


    def delete_row2(self):
        # Get the selected row
        selected_row2 = self.form.tableWidget_2.currentRow()
       
        if selected_row2 >-1:  # -1 means no selection
            # Confirm the deletion
            reply2 = QMessageBox.question(self, 'Delete Row', 
                                         "Are you sure you want to delete the selected row?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply2 == QMessageBox.Yes:
                # Remove the selected row
                
                self.delete_row_from_csv2(selected_row2)
                self.form.tableWidget_2.removeRow(selected_row2)
        else:
            QMessageBox.warning(self, "No Selection", "Please select a row to delete.")



    def load_csv1(self, file_path):
        # Read the CSV file in reverse order
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = list(csv.reader(csvfile))
            reader.reverse()  # Reverse the order of rows

            # Set the number of rows and columns
            self.form.tableWidget_1.setRowCount(len(reader))
            self.form.tableWidget_1.setColumnCount(len(reader[0])-1)

            # Populate QTableWidget with data
            for row_index, row_data in enumerate(reader):
                for column_index, cell_data in enumerate(row_data):
                    self.form.tableWidget_1.setItem(row_index, column_index, QTableWidgetItem(cell_data))
    
    def load_csv2(self, file_path2):
        # Read the CSV file in reverse order
        with open(file_path2, newline='', encoding='utf-8') as csvfile2:
            reader2 = list(csv.reader(csvfile2))
            reader2.reverse()  # Reverse the order of rows

            # Set the number of rows and columns
            self.form.tableWidget_2.setRowCount(len(reader2))
            self.form.tableWidget_2.setColumnCount(len(reader2[0])-1)

            # Populate QTableWidget with data
            for row_index2, row_data2 in enumerate(reader2):
                for column_index2, cell_data2 in enumerate(row_data2):
                    self.form.tableWidget_2.setItem(row_index2, column_index2, QTableWidgetItem(cell_data2))

    def calc(self):
        # Get the text from the line edit
        expression = self.form.lineEdit_calc.text()
        self.form.label_calc.setText(expression+' = ')
        try:
            # Evaluate the expression and display the result
            result = eval(expression)
            self.form.lineEdit_calc.setText(str(result))
        except Exception as e:
            self.form.lineEdit_calc.setText("Error: " + str(e))
    
    def plot_red_bar(self):
        global current_income
        self.form.tabWidget_2.setCurrentIndex(0)
        money = self.form.lineEdit_spend.text()
        remain1 = int(current_income)-int(money)
        
        y1_income.append(int(remain1))
        self.form.lineEdit_income.setText(str(remain1))
        current_income = remain1
        
        self.data_saver1()


    def plot_blue_bar(self):

        global current_income

        self.form.tabWidget_2.setCurrentIndex(1)
        money2 = self.form.lineEdit_get.text()
        remain2 = int(current_income)+int(money2)
        
        y1_income.append(int(remain2))
        self.form.lineEdit_income.setText(str(remain2))
        current_income = remain2
        
        self.data_saver2()

    def plot_bar(self, color,mon):
        x = [self.index]  # X position for the bar
        height = [mon]  # Height of the bar
        
        # Plotting the bar
        bar = pg.BarGraphItem(x=x, height=height, width=0.6, brush=color)
        self.plot_widget.addItem(bar)
        self.bars.append(bar)
        
        
        # Update the index for the next bar
        self.index += 1


    '''def graph_plotter(self,money,col):
        global y1_income,monthly_income
     

        remain1 = int(monthly_income)-int(money)
        
        y1_income.append(int(remain1))
        self.form.lineEdit_income.setText(str(remain1))
        monthly_income = remain1

        print(monthly_income)
        if len(y1_income)<=7:

            y = y1_income+[0 for ar in range(7-len(y1_income))]
            x = np.arange(1,8)
            # Set the bar color to rgb(107, 139, 255)
            
            # Create a bar graph item with the specified color
            if col==0:

                bg = pg.BarGraphItem(x=x, height=y, width=0.6, brush='r')
                
            else:
                bg = pg.BarGraphItem(x=x, height=y, width=0.6, brush='b')

            self.plot_widget.addItem(bg)
        else:
            y = y1_income
            x = np.arange(len(y))
            # Set the bar color to rgb(107, 139, 255)
            
            # Create a bar graph item with the specified color
            if col==0:

                bg = pg.BarGraphItem(x=x, height=y, width=0.6, brush=QColor(107, 139, 255))
            else:
                bg = pg.BarGraphItem(x=x, height=y, width=0.6, brush=QColor(0, 255, 0))

            self.plot_widget.addItem(bg)'''





    def data_saver1(self):
        global k0
        
        a1 = self.form.lineEdit_spend.text()
        a2 = self.form.lineEdit_item.text()
        a3 = self.form.lineEdit_reciepent.text()
        a5 = self.form.lineEdit_income.text()



        now = datetime.now()
        a4 = now.strftime("%d/%m/%Y %#I:%M%p")

        self.form.tableWidget_1.insertRow(0)

        self.form.tableWidget_1.setItem(0, 0, QTableWidgetItem(a1))
        self.form.tableWidget_1.setItem(0, 2, QTableWidgetItem(a2))
        self.form.tableWidget_1.setItem(0, 4, QTableWidgetItem(a3))
        self.form.tableWidget_1.setItem(0, 6, QTableWidgetItem(a4))
        k0+=1
        #self.graph_plotter(a1,0)

        spend_save(data1=[a1,' ',a2,' ',a3,' ',a4,a5],)

        self.save_settings()


    def data_saver2(self):
        global l0
        b1 = self.form.lineEdit_get.text()
        b2 = self.form.lineEdit_for_what.text()
        b3 = self.form.lineEdit_giver.text()

        b5 = self.form.label_total_gains.text()
        now1 = datetime.now()
        b4 = now1.strftime("%d/%m/%Y %#I:%M%p")

        self.form.tableWidget_2.insertRow(0)

        self.form.tableWidget_2.setItem(0, 0, QTableWidgetItem(b1))
        self.form.tableWidget_2.setItem(0, 2, QTableWidgetItem(b2))
        self.form.tableWidget_2.setItem(0, 4, QTableWidgetItem(b3))
        self.form.tableWidget_2.setItem(0, 6, QTableWidgetItem(b4))
        l0+=1
        #self.graph_plotter(-int(b1),1)

        gain_save(data2=[b1,' ',b2,' ',b3,' ',b4,b5],)

        self.save_settings()
       


class about_form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_about()
        self.form.setupUi(self)
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    widget = window()
    widget.show()

    
    sys.exit(app.exec())