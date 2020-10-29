# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AVR_PortConfig_Final.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import sys
import re
import os

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(784, 498)
        Form.setLayoutDirection(Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QRect(260, 18, 91, 51))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50);
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(400, 18, 91, 51))
        font1 = QFont()
        font1.setPointSize(8)
        self.pushButton_2.setFont(font1)
        self.DIOgroupBox = QGroupBox(Form)
        self.DIOgroupBox.setObjectName(u"DIOgroupBox")
        self.DIOgroupBox.setGeometry(QRect(10, 70, 761, 421))
        self.DIOgroupBox.setVisible(False)
        self.pushButton = QPushButton(self.DIOgroupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(590, 350, 101, 61))
        self.textEdit = QTextEdit(self.DIOgroupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QRect(40, 287, 301, 71))
        self.tabWidget = QTabWidget(self.DIOgroupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 30, 771, 241))
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setContextMenuPolicy(Qt.PreventContextMenu)
        self.tabWidget.setTabBarAutoHide(False)
        self.PORTA_tab_2 = QWidget()
        self.PORTA_tab_2.setObjectName(u"PORTA_tab_2")
        self.PORTA_groupBox_2 = QGroupBox(self.PORTA_tab_2)
        self.PORTA_groupBox_2.setObjectName(u"PORTA_groupBox_2")
        self.PORTA_groupBox_2.setEnabled(True)
        self.PORTA_groupBox_2.setGeometry(QRect(10, 10, 741, 191))
        self.PORTA_groupBox_2.setCheckable(False)
        self.PORTA_groupBox_2.setChecked(False)
        self.All_Output_Init0_pushButton_18 = QPushButton(self.PORTA_groupBox_2)
        self.All_Output_Init0_pushButton_18.setObjectName(u"All_Output_Init0_pushButton_18")
        self.All_Output_Init0_pushButton_18.setGeometry(QRect(120, 160, 111, 18))
        self.All_Output_Init1_pushButton_18 = QPushButton(self.PORTA_groupBox_2)
        self.All_Output_Init1_pushButton_18.setObjectName(u"All_Output_Init1_pushButton_18")
        self.All_Output_Init1_pushButton_18.setGeometry(QRect(250, 160, 111, 18))
        self.All_Input_Init0_pushButton_18 = QPushButton(self.PORTA_groupBox_2)
        self.All_Input_Init0_pushButton_18.setObjectName(u"All_Input_Init0_pushButton_18")
        self.All_Input_Init0_pushButton_18.setGeometry(QRect(380, 160, 111, 18))
        self.All_Input_Init1_pushButton_18 = QPushButton(self.PORTA_groupBox_2)
        self.All_Input_Init1_pushButton_18.setObjectName(u"All_Input_Init1_pushButton_18")
        self.All_Input_Init1_pushButton_18.setGeometry(QRect(510, 160, 111, 18))
        self.PIN1_groupBox_18 = QGroupBox(self.PORTA_groupBox_2)
        self.PIN1_groupBox_18.setObjectName(u"PIN1_groupBox_18")
        self.PIN1_groupBox_18.setGeometry(QRect(100, 20, 91, 131))
        self.Output_init1_PIN1_radioButton_18 = QRadioButton(self.PIN1_groupBox_18)
        self.Output_init1_PIN1_radioButton_18.setObjectName(u"Output_init1_PIN1_radioButton_18")
        self.Output_init1_PIN1_radioButton_18.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN1_radioButton_18 = QRadioButton(self.PIN1_groupBox_18)
        self.Input_init0_PIN1_radioButton_18.setObjectName(u"Input_init0_PIN1_radioButton_18")
        self.Input_init0_PIN1_radioButton_18.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN1_radioButton_18 = QRadioButton(self.PIN1_groupBox_18)
        self.Input_init1_PIN1_radioButton_18.setObjectName(u"Input_init1_PIN1_radioButton_18")
        self.Input_init1_PIN1_radioButton_18.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN1_radioButton_18 = QRadioButton(self.PIN1_groupBox_18)
        self.Output_init0_PIN1_radioButton_18.setObjectName(u"Output_init0_PIN1_radioButton_18")
        self.Output_init0_PIN1_radioButton_18.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN1_radioButton_18.setChecked(True)
        self.PIN0_groupBox_17 = QGroupBox(self.PORTA_groupBox_2)
        self.PIN0_groupBox_17.setObjectName(u"PIN0_groupBox_17")
        self.PIN0_groupBox_17.setGeometry(QRect(10, 20, 91, 131))
        self.Output_init1_PIN0_radioButton_18 = QRadioButton(self.PIN0_groupBox_17)
        self.Output_init1_PIN0_radioButton_18.setObjectName(u"Output_init1_PIN0_radioButton_18")
        self.Output_init1_PIN0_radioButton_18.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN0_radioButton_18 = QRadioButton(self.PIN0_groupBox_17)
        self.Input_init0_PIN0_radioButton_18.setObjectName(u"Input_init0_PIN0_radioButton_18")
        self.Input_init0_PIN0_radioButton_18.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN0_radioButton_19 = QRadioButton(self.PIN0_groupBox_17)
        self.Input_init1_PIN0_radioButton_19.setObjectName(u"Input_init1_PIN0_radioButton_19")
        self.Input_init1_PIN0_radioButton_19.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN0_radioButton_18 = QRadioButton(self.PIN0_groupBox_17)
        self.Output_init0_PIN0_radioButton_18.setObjectName(u"Output_init0_PIN0_radioButton_18")
        self.Output_init0_PIN0_radioButton_18.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN0_radioButton_18.setChecked(True)
        self.PIN4_groupBox_17 = QGroupBox(self.PORTA_groupBox_2)
        self.PIN4_groupBox_17.setObjectName(u"PIN4_groupBox_17")
        self.PIN4_groupBox_17.setGeometry(QRect(370, 20, 91, 131))
        self.Output_init1_PIN4_radioButton_17 = QRadioButton(self.PIN4_groupBox_17)
        self.Output_init1_PIN4_radioButton_17.setObjectName(u"Output_init1_PIN4_radioButton_17")
        self.Output_init1_PIN4_radioButton_17.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN4_radioButton_17 = QRadioButton(self.PIN4_groupBox_17)
        self.Input_init0_PIN4_radioButton_17.setObjectName(u"Input_init0_PIN4_radioButton_17")
        self.Input_init0_PIN4_radioButton_17.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN4_radioButton_17 = QRadioButton(self.PIN4_groupBox_17)
        self.Input_init1_PIN4_radioButton_17.setObjectName(u"Input_init1_PIN4_radioButton_17")
        self.Input_init1_PIN4_radioButton_17.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN4_radioButton_17 = QRadioButton(self.PIN4_groupBox_17)
        self.Output_init0_PIN4_radioButton_17.setObjectName(u"Output_init0_PIN4_radioButton_17")
        self.Output_init0_PIN4_radioButton_17.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN4_radioButton_17.setChecked(True)
        self.PIN2_groupBox_17 = QGroupBox(self.PORTA_groupBox_2)
        self.PIN2_groupBox_17.setObjectName(u"PIN2_groupBox_17")
        self.PIN2_groupBox_17.setGeometry(QRect(190, 20, 91, 131))
        self.Output_init1_PIN2_radioButton_17 = QRadioButton(self.PIN2_groupBox_17)
        self.Output_init1_PIN2_radioButton_17.setObjectName(u"Output_init1_PIN2_radioButton_17")
        self.Output_init1_PIN2_radioButton_17.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN2_radioButton_17 = QRadioButton(self.PIN2_groupBox_17)
        self.Input_init0_PIN2_radioButton_17.setObjectName(u"Input_init0_PIN2_radioButton_17")
        self.Input_init0_PIN2_radioButton_17.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN2_radioButton_17 = QRadioButton(self.PIN2_groupBox_17)
        self.Input_init1_PIN2_radioButton_17.setObjectName(u"Input_init1_PIN2_radioButton_17")
        self.Input_init1_PIN2_radioButton_17.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN2_radioButton_17 = QRadioButton(self.PIN2_groupBox_17)
        self.Output_init0_PIN2_radioButton_17.setObjectName(u"Output_init0_PIN2_radioButton_17")
        self.Output_init0_PIN2_radioButton_17.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN2_radioButton_17.setChecked(True)
        self.PIN5_groupBox_17 = QGroupBox(self.PORTA_groupBox_2)
        self.PIN5_groupBox_17.setObjectName(u"PIN5_groupBox_17")
        self.PIN5_groupBox_17.setGeometry(QRect(460, 20, 91, 131))
        self.Output_init1_PIN5_radioButton_17 = QRadioButton(self.PIN5_groupBox_17)
        self.Output_init1_PIN5_radioButton_17.setObjectName(u"Output_init1_PIN5_radioButton_17")
        self.Output_init1_PIN5_radioButton_17.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN5_radioButton_17 = QRadioButton(self.PIN5_groupBox_17)
        self.Input_init0_PIN5_radioButton_17.setObjectName(u"Input_init0_PIN5_radioButton_17")
        self.Input_init0_PIN5_radioButton_17.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN5_radioButton_17 = QRadioButton(self.PIN5_groupBox_17)
        self.Input_init1_PIN5_radioButton_17.setObjectName(u"Input_init1_PIN5_radioButton_17")
        self.Input_init1_PIN5_radioButton_17.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN5_radioButton_17 = QRadioButton(self.PIN5_groupBox_17)
        self.Output_init0_PIN5_radioButton_17.setObjectName(u"Output_init0_PIN5_radioButton_17")
        self.Output_init0_PIN5_radioButton_17.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN5_radioButton_17.setChecked(True)
        self.PIN7_groupBox_17 = QGroupBox(self.PORTA_groupBox_2)
        self.PIN7_groupBox_17.setObjectName(u"PIN7_groupBox_17")
        self.PIN7_groupBox_17.setGeometry(QRect(640, 20, 91, 131))
        self.Output_init1_PIN7_radioButton_17 = QRadioButton(self.PIN7_groupBox_17)
        self.Output_init1_PIN7_radioButton_17.setObjectName(u"Output_init1_PIN7_radioButton_17")
        self.Output_init1_PIN7_radioButton_17.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN7_radioButton_17 = QRadioButton(self.PIN7_groupBox_17)
        self.Input_init0_PIN7_radioButton_17.setObjectName(u"Input_init0_PIN7_radioButton_17")
        self.Input_init0_PIN7_radioButton_17.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN7_radioButton_17 = QRadioButton(self.PIN7_groupBox_17)
        self.Input_init1_PIN7_radioButton_17.setObjectName(u"Input_init1_PIN7_radioButton_17")
        self.Input_init1_PIN7_radioButton_17.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN7_radioButton_17 = QRadioButton(self.PIN7_groupBox_17)
        self.Output_init0_PIN7_radioButton_17.setObjectName(u"Output_init0_PIN7_radioButton_17")
        self.Output_init0_PIN7_radioButton_17.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN7_radioButton_17.setChecked(True)
        self.PIN6_groupBox_17 = QGroupBox(self.PORTA_groupBox_2)
        self.PIN6_groupBox_17.setObjectName(u"PIN6_groupBox_17")
        self.PIN6_groupBox_17.setGeometry(QRect(550, 20, 91, 131))
        self.Output_init1_PIN6_radioButton_17 = QRadioButton(self.PIN6_groupBox_17)
        self.Output_init1_PIN6_radioButton_17.setObjectName(u"Output_init1_PIN6_radioButton_17")
        self.Output_init1_PIN6_radioButton_17.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN6_radioButton_17 = QRadioButton(self.PIN6_groupBox_17)
        self.Input_init0_PIN6_radioButton_17.setObjectName(u"Input_init0_PIN6_radioButton_17")
        self.Input_init0_PIN6_radioButton_17.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN6_radioButton_17 = QRadioButton(self.PIN6_groupBox_17)
        self.Input_init1_PIN6_radioButton_17.setObjectName(u"Input_init1_PIN6_radioButton_17")
        self.Input_init1_PIN6_radioButton_17.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN6_radioButton_17 = QRadioButton(self.PIN6_groupBox_17)
        self.Output_init0_PIN6_radioButton_17.setObjectName(u"Output_init0_PIN6_radioButton_17")
        self.Output_init0_PIN6_radioButton_17.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN6_radioButton_17.setChecked(True)
        self.PIN3_groupBox_17 = QGroupBox(self.PORTA_groupBox_2)
        self.PIN3_groupBox_17.setObjectName(u"PIN3_groupBox_17")
        self.PIN3_groupBox_17.setGeometry(QRect(280, 20, 91, 131))
        self.Output_init1_PIN3_radioButton_17 = QRadioButton(self.PIN3_groupBox_17)
        self.Output_init1_PIN3_radioButton_17.setObjectName(u"Output_init1_PIN3_radioButton_17")
        self.Output_init1_PIN3_radioButton_17.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN3_radioButton_17 = QRadioButton(self.PIN3_groupBox_17)
        self.Input_init0_PIN3_radioButton_17.setObjectName(u"Input_init0_PIN3_radioButton_17")
        self.Input_init0_PIN3_radioButton_17.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN3_radioButton_17 = QRadioButton(self.PIN3_groupBox_17)
        self.Input_init1_PIN3_radioButton_17.setObjectName(u"Input_init1_PIN3_radioButton_17")
        self.Input_init1_PIN3_radioButton_17.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN3_radioButton_17 = QRadioButton(self.PIN3_groupBox_17)
        self.Output_init0_PIN3_radioButton_17.setObjectName(u"Output_init0_PIN3_radioButton_17")
        self.Output_init0_PIN3_radioButton_17.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN3_radioButton_17.setChecked(True)
        self.tabWidget.addTab(self.PORTA_tab_2, "PORTA")
        self.PORTB_tab_2 = QWidget()
        self.PORTB_tab_2.setObjectName(u"PORTB_tab_2")
        self.PORTB_groupBox_2 = QGroupBox(self.PORTB_tab_2)
        self.PORTB_groupBox_2.setObjectName(u"PORTB_groupBox_2")
        self.PORTB_groupBox_2.setEnabled(True)
        self.PORTB_groupBox_2.setGeometry(QRect(10, 10, 741, 191))
        self.All_Output_Init0_pushButton_19 = QPushButton(self.PORTB_groupBox_2)
        self.All_Output_Init0_pushButton_19.setObjectName(u"All_Output_Init0_pushButton_19")
        self.All_Output_Init0_pushButton_19.setGeometry(QRect(120, 160, 111, 18))
        self.All_Output_Init1_pushButton_19 = QPushButton(self.PORTB_groupBox_2)
        self.All_Output_Init1_pushButton_19.setObjectName(u"All_Output_Init1_pushButton_19")
        self.All_Output_Init1_pushButton_19.setGeometry(QRect(250, 160, 111, 18))
        self.All_Input_Init0_pushButton_19 = QPushButton(self.PORTB_groupBox_2)
        self.All_Input_Init0_pushButton_19.setObjectName(u"All_Input_Init0_pushButton_19")
        self.All_Input_Init0_pushButton_19.setGeometry(QRect(380, 160, 111, 18))
        self.All_Input_Init1_pushButton_19 = QPushButton(self.PORTB_groupBox_2)
        self.All_Input_Init1_pushButton_19.setObjectName(u"All_Input_Init1_pushButton_19")
        self.All_Input_Init1_pushButton_19.setGeometry(QRect(510, 160, 111, 18))
        self.PIN1_groupBox_19 = QGroupBox(self.PORTB_groupBox_2)
        self.PIN1_groupBox_19.setObjectName(u"PIN1_groupBox_19")
        self.PIN1_groupBox_19.setGeometry(QRect(100, 20, 91, 131))
        self.Output_init1_PIN1_radioButton_19 = QRadioButton(self.PIN1_groupBox_19)
        self.Output_init1_PIN1_radioButton_19.setObjectName(u"Output_init1_PIN1_radioButton_19")
        self.Output_init1_PIN1_radioButton_19.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN1_radioButton_19 = QRadioButton(self.PIN1_groupBox_19)
        self.Input_init0_PIN1_radioButton_19.setObjectName(u"Input_init0_PIN1_radioButton_19")
        self.Input_init0_PIN1_radioButton_19.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN1_radioButton_19 = QRadioButton(self.PIN1_groupBox_19)
        self.Input_init1_PIN1_radioButton_19.setObjectName(u"Input_init1_PIN1_radioButton_19")
        self.Input_init1_PIN1_radioButton_19.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN1_radioButton_19 = QRadioButton(self.PIN1_groupBox_19)
        self.Output_init0_PIN1_radioButton_19.setObjectName(u"Output_init0_PIN1_radioButton_19")
        self.Output_init0_PIN1_radioButton_19.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN1_radioButton_19.setChecked(True)
        self.PIN0_groupBox_18 = QGroupBox(self.PORTB_groupBox_2)
        self.PIN0_groupBox_18.setObjectName(u"PIN0_groupBox_18")
        self.PIN0_groupBox_18.setGeometry(QRect(10, 20, 91, 131))
        self.Output_init1_PIN0_radioButton_19 = QRadioButton(self.PIN0_groupBox_18)
        self.Output_init1_PIN0_radioButton_19.setObjectName(u"Output_init1_PIN0_radioButton_19")
        self.Output_init1_PIN0_radioButton_19.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN0_radioButton_19 = QRadioButton(self.PIN0_groupBox_18)
        self.Input_init0_PIN0_radioButton_19.setObjectName(u"Input_init0_PIN0_radioButton_19")
        self.Input_init0_PIN0_radioButton_19.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN0_radioButton_20 = QRadioButton(self.PIN0_groupBox_18)
        self.Input_init1_PIN0_radioButton_20.setObjectName(u"Input_init1_PIN0_radioButton_20")
        self.Input_init1_PIN0_radioButton_20.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN0_radioButton_19 = QRadioButton(self.PIN0_groupBox_18)
        self.Output_init0_PIN0_radioButton_19.setObjectName(u"Output_init0_PIN0_radioButton_19")
        self.Output_init0_PIN0_radioButton_19.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN0_radioButton_19.setChecked(True)
        self.PIN4_groupBox_18 = QGroupBox(self.PORTB_groupBox_2)
        self.PIN4_groupBox_18.setObjectName(u"PIN4_groupBox_18")
        self.PIN4_groupBox_18.setGeometry(QRect(370, 20, 91, 131))
        self.Output_init1_PIN4_radioButton_18 = QRadioButton(self.PIN4_groupBox_18)
        self.Output_init1_PIN4_radioButton_18.setObjectName(u"Output_init1_PIN4_radioButton_18")
        self.Output_init1_PIN4_radioButton_18.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN4_radioButton_18 = QRadioButton(self.PIN4_groupBox_18)
        self.Input_init0_PIN4_radioButton_18.setObjectName(u"Input_init0_PIN4_radioButton_18")
        self.Input_init0_PIN4_radioButton_18.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN4_radioButton_18 = QRadioButton(self.PIN4_groupBox_18)
        self.Input_init1_PIN4_radioButton_18.setObjectName(u"Input_init1_PIN4_radioButton_18")
        self.Input_init1_PIN4_radioButton_18.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN4_radioButton_18 = QRadioButton(self.PIN4_groupBox_18)
        self.Output_init0_PIN4_radioButton_18.setObjectName(u"Output_init0_PIN4_radioButton_18")
        self.Output_init0_PIN4_radioButton_18.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN4_radioButton_18.setChecked(True)
        self.PIN2_groupBox_18 = QGroupBox(self.PORTB_groupBox_2)
        self.PIN2_groupBox_18.setObjectName(u"PIN2_groupBox_18")
        self.PIN2_groupBox_18.setGeometry(QRect(190, 20, 91, 131))
        self.Output_init1_PIN2_radioButton_18 = QRadioButton(self.PIN2_groupBox_18)
        self.Output_init1_PIN2_radioButton_18.setObjectName(u"Output_init1_PIN2_radioButton_18")
        self.Output_init1_PIN2_radioButton_18.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN2_radioButton_18 = QRadioButton(self.PIN2_groupBox_18)
        self.Input_init0_PIN2_radioButton_18.setObjectName(u"Input_init0_PIN2_radioButton_18")
        self.Input_init0_PIN2_radioButton_18.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN2_radioButton_18 = QRadioButton(self.PIN2_groupBox_18)
        self.Input_init1_PIN2_radioButton_18.setObjectName(u"Input_init1_PIN2_radioButton_18")
        self.Input_init1_PIN2_radioButton_18.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN2_radioButton_18 = QRadioButton(self.PIN2_groupBox_18)
        self.Output_init0_PIN2_radioButton_18.setObjectName(u"Output_init0_PIN2_radioButton_18")
        self.Output_init0_PIN2_radioButton_18.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN2_radioButton_18.setChecked(True)
        self.PIN5_groupBox_18 = QGroupBox(self.PORTB_groupBox_2)
        self.PIN5_groupBox_18.setObjectName(u"PIN5_groupBox_18")
        self.PIN5_groupBox_18.setGeometry(QRect(460, 20, 91, 131))
        self.Output_init1_PIN5_radioButton_18 = QRadioButton(self.PIN5_groupBox_18)
        self.Output_init1_PIN5_radioButton_18.setObjectName(u"Output_init1_PIN5_radioButton_18")
        self.Output_init1_PIN5_radioButton_18.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN5_radioButton_18 = QRadioButton(self.PIN5_groupBox_18)
        self.Input_init0_PIN5_radioButton_18.setObjectName(u"Input_init0_PIN5_radioButton_18")
        self.Input_init0_PIN5_radioButton_18.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN5_radioButton_18 = QRadioButton(self.PIN5_groupBox_18)
        self.Input_init1_PIN5_radioButton_18.setObjectName(u"Input_init1_PIN5_radioButton_18")
        self.Input_init1_PIN5_radioButton_18.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN5_radioButton_18 = QRadioButton(self.PIN5_groupBox_18)
        self.Output_init0_PIN5_radioButton_18.setObjectName(u"Output_init0_PIN5_radioButton_18")
        self.Output_init0_PIN5_radioButton_18.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN5_radioButton_18.setChecked(True)
        self.PIN7_groupBox_18 = QGroupBox(self.PORTB_groupBox_2)
        self.PIN7_groupBox_18.setObjectName(u"PIN7_groupBox_18")
        self.PIN7_groupBox_18.setGeometry(QRect(640, 20, 91, 131))
        self.Output_init1_PIN7_radioButton_18 = QRadioButton(self.PIN7_groupBox_18)
        self.Output_init1_PIN7_radioButton_18.setObjectName(u"Output_init1_PIN7_radioButton_18")
        self.Output_init1_PIN7_radioButton_18.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN7_radioButton_18 = QRadioButton(self.PIN7_groupBox_18)
        self.Input_init0_PIN7_radioButton_18.setObjectName(u"Input_init0_PIN7_radioButton_18")
        self.Input_init0_PIN7_radioButton_18.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN7_radioButton_18 = QRadioButton(self.PIN7_groupBox_18)
        self.Input_init1_PIN7_radioButton_18.setObjectName(u"Input_init1_PIN7_radioButton_18")
        self.Input_init1_PIN7_radioButton_18.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN7_radioButton_18 = QRadioButton(self.PIN7_groupBox_18)
        self.Output_init0_PIN7_radioButton_18.setObjectName(u"Output_init0_PIN7_radioButton_18")
        self.Output_init0_PIN7_radioButton_18.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN7_radioButton_18.setChecked(True)
        self.PIN6_groupBox_18 = QGroupBox(self.PORTB_groupBox_2)
        self.PIN6_groupBox_18.setObjectName(u"PIN6_groupBox_18")
        self.PIN6_groupBox_18.setGeometry(QRect(550, 20, 91, 131))
        self.Output_init1_PIN6_radioButton_18 = QRadioButton(self.PIN6_groupBox_18)
        self.Output_init1_PIN6_radioButton_18.setObjectName(u"Output_init1_PIN6_radioButton_18")
        self.Output_init1_PIN6_radioButton_18.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN6_radioButton_18 = QRadioButton(self.PIN6_groupBox_18)
        self.Input_init0_PIN6_radioButton_18.setObjectName(u"Input_init0_PIN6_radioButton_18")
        self.Input_init0_PIN6_radioButton_18.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN6_radioButton_18 = QRadioButton(self.PIN6_groupBox_18)
        self.Input_init1_PIN6_radioButton_18.setObjectName(u"Input_init1_PIN6_radioButton_18")
        self.Input_init1_PIN6_radioButton_18.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN6_radioButton_18 = QRadioButton(self.PIN6_groupBox_18)
        self.Output_init0_PIN6_radioButton_18.setObjectName(u"Output_init0_PIN6_radioButton_18")
        self.Output_init0_PIN6_radioButton_18.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN6_radioButton_18.setChecked(True)
        self.PIN3_groupBox_18 = QGroupBox(self.PORTB_groupBox_2)
        self.PIN3_groupBox_18.setObjectName(u"PIN3_groupBox_18")
        self.PIN3_groupBox_18.setGeometry(QRect(280, 20, 91, 131))
        self.Output_init1_PIN3_radioButton_18 = QRadioButton(self.PIN3_groupBox_18)
        self.Output_init1_PIN3_radioButton_18.setObjectName(u"Output_init1_PIN3_radioButton_18")
        self.Output_init1_PIN3_radioButton_18.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN3_radioButton_18 = QRadioButton(self.PIN3_groupBox_18)
        self.Input_init0_PIN3_radioButton_18.setObjectName(u"Input_init0_PIN3_radioButton_18")
        self.Input_init0_PIN3_radioButton_18.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN3_radioButton_18 = QRadioButton(self.PIN3_groupBox_18)
        self.Input_init1_PIN3_radioButton_18.setObjectName(u"Input_init1_PIN3_radioButton_18")
        self.Input_init1_PIN3_radioButton_18.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN3_radioButton_18 = QRadioButton(self.PIN3_groupBox_18)
        self.Output_init0_PIN3_radioButton_18.setObjectName(u"Output_init0_PIN3_radioButton_18")
        self.Output_init0_PIN3_radioButton_18.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN3_radioButton_18.setChecked(True)
        self.tabWidget.addTab(self.PORTB_tab_2, "PORTB")
        self.PORTC_tab_2 = QWidget()
        self.PORTC_tab_2.setObjectName(u"PORTC_tab_2")
        self.PORTC_groupBox_2 = QGroupBox(self.PORTC_tab_2)
        self.PORTC_groupBox_2.setObjectName(u"PORTC_groupBox_2")
        self.PORTC_groupBox_2.setGeometry(QRect(10, 10, 741, 191))
        self.All_Output_Init0_pushButton_20 = QPushButton(self.PORTC_groupBox_2)
        self.All_Output_Init0_pushButton_20.setObjectName(u"All_Output_Init0_pushButton_20")
        self.All_Output_Init0_pushButton_20.setGeometry(QRect(120, 160, 111, 18))
        self.All_Output_Init1_pushButton_20 = QPushButton(self.PORTC_groupBox_2)
        self.All_Output_Init1_pushButton_20.setObjectName(u"All_Output_Init1_pushButton_20")
        self.All_Output_Init1_pushButton_20.setGeometry(QRect(250, 160, 111, 18))
        self.All_Input_Init0_pushButton_20 = QPushButton(self.PORTC_groupBox_2)
        self.All_Input_Init0_pushButton_20.setObjectName(u"All_Input_Init0_pushButton_20")
        self.All_Input_Init0_pushButton_20.setGeometry(QRect(380, 160, 111, 18))
        self.All_Input_Init1_pushButton_20 = QPushButton(self.PORTC_groupBox_2)
        self.All_Input_Init1_pushButton_20.setObjectName(u"All_Input_Init1_pushButton_20")
        self.All_Input_Init1_pushButton_20.setGeometry(QRect(510, 160, 111, 18))
        self.PIN1_groupBox_20 = QGroupBox(self.PORTC_groupBox_2)
        self.PIN1_groupBox_20.setObjectName(u"PIN1_groupBox_20")
        self.PIN1_groupBox_20.setGeometry(QRect(100, 20, 91, 131))
        self.Output_init1_PIN1_radioButton_20 = QRadioButton(self.PIN1_groupBox_20)
        self.Output_init1_PIN1_radioButton_20.setObjectName(u"Output_init1_PIN1_radioButton_20")
        self.Output_init1_PIN1_radioButton_20.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN1_radioButton_20 = QRadioButton(self.PIN1_groupBox_20)
        self.Input_init0_PIN1_radioButton_20.setObjectName(u"Input_init0_PIN1_radioButton_20")
        self.Input_init0_PIN1_radioButton_20.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN1_radioButton_20 = QRadioButton(self.PIN1_groupBox_20)
        self.Input_init1_PIN1_radioButton_20.setObjectName(u"Input_init1_PIN1_radioButton_20")
        self.Input_init1_PIN1_radioButton_20.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN1_radioButton_20 = QRadioButton(self.PIN1_groupBox_20)
        self.Output_init0_PIN1_radioButton_20.setObjectName(u"Output_init0_PIN1_radioButton_20")
        self.Output_init0_PIN1_radioButton_20.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN1_radioButton_20.setChecked(True)
        self.PIN0_groupBox_19 = QGroupBox(self.PORTC_groupBox_2)
        self.PIN0_groupBox_19.setObjectName(u"PIN0_groupBox_19")
        self.PIN0_groupBox_19.setGeometry(QRect(10, 20, 91, 131))
        self.Output_init1_PIN0_radioButton_20 = QRadioButton(self.PIN0_groupBox_19)
        self.Output_init1_PIN0_radioButton_20.setObjectName(u"Output_init1_PIN0_radioButton_20")
        self.Output_init1_PIN0_radioButton_20.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN0_radioButton_20 = QRadioButton(self.PIN0_groupBox_19)
        self.Input_init0_PIN0_radioButton_20.setObjectName(u"Input_init0_PIN0_radioButton_20")
        self.Input_init0_PIN0_radioButton_20.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN0_radioButton_21 = QRadioButton(self.PIN0_groupBox_19)
        self.Input_init1_PIN0_radioButton_21.setObjectName(u"Input_init1_PIN0_radioButton_21")
        self.Input_init1_PIN0_radioButton_21.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN0_radioButton_20 = QRadioButton(self.PIN0_groupBox_19)
        self.Output_init0_PIN0_radioButton_20.setObjectName(u"Output_init0_PIN0_radioButton_20")
        self.Output_init0_PIN0_radioButton_20.setGeometry(QRect(10, 29, 71, 20))
        self.Output_init0_PIN0_radioButton_20.setChecked(True)
        self.PIN4_groupBox_19 = QGroupBox(self.PORTC_groupBox_2)
        self.PIN4_groupBox_19.setObjectName(u"PIN4_groupBox_19")
        self.PIN4_groupBox_19.setGeometry(QRect(370, 20, 91, 131))
        self.Output_init1_PIN4_radioButton_19 = QRadioButton(self.PIN4_groupBox_19)
        self.Output_init1_PIN4_radioButton_19.setObjectName(u"Output_init1_PIN4_radioButton_19")
        self.Output_init1_PIN4_radioButton_19.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN4_radioButton_19 = QRadioButton(self.PIN4_groupBox_19)
        self.Input_init0_PIN4_radioButton_19.setObjectName(u"Input_init0_PIN4_radioButton_19")
        self.Input_init0_PIN4_radioButton_19.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN4_radioButton_19 = QRadioButton(self.PIN4_groupBox_19)
        self.Input_init1_PIN4_radioButton_19.setObjectName(u"Input_init1_PIN4_radioButton_19")
        self.Input_init1_PIN4_radioButton_19.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN4_radioButton_19 = QRadioButton(self.PIN4_groupBox_19)
        self.Output_init0_PIN4_radioButton_19.setObjectName(u"Output_init0_PIN4_radioButton_19")
        self.Output_init0_PIN4_radioButton_19.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN4_radioButton_19.setChecked(True)
        self.PIN2_groupBox_19 = QGroupBox(self.PORTC_groupBox_2)
        self.PIN2_groupBox_19.setObjectName(u"PIN2_groupBox_19")
        self.PIN2_groupBox_19.setGeometry(QRect(190, 20, 91, 131))
        self.Output_init1_PIN2_radioButton_19 = QRadioButton(self.PIN2_groupBox_19)
        self.Output_init1_PIN2_radioButton_19.setObjectName(u"Output_init1_PIN2_radioButton_19")
        self.Output_init1_PIN2_radioButton_19.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN2_radioButton_19 = QRadioButton(self.PIN2_groupBox_19)
        self.Input_init0_PIN2_radioButton_19.setObjectName(u"Input_init0_PIN2_radioButton_19")
        self.Input_init0_PIN2_radioButton_19.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN2_radioButton_19 = QRadioButton(self.PIN2_groupBox_19)
        self.Input_init1_PIN2_radioButton_19.setObjectName(u"Input_init1_PIN2_radioButton_19")
        self.Input_init1_PIN2_radioButton_19.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN2_radioButton_19 = QRadioButton(self.PIN2_groupBox_19)
        self.Output_init0_PIN2_radioButton_19.setObjectName(u"Output_init0_PIN2_radioButton_19")
        self.Output_init0_PIN2_radioButton_19.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN2_radioButton_19.setChecked(True)
        self.PIN5_groupBox_19 = QGroupBox(self.PORTC_groupBox_2)
        self.PIN5_groupBox_19.setObjectName(u"PIN5_groupBox_19")
        self.PIN5_groupBox_19.setGeometry(QRect(460, 20, 91, 131))
        self.Output_init1_PIN5_radioButton_19 = QRadioButton(self.PIN5_groupBox_19)
        self.Output_init1_PIN5_radioButton_19.setObjectName(u"Output_init1_PIN5_radioButton_19")
        self.Output_init1_PIN5_radioButton_19.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN5_radioButton_19 = QRadioButton(self.PIN5_groupBox_19)
        self.Input_init0_PIN5_radioButton_19.setObjectName(u"Input_init0_PIN5_radioButton_19")
        self.Input_init0_PIN5_radioButton_19.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN5_radioButton_19 = QRadioButton(self.PIN5_groupBox_19)
        self.Input_init1_PIN5_radioButton_19.setObjectName(u"Input_init1_PIN5_radioButton_19")
        self.Input_init1_PIN5_radioButton_19.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN5_radioButton_19 = QRadioButton(self.PIN5_groupBox_19)
        self.Output_init0_PIN5_radioButton_19.setObjectName(u"Output_init0_PIN5_radioButton_19")
        self.Output_init0_PIN5_radioButton_19.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN5_radioButton_19.setChecked(True)
        self.PIN7_groupBox_19 = QGroupBox(self.PORTC_groupBox_2)
        self.PIN7_groupBox_19.setObjectName(u"PIN7_groupBox_19")
        self.PIN7_groupBox_19.setGeometry(QRect(640, 20, 91, 131))
        self.Output_init1_PIN7_radioButton_19 = QRadioButton(self.PIN7_groupBox_19)
        self.Output_init1_PIN7_radioButton_19.setObjectName(u"Output_init1_PIN7_radioButton_19")
        self.Output_init1_PIN7_radioButton_19.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN7_radioButton_19 = QRadioButton(self.PIN7_groupBox_19)
        self.Input_init0_PIN7_radioButton_19.setObjectName(u"Input_init0_PIN7_radioButton_19")
        self.Input_init0_PIN7_radioButton_19.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN7_radioButton_19 = QRadioButton(self.PIN7_groupBox_19)
        self.Input_init1_PIN7_radioButton_19.setObjectName(u"Input_init1_PIN7_radioButton_19")
        self.Input_init1_PIN7_radioButton_19.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN7_radioButton_19 = QRadioButton(self.PIN7_groupBox_19)
        self.Output_init0_PIN7_radioButton_19.setObjectName(u"Output_init0_PIN7_radioButton_19")
        self.Output_init0_PIN7_radioButton_19.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN7_radioButton_19.setChecked(True)
        self.PIN6_groupBox_19 = QGroupBox(self.PORTC_groupBox_2)
        self.PIN6_groupBox_19.setObjectName(u"PIN6_groupBox_19")
        self.PIN6_groupBox_19.setGeometry(QRect(550, 20, 91, 131))
        self.Output_init1_PIN6_radioButton_19 = QRadioButton(self.PIN6_groupBox_19)
        self.Output_init1_PIN6_radioButton_19.setObjectName(u"Output_init1_PIN6_radioButton_19")
        self.Output_init1_PIN6_radioButton_19.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN6_radioButton_19 = QRadioButton(self.PIN6_groupBox_19)
        self.Input_init0_PIN6_radioButton_19.setObjectName(u"Input_init0_PIN6_radioButton_19")
        self.Input_init0_PIN6_radioButton_19.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN6_radioButton_19 = QRadioButton(self.PIN6_groupBox_19)
        self.Input_init1_PIN6_radioButton_19.setObjectName(u"Input_init1_PIN6_radioButton_19")
        self.Input_init1_PIN6_radioButton_19.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN6_radioButton_19 = QRadioButton(self.PIN6_groupBox_19)
        self.Output_init0_PIN6_radioButton_19.setObjectName(u"Output_init0_PIN6_radioButton_19")
        self.Output_init0_PIN6_radioButton_19.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN6_radioButton_19.setChecked(True)
        self.PIN3_groupBox_19 = QGroupBox(self.PORTC_groupBox_2)
        self.PIN3_groupBox_19.setObjectName(u"PIN3_groupBox_19")
        self.PIN3_groupBox_19.setGeometry(QRect(280, 20, 91, 131))
        self.Output_init1_PIN3_radioButton_19 = QRadioButton(self.PIN3_groupBox_19)
        self.Output_init1_PIN3_radioButton_19.setObjectName(u"Output_init1_PIN3_radioButton_19")
        self.Output_init1_PIN3_radioButton_19.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN3_radioButton_19 = QRadioButton(self.PIN3_groupBox_19)
        self.Input_init0_PIN3_radioButton_19.setObjectName(u"Input_init0_PIN3_radioButton_19")
        self.Input_init0_PIN3_radioButton_19.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN3_radioButton_19 = QRadioButton(self.PIN3_groupBox_19)
        self.Input_init1_PIN3_radioButton_19.setObjectName(u"Input_init1_PIN3_radioButton_19")
        self.Input_init1_PIN3_radioButton_19.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN3_radioButton_19 = QRadioButton(self.PIN3_groupBox_19)
        self.Output_init0_PIN3_radioButton_19.setObjectName(u"Output_init0_PIN3_radioButton_19")
        self.Output_init0_PIN3_radioButton_19.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN3_radioButton_19.setChecked(True)
        self.tabWidget.addTab(self.PORTC_tab_2, "PORTC")
        self.PORTD_tab_2 = QWidget()
        self.PORTD_tab_2.setObjectName(u"PORTD_tab_2")
        self.PORTD_groupBox_2 = QGroupBox(self.PORTD_tab_2)
        self.PORTD_groupBox_2.setObjectName(u"PORTD_groupBox_2")
        self.PORTD_groupBox_2.setGeometry(QRect(10, 10, 741, 191))
        self.All_Output_Init0_pushButton_11 = QPushButton(self.PORTD_groupBox_2)
        self.All_Output_Init0_pushButton_11.setObjectName(u"All_Output_Init0_pushButton_11")
        self.All_Output_Init0_pushButton_11.setGeometry(QRect(120, 160, 111, 18))
        self.All_Output_Init1_pushButton_11 = QPushButton(self.PORTD_groupBox_2)
        self.All_Output_Init1_pushButton_11.setObjectName(u"All_Output_Init1_pushButton_11")
        self.All_Output_Init1_pushButton_11.setGeometry(QRect(250, 160, 111, 18))
        self.All_Input_Init0_pushButton_11 = QPushButton(self.PORTD_groupBox_2)
        self.All_Input_Init0_pushButton_11.setObjectName(u"All_Input_Init0_pushButton_11")
        self.All_Input_Init0_pushButton_11.setGeometry(QRect(380, 160, 111, 18))
        self.All_Input_Init1_pushButton_11 = QPushButton(self.PORTD_groupBox_2)
        self.All_Input_Init1_pushButton_11.setObjectName(u"All_Input_Init1_pushButton_11")
        self.All_Input_Init1_pushButton_11.setGeometry(QRect(510, 160, 111, 18))
        self.PIN1_groupBox_11 = QGroupBox(self.PORTD_groupBox_2)
        self.PIN1_groupBox_11.setObjectName(u"PIN1_groupBox_11")
        self.PIN1_groupBox_11.setGeometry(QRect(100, 20, 91, 131))
        self.Output_init1_PIN1_radioButton_11 = QRadioButton(self.PIN1_groupBox_11)
        self.Output_init1_PIN1_radioButton_11.setObjectName(u"Output_init1_PIN1_radioButton_11")
        self.Output_init1_PIN1_radioButton_11.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN1_radioButton_11 = QRadioButton(self.PIN1_groupBox_11)
        self.Input_init0_PIN1_radioButton_11.setObjectName(u"Input_init0_PIN1_radioButton_11")
        self.Input_init0_PIN1_radioButton_11.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN1_radioButton_11 = QRadioButton(self.PIN1_groupBox_11)
        self.Input_init1_PIN1_radioButton_11.setObjectName(u"Input_init1_PIN1_radioButton_11")
        self.Input_init1_PIN1_radioButton_11.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN1_radioButton_11 = QRadioButton(self.PIN1_groupBox_11)
        self.Output_init0_PIN1_radioButton_11.setObjectName(u"Output_init0_PIN1_radioButton_11")
        self.Output_init0_PIN1_radioButton_11.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN1_radioButton_11.setChecked(True)
        self.PIN0_groupBox_10 = QGroupBox(self.PORTD_groupBox_2)
        self.PIN0_groupBox_10.setObjectName(u"PIN0_groupBox_10")
        self.PIN0_groupBox_10.setEnabled(True)
        self.PIN0_groupBox_10.setGeometry(QRect(10, 20, 91, 131))
        self.PIN0_groupBox_10.setAutoFillBackground(False)
        self.Output_init1_PIN0_radioButton_11 = QRadioButton(self.PIN0_groupBox_10)
        self.Output_init1_PIN0_radioButton_11.setObjectName(u"Output_init1_PIN0_radioButton_11")
        self.Output_init1_PIN0_radioButton_11.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN0_radioButton_11 = QRadioButton(self.PIN0_groupBox_10)
        self.Input_init0_PIN0_radioButton_11.setObjectName(u"Input_init0_PIN0_radioButton_11")
        self.Input_init0_PIN0_radioButton_11.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN0_radioButton_12 = QRadioButton(self.PIN0_groupBox_10)
        self.Input_init1_PIN0_radioButton_12.setObjectName(u"Input_init1_PIN0_radioButton_12")
        self.Input_init1_PIN0_radioButton_12.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN0_radioButton_11 = QRadioButton(self.PIN0_groupBox_10)
        self.Output_init0_PIN0_radioButton_11.setObjectName(u"Output_init0_PIN0_radioButton_11")
        self.Output_init0_PIN0_radioButton_11.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN0_radioButton_11.setChecked(True)
        self.PIN4_groupBox_10 = QGroupBox(self.PORTD_groupBox_2)
        self.PIN4_groupBox_10.setObjectName(u"PIN4_groupBox_10")
        self.PIN4_groupBox_10.setGeometry(QRect(370, 20, 91, 131))
        self.Output_init1_PIN4_radioButton_10 = QRadioButton(self.PIN4_groupBox_10)
        self.Output_init1_PIN4_radioButton_10.setObjectName(u"Output_init1_PIN4_radioButton_10")
        self.Output_init1_PIN4_radioButton_10.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN4_radioButton_10 = QRadioButton(self.PIN4_groupBox_10)
        self.Input_init0_PIN4_radioButton_10.setObjectName(u"Input_init0_PIN4_radioButton_10")
        self.Input_init0_PIN4_radioButton_10.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN4_radioButton_10 = QRadioButton(self.PIN4_groupBox_10)
        self.Input_init1_PIN4_radioButton_10.setObjectName(u"Input_init1_PIN4_radioButton_10")
        self.Input_init1_PIN4_radioButton_10.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN4_radioButton_10 = QRadioButton(self.PIN4_groupBox_10)
        self.Output_init0_PIN4_radioButton_10.setObjectName(u"Output_init0_PIN4_radioButton_10")
        self.Output_init0_PIN4_radioButton_10.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN4_radioButton_10.setChecked(True)
        self.PIN2_groupBox_10 = QGroupBox(self.PORTD_groupBox_2)
        self.PIN2_groupBox_10.setObjectName(u"PIN2_groupBox_10")
        self.PIN2_groupBox_10.setGeometry(QRect(190, 20, 91, 131))
        self.Output_init1_PIN2_radioButton_10 = QRadioButton(self.PIN2_groupBox_10)
        self.Output_init1_PIN2_radioButton_10.setObjectName(u"Output_init1_PIN2_radioButton_10")
        self.Output_init1_PIN2_radioButton_10.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN2_radioButton_10 = QRadioButton(self.PIN2_groupBox_10)
        self.Input_init0_PIN2_radioButton_10.setObjectName(u"Input_init0_PIN2_radioButton_10")
        self.Input_init0_PIN2_radioButton_10.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN2_radioButton_10 = QRadioButton(self.PIN2_groupBox_10)
        self.Input_init1_PIN2_radioButton_10.setObjectName(u"Input_init1_PIN2_radioButton_10")
        self.Input_init1_PIN2_radioButton_10.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN2_radioButton_10 = QRadioButton(self.PIN2_groupBox_10)
        self.Output_init0_PIN2_radioButton_10.setObjectName(u"Output_init0_PIN2_radioButton_10")
        self.Output_init0_PIN2_radioButton_10.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN2_radioButton_10.setChecked(True)
        self.PIN5_groupBox_10 = QGroupBox(self.PORTD_groupBox_2)
        self.PIN5_groupBox_10.setObjectName(u"PIN5_groupBox_10")
        self.PIN5_groupBox_10.setGeometry(QRect(460, 20, 91, 131))
        self.Output_init1_PIN5_radioButton_10 = QRadioButton(self.PIN5_groupBox_10)
        self.Output_init1_PIN5_radioButton_10.setObjectName(u"Output_init1_PIN5_radioButton_10")
        self.Output_init1_PIN5_radioButton_10.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN5_radioButton_10 = QRadioButton(self.PIN5_groupBox_10)
        self.Input_init0_PIN5_radioButton_10.setObjectName(u"Input_init0_PIN5_radioButton_10")
        self.Input_init0_PIN5_radioButton_10.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN5_radioButton_10 = QRadioButton(self.PIN5_groupBox_10)
        self.Input_init1_PIN5_radioButton_10.setObjectName(u"Input_init1_PIN5_radioButton_10")
        self.Input_init1_PIN5_radioButton_10.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN5_radioButton_10 = QRadioButton(self.PIN5_groupBox_10)
        self.Output_init0_PIN5_radioButton_10.setObjectName(u"Output_init0_PIN5_radioButton_10")
        self.Output_init0_PIN5_radioButton_10.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN5_radioButton_10.setChecked(True)
        self.PIN7_groupBox_10 = QGroupBox(self.PORTD_groupBox_2)
        self.PIN7_groupBox_10.setObjectName(u"PIN7_groupBox_10")
        self.PIN7_groupBox_10.setGeometry(QRect(640, 20, 91, 131))
        self.Output_init1_PIN7_radioButton_10 = QRadioButton(self.PIN7_groupBox_10)
        self.Output_init1_PIN7_radioButton_10.setObjectName(u"Output_init1_PIN7_radioButton_10")
        self.Output_init1_PIN7_radioButton_10.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN7_radioButton_10 = QRadioButton(self.PIN7_groupBox_10)
        self.Input_init0_PIN7_radioButton_10.setObjectName(u"Input_init0_PIN7_radioButton_10")
        self.Input_init0_PIN7_radioButton_10.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN7_radioButton_10 = QRadioButton(self.PIN7_groupBox_10)
        self.Input_init1_PIN7_radioButton_10.setObjectName(u"Input_init1_PIN7_radioButton_10")
        self.Input_init1_PIN7_radioButton_10.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN7_radioButton_10 = QRadioButton(self.PIN7_groupBox_10)
        self.Output_init0_PIN7_radioButton_10.setObjectName(u"Output_init0_PIN7_radioButton_10")
        self.Output_init0_PIN7_radioButton_10.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN7_radioButton_10.setChecked(True)
        self.PIN6_groupBox_10 = QGroupBox(self.PORTD_groupBox_2)
        self.PIN6_groupBox_10.setObjectName(u"PIN6_groupBox_10")
        self.PIN6_groupBox_10.setGeometry(QRect(550, 20, 91, 131))
        self.Output_init1_PIN6_radioButton_10 = QRadioButton(self.PIN6_groupBox_10)
        self.Output_init1_PIN6_radioButton_10.setObjectName(u"Output_init1_PIN6_radioButton_10")
        self.Output_init1_PIN6_radioButton_10.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN6_radioButton_10 = QRadioButton(self.PIN6_groupBox_10)
        self.Input_init0_PIN6_radioButton_10.setObjectName(u"Input_init0_PIN6_radioButton_10")
        self.Input_init0_PIN6_radioButton_10.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN6_radioButton_10 = QRadioButton(self.PIN6_groupBox_10)
        self.Input_init1_PIN6_radioButton_10.setObjectName(u"Input_init1_PIN6_radioButton_10")
        self.Input_init1_PIN6_radioButton_10.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN6_radioButton_10 = QRadioButton(self.PIN6_groupBox_10)
        self.Output_init0_PIN6_radioButton_10.setObjectName(u"Output_init0_PIN6_radioButton_10")
        self.Output_init0_PIN6_radioButton_10.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN6_radioButton_10.setChecked(True)
        self.PIN3_groupBox_10 = QGroupBox(self.PORTD_groupBox_2)
        self.PIN3_groupBox_10.setObjectName(u"PIN3_groupBox_10")
        self.PIN3_groupBox_10.setGeometry(QRect(280, 20, 91, 131))
        self.Output_init1_PIN3_radioButton_10 = QRadioButton(self.PIN3_groupBox_10)
        self.Output_init1_PIN3_radioButton_10.setObjectName(u"Output_init1_PIN3_radioButton_10")
        self.Output_init1_PIN3_radioButton_10.setGeometry(QRect(10, 50, 71, 18))
        self.Input_init0_PIN3_radioButton_10 = QRadioButton(self.PIN3_groupBox_10)
        self.Input_init0_PIN3_radioButton_10.setObjectName(u"Input_init0_PIN3_radioButton_10")
        self.Input_init0_PIN3_radioButton_10.setGeometry(QRect(10, 70, 71, 18))
        self.Input_init1_PIN3_radioButton_10 = QRadioButton(self.PIN3_groupBox_10)
        self.Input_init1_PIN3_radioButton_10.setObjectName(u"Input_init1_PIN3_radioButton_10")
        self.Input_init1_PIN3_radioButton_10.setGeometry(QRect(10, 90, 71, 18))
        self.Output_init0_PIN3_radioButton_10 = QRadioButton(self.PIN3_groupBox_10)
        self.Output_init0_PIN3_radioButton_10.setObjectName(u"Output_init0_PIN3_radioButton_10")
        self.Output_init0_PIN3_radioButton_10.setGeometry(QRect(10, 30, 71, 18))
        self.Output_init0_PIN3_radioButton_10.setChecked(True)
        self.tabWidget.addTab(self.PORTD_tab_2, "PORTD")
        self.lineEdit = QLineEdit(self.DIOgroupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 370, 471, 31))
        self.dockWidget = QDockWidget(Form)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setGeometry(QRect(10, 80, 761, 101))
        self.dockWidget.setVisible(False)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.LoadgroupBox = QGroupBox(self.dockWidgetContents)
        self.LoadgroupBox.setObjectName(u"LoadgroupBox")
        self.LoadgroupBox.setGeometry(QRect(10, 10, 731, 61))
        self.LoadgroupBox.setLayoutDirection(Qt.RightToLeft)
        # Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter
        # AlignRight          =   0x0002 
        # Qt.AlignTrailing    =   AlignRight
        # AlignVCenter        =   0x0080
        self.LoadgroupBox.setAlignment(0x0002|0x0002|0x0080)
        self.LoadpushButton = QPushButton(self.LoadgroupBox)
        self.LoadpushButton.setObjectName(u"LoadpushButton")
        self.LoadpushButton.setGeometry(QRect(641, 20, 81, 31))
        self.textEdit_2 = QTextEdit(self.LoadgroupBox)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(9, 20, 620, 31))
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(660, 20, 71, 41))
        self.pushButton_4.setVisible(False)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1, -6, 781, 501))
        self.label.setTextFormat(Qt.AutoText)
        #self.label.setPixmap(QPixmap(u":/newPrefix/skull.png"))
        self.label.setPixmap(QPixmap(u"skull.png"))
        self.label.setScaledContents(True)
        self.label.raise_()
        self.dockWidget.raise_()
        self.DIOgroupBox.raise_()
        self.pushButton_4.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(self.pushButton_2.hide)
        self.pushButton_2.clicked.connect(self.pushButton_3.hide)
        self.pushButton_3.clicked.connect(self.DIOgroupBox.show)
       # self.LoadpushButton.clicked.connect(self.DIOgroupBox.show)
       # self.LoadgroupBox.clicked.connect(self.LoadgroupBox.hide)
       # self.LoadpushButton.clicked.connect(self.dockWidget.close)  
        self.pushButton_2.clicked.connect(self.LoadgroupBox.show)
        self.pushButton_2.clicked.connect(self.dockWidget.show)
      
        self.pushButton_3.clicked.connect(self.pushButton_4.show)
        self.pushButton_4.clicked.connect(self.DIOgroupBox.hide)
        self.pushButton_4.clicked.connect(self.pushButton_3.show)
        self.pushButton_4.clicked.connect(self.pushButton_2.show)
        self.pushButton_2.clicked.connect(self.pushButton_4.show)
        self.pushButton_4.clicked.connect(self.dockWidget.close)
        self.pushButton_3.clicked.connect(self.pushButton_3.hide)
        self.pushButton_2.clicked.connect(self.pushButton_2.hide)
        self.All_Output_Init0_pushButton_18.clicked.connect(self.Output_init0_PIN0_radioButton_18.click)
        self.All_Output_Init0_pushButton_18.clicked.connect(self.Output_init0_PIN1_radioButton_18.click)
        self.All_Output_Init0_pushButton_18.clicked.connect(self.Output_init0_PIN2_radioButton_17.click)
        self.All_Output_Init0_pushButton_18.clicked.connect(self.Output_init0_PIN3_radioButton_17.click)
        self.All_Output_Init0_pushButton_18.clicked.connect(self.Output_init0_PIN4_radioButton_17.click)
        self.All_Output_Init0_pushButton_18.clicked.connect(self.Output_init0_PIN6_radioButton_17.click)
        self.All_Output_Init0_pushButton_18.clicked.connect(self.Output_init0_PIN7_radioButton_17.click)
        self.All_Output_Init1_pushButton_18.clicked.connect(self.Output_init1_PIN0_radioButton_18.click)
        self.All_Output_Init1_pushButton_18.clicked.connect(self.Output_init1_PIN1_radioButton_18.click)
        self.All_Output_Init1_pushButton_18.clicked.connect(self.Output_init1_PIN2_radioButton_17.click)
        self.All_Output_Init1_pushButton_18.clicked.connect(self.Output_init1_PIN3_radioButton_17.click)
        self.All_Output_Init1_pushButton_18.clicked.connect(self.Output_init1_PIN4_radioButton_17.click)
        self.All_Output_Init1_pushButton_18.clicked.connect(self.Output_init1_PIN5_radioButton_17.click)
        self.All_Output_Init1_pushButton_18.clicked.connect(self.Output_init1_PIN6_radioButton_17.click)
        self.All_Output_Init1_pushButton_18.clicked.connect(self.Output_init1_PIN7_radioButton_17.click)
        self.All_Input_Init0_pushButton_18.clicked.connect(self.Input_init0_PIN0_radioButton_18.click)
        self.All_Input_Init0_pushButton_18.clicked.connect(self.Input_init0_PIN1_radioButton_18.click)
        self.All_Input_Init0_pushButton_18.clicked.connect(self.Input_init0_PIN2_radioButton_17.click)
        self.All_Input_Init0_pushButton_18.clicked.connect(self.Input_init0_PIN3_radioButton_17.click)
        self.All_Input_Init0_pushButton_18.clicked.connect(self.Input_init0_PIN4_radioButton_17.click)
        self.All_Input_Init0_pushButton_18.clicked.connect(self.Input_init0_PIN5_radioButton_17.click)
        self.All_Input_Init0_pushButton_18.clicked.connect(self.Input_init0_PIN6_radioButton_17.click)
        self.All_Input_Init0_pushButton_18.clicked.connect(self.Input_init0_PIN7_radioButton_17.click)
        self.All_Input_Init1_pushButton_18.clicked.connect(self.Input_init1_PIN7_radioButton_17.click)
        self.All_Input_Init1_pushButton_18.clicked.connect(self.Input_init1_PIN6_radioButton_17.click)
        self.All_Input_Init1_pushButton_18.clicked.connect(self.Input_init1_PIN5_radioButton_17.click)
        self.All_Input_Init1_pushButton_18.clicked.connect(self.Input_init1_PIN4_radioButton_17.click)
        self.All_Input_Init1_pushButton_18.clicked.connect(self.Input_init1_PIN3_radioButton_17.click)
        self.All_Input_Init1_pushButton_18.clicked.connect(self.Input_init1_PIN2_radioButton_17.click)
        self.All_Input_Init1_pushButton_18.clicked.connect(self.Input_init1_PIN1_radioButton_18.click)
        self.All_Input_Init1_pushButton_18.clicked.connect(self.Input_init1_PIN0_radioButton_19.click)
        self.All_Output_Init0_pushButton_18.clicked.connect(self.Output_init0_PIN5_radioButton_17.click)
        self.All_Output_Init0_pushButton_19.clicked.connect(self.Output_init0_PIN0_radioButton_19.click)
        self.All_Output_Init0_pushButton_19.clicked.connect(self.Output_init0_PIN1_radioButton_19.click)
        self.All_Output_Init0_pushButton_19.clicked.connect(self.Output_init0_PIN2_radioButton_18.click)
        self.All_Output_Init0_pushButton_19.clicked.connect(self.Output_init0_PIN3_radioButton_18.click)
        self.All_Output_Init0_pushButton_19.clicked.connect(self.Output_init0_PIN4_radioButton_18.click)
        self.All_Output_Init0_pushButton_19.clicked.connect(self.Output_init0_PIN5_radioButton_18.click)
        self.All_Output_Init0_pushButton_19.clicked.connect(self.Output_init0_PIN6_radioButton_18.click)
        self.All_Output_Init0_pushButton_19.clicked.connect(self.Output_init0_PIN7_radioButton_18.click)
        self.All_Output_Init1_pushButton_19.clicked.connect(self.Output_init1_PIN0_radioButton_19.click)
        self.All_Output_Init1_pushButton_19.clicked.connect(self.Output_init1_PIN1_radioButton_19.click)
        self.All_Output_Init1_pushButton_19.clicked.connect(self.Output_init1_PIN2_radioButton_18.click)
        self.All_Output_Init1_pushButton_19.clicked.connect(self.Output_init1_PIN3_radioButton_18.click)
        self.All_Output_Init1_pushButton_19.clicked.connect(self.Output_init1_PIN4_radioButton_18.click)
        self.All_Output_Init1_pushButton_19.clicked.connect(self.Output_init1_PIN5_radioButton_18.click)
        self.All_Output_Init1_pushButton_19.clicked.connect(self.Output_init1_PIN6_radioButton_18.click)
        self.All_Output_Init1_pushButton_19.clicked.connect(self.Output_init1_PIN7_radioButton_18.click)
        self.All_Input_Init0_pushButton_19.clicked.connect(self.Input_init0_PIN0_radioButton_19.click)
        self.All_Input_Init0_pushButton_19.clicked.connect(self.Input_init0_PIN1_radioButton_19.click)
        self.All_Input_Init0_pushButton_19.clicked.connect(self.Input_init0_PIN2_radioButton_18.click)
        self.All_Input_Init0_pushButton_19.clicked.connect(self.Input_init0_PIN3_radioButton_18.click)
        self.All_Input_Init0_pushButton_19.clicked.connect(self.Input_init0_PIN4_radioButton_18.click)
        self.All_Input_Init0_pushButton_19.clicked.connect(self.Input_init0_PIN5_radioButton_18.click)
        self.All_Input_Init0_pushButton_19.clicked.connect(self.Input_init0_PIN7_radioButton_18.click)
        self.All_Input_Init1_pushButton_19.clicked.connect(self.Input_init1_PIN0_radioButton_20.click)
        self.All_Input_Init1_pushButton_19.clicked.connect(self.Input_init1_PIN7_radioButton_18.click)
        self.All_Input_Init1_pushButton_19.clicked.connect(self.Input_init1_PIN6_radioButton_18.click)
        self.All_Input_Init1_pushButton_19.clicked.connect(self.Input_init1_PIN5_radioButton_18.click)
        self.All_Input_Init1_pushButton_19.clicked.connect(self.Input_init1_PIN4_radioButton_18.click)
        self.All_Input_Init1_pushButton_19.clicked.connect(self.Input_init1_PIN3_radioButton_18.click)
        self.All_Input_Init1_pushButton_19.clicked.connect(self.Input_init1_PIN2_radioButton_18.click)
        self.All_Input_Init1_pushButton_19.clicked.connect(self.Input_init1_PIN1_radioButton_19.click)
        self.All_Input_Init0_pushButton_19.clicked.connect(self.Input_init0_PIN6_radioButton_18.click)
        self.All_Output_Init0_pushButton_20.clicked.connect(self.Output_init0_PIN0_radioButton_20.click)
        self.All_Output_Init0_pushButton_20.clicked.connect(self.Output_init0_PIN1_radioButton_20.click)
        self.All_Output_Init0_pushButton_20.clicked.connect(self.Output_init0_PIN2_radioButton_19.click)
        self.All_Output_Init0_pushButton_20.clicked.connect(self.Output_init0_PIN3_radioButton_19.click)
        self.All_Output_Init0_pushButton_20.clicked.connect(self.Output_init0_PIN4_radioButton_19.click)
        self.All_Output_Init0_pushButton_20.clicked.connect(self.Output_init0_PIN5_radioButton_19.click)
        self.All_Output_Init0_pushButton_20.clicked.connect(self.Output_init0_PIN6_radioButton_19.click)
        self.All_Output_Init0_pushButton_20.clicked.connect(self.Output_init0_PIN7_radioButton_19.click)
        self.All_Output_Init1_pushButton_20.clicked.connect(self.Output_init1_PIN0_radioButton_20.click)
        self.All_Output_Init1_pushButton_20.clicked.connect(self.Output_init1_PIN1_radioButton_20.click)
        self.All_Output_Init1_pushButton_20.clicked.connect(self.Output_init1_PIN2_radioButton_19.click)
        self.All_Output_Init1_pushButton_20.clicked.connect(self.Output_init1_PIN3_radioButton_19.click)
        self.All_Output_Init1_pushButton_20.clicked.connect(self.Output_init1_PIN4_radioButton_19.click)
        self.All_Output_Init1_pushButton_20.clicked.connect(self.Output_init1_PIN5_radioButton_19.click)
        self.All_Output_Init1_pushButton_20.clicked.connect(self.Output_init1_PIN6_radioButton_19.click)
        self.All_Output_Init1_pushButton_20.clicked.connect(self.Output_init1_PIN7_radioButton_19.click)
        self.All_Input_Init0_pushButton_20.clicked.connect(self.Input_init0_PIN7_radioButton_19.click)
        self.All_Input_Init0_pushButton_20.clicked.connect(self.Input_init0_PIN6_radioButton_19.click)
        self.All_Input_Init0_pushButton_20.clicked.connect(self.Input_init0_PIN5_radioButton_19.click)
        self.All_Input_Init0_pushButton_20.clicked.connect(self.Input_init0_PIN4_radioButton_19.click)
        self.All_Input_Init0_pushButton_20.clicked.connect(self.Input_init0_PIN3_radioButton_19.click)
        self.All_Input_Init0_pushButton_20.clicked.connect(self.Input_init0_PIN2_radioButton_19.click)
        self.All_Input_Init0_pushButton_20.clicked.connect(self.Input_init0_PIN1_radioButton_20.click)
        self.All_Input_Init0_pushButton_20.clicked.connect(self.Input_init0_PIN0_radioButton_20.click)
        self.All_Input_Init1_pushButton_20.clicked.connect(self.Input_init1_PIN7_radioButton_19.click)
        self.All_Input_Init1_pushButton_20.clicked.connect(self.Input_init1_PIN6_radioButton_19.click)
        self.All_Input_Init1_pushButton_20.clicked.connect(self.Input_init1_PIN5_radioButton_19.click)
        self.All_Input_Init1_pushButton_20.clicked.connect(self.Input_init1_PIN4_radioButton_19.click)
        self.All_Input_Init1_pushButton_20.clicked.connect(self.Input_init1_PIN3_radioButton_19.click)
        self.All_Input_Init1_pushButton_20.clicked.connect(self.Input_init1_PIN2_radioButton_19.click)
        self.All_Input_Init1_pushButton_20.clicked.connect(self.Input_init1_PIN1_radioButton_20.click)
        self.All_Input_Init1_pushButton_20.clicked.connect(self.Input_init1_PIN0_radioButton_21.click)
        self.All_Output_Init0_pushButton_11.clicked.connect(self.Output_init0_PIN0_radioButton_11.click)
        self.All_Output_Init0_pushButton_11.clicked.connect(self.Output_init0_PIN1_radioButton_11.click)
        self.All_Output_Init0_pushButton_11.clicked.connect(self.Output_init0_PIN2_radioButton_10.click)
        self.All_Output_Init0_pushButton_11.clicked.connect(self.Output_init0_PIN3_radioButton_10.click)
        self.All_Output_Init0_pushButton_11.clicked.connect(self.Output_init0_PIN4_radioButton_10.click)
        self.All_Output_Init0_pushButton_11.clicked.connect(self.Output_init0_PIN5_radioButton_10.click)
        self.All_Output_Init0_pushButton_11.clicked.connect(self.Output_init0_PIN6_radioButton_10.click)
        self.All_Output_Init0_pushButton_11.clicked.connect(self.Output_init0_PIN7_radioButton_10.click)
        self.All_Output_Init1_pushButton_11.clicked.connect(self.Output_init1_PIN0_radioButton_11.click)
        self.All_Output_Init1_pushButton_11.clicked.connect(self.Output_init1_PIN3_radioButton_10.click)
        self.All_Output_Init1_pushButton_11.clicked.connect(self.Output_init1_PIN7_radioButton_10.click)
        self.All_Output_Init1_pushButton_11.clicked.connect(self.Output_init1_PIN6_radioButton_10.click)
        self.All_Output_Init1_pushButton_11.clicked.connect(self.Output_init1_PIN5_radioButton_10.click)
        self.All_Output_Init1_pushButton_11.clicked.connect(self.Output_init1_PIN4_radioButton_10.click)
        self.All_Output_Init1_pushButton_11.clicked.connect(self.Output_init1_PIN2_radioButton_10.click)
        self.All_Output_Init1_pushButton_11.clicked.connect(self.Output_init1_PIN1_radioButton_11.click)
        self.All_Input_Init0_pushButton_11.clicked.connect(self.Input_init0_PIN7_radioButton_10.click)
        self.All_Input_Init0_pushButton_11.clicked.connect(self.Input_init0_PIN6_radioButton_10.click)
        self.All_Input_Init0_pushButton_11.clicked.connect(self.Input_init0_PIN5_radioButton_10.click)
        self.All_Input_Init0_pushButton_11.clicked.connect(self.Input_init0_PIN4_radioButton_10.click)
        self.All_Input_Init0_pushButton_11.clicked.connect(self.Input_init0_PIN3_radioButton_10.click)
        self.All_Input_Init0_pushButton_11.clicked.connect(self.Input_init0_PIN2_radioButton_10.click)
        self.All_Input_Init0_pushButton_11.clicked.connect(self.Input_init0_PIN1_radioButton_11.click)
        self.All_Input_Init0_pushButton_11.clicked.connect(self.Input_init0_PIN0_radioButton_11.click)
        self.All_Input_Init1_pushButton_11.clicked.connect(self.Input_init1_PIN7_radioButton_10.click)
        self.All_Input_Init1_pushButton_11.clicked.connect(self.Input_init1_PIN6_radioButton_10.click)
        self.All_Input_Init1_pushButton_11.clicked.connect(self.Input_init1_PIN5_radioButton_10.click)
        self.All_Input_Init1_pushButton_11.clicked.connect(self.Input_init1_PIN4_radioButton_10.click)
        self.All_Input_Init1_pushButton_11.clicked.connect(self.Input_init1_PIN3_radioButton_10.click)
        self.All_Input_Init1_pushButton_11.clicked.connect(self.Input_init1_PIN2_radioButton_10.click)
        self.All_Input_Init1_pushButton_11.clicked.connect(self.Input_init1_PIN1_radioButton_11.click)
        self.All_Input_Init1_pushButton_11.clicked.connect(self.Input_init1_PIN0_radioButton_12.click)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
        
        #Generate PushButton 
        self.pushButton.clicked.connect(self.GenerateFunction)
        
        #Load pushButton
        self.LoadpushButton.clicked.connect(self.LoadFunction)
        
        #Back pushButton (pushButton_4)
        self.pushButton_4.clicked.connect(self.BackPushButton)
        
    # setupUi
    
     #########################################################
    # Function Called By pushButton_4
    # Responsible for Going Back One Step To Main Menu
    #########################################################
    def BackPushButton(self):
      if self.pushButton_4.clicked:
        self.textEdit_2.setPlainText("Please Enter The Path of The File You Want To Load")
        self.lineEdit.setText("Enter Output Path Here")
        self.pushButton_4.clicked.connect(self.pushButton_4.hide)
    # BackPushButton    
    
    
    #########################################################
    # Function Called By Load Function
    # Responsible for loading ALL Ports Configurations
    # into DIO_Configurator tool
    #########################################################
    def LoadPorts(self):
      Port_List=["A","B","C","D"]
      Pin_List=[0,1,2,3,4,5,6,7]
      Loaded_Port_File=open(self.textEdit_2.toPlainText(),'r')
      File_Content=Loaded_Port_File.read()
      Loaded_Port_File.seek(0)
      Port_InitValue_List=[]
      Port_Direction_List=[]
      for i in Port_List:
        for j in Pin_List:
          InitValue_regex="(PORT"+i+"_PIN"+str(Pin_List[j])+"_INIT_VALUE)\s+(\d)"
          Direction_regex="(PORT"+i+"_PIN"+str(Pin_List[j])+"_DIR)\s+(\d)"
          Port_InitValue_List.append((re.search(InitValue_regex,File_Content)).group(2))
          Port_Direction_List.append((re.search(Direction_regex,File_Content)).group(2))
          ###################
          #      PORTA      #
          ###################
          if i == "A":
            if j == 0:
              if Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '1':
                self.Output_init1_PIN0_radioButton_18.setChecked(True)
              elif Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '0':
                self.Output_init0_PIN0_radioButton_18.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '1': 
                self.Input_init1_PIN0_radioButton_19.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '0':
                self.Input_init0_PIN0_radioButton_18.setChecked(True)
            elif j == 1:
              if Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '1':
                self.Output_init1_PIN1_radioButton_18.setChecked(True)
              elif Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '0':
                self.Output_init0_PIN1_radioButton_18.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '1': 
                self.Input_init1_PIN1_radioButton_18.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '0':
                self.Input_init0_PIN1_radioButton_18.setChecked(True)
            elif j == 2:
              if Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '1':
                self.Output_init1_PIN2_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '0':
                self.Output_init0_PIN2_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '1': 
                self.Input_init1_PIN2_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '0':
                self.Input_init0_PIN2_radioButton_17.setChecked(True) 
            elif j == 3:
              if Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '1':
                self.Output_init1_PIN3_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '0':
                self.Output_init0_PIN3_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '1': 
                self.Input_init1_PIN3_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '0':
                self.Input_init0_PIN3_radioButton_17.setChecked(True)
            elif j == 4:
              if Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '1':
                self.Output_init1_PIN4_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '0':
                self.Output_init0_PIN4_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '1': 
                self.Input_init1_PIN4_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '0':
                self.Input_init0_PIN4_radioButton_17.setChecked(True)  
            elif j == 5:
              if Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '1':
                self.Output_init1_PIN5_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '0':
                self.Output_init0_PIN5_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '1': 
                self.Input_init1_PIN5_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '0':
                self.Input_init0_PIN5_radioButton_17.setChecked(True)     
            elif j == 6:
              if Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '1':
                self.Output_init1_PIN6_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '0':
                self.Output_init0_PIN6_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '1': 
                self.Input_init1_PIN6_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '0':
                self.Input_init0_PIN6_radioButton_17.setChecked(True)
            elif j == 7:
              if Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '1':
                self.Output_init1_PIN7_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '1' and Port_InitValue_List[j] == '0':
                self.Output_init0_PIN7_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '1': 
                self.Input_init1_PIN7_radioButton_17.setChecked(True)
              elif Port_Direction_List[j] == '0' and Port_InitValue_List[j] == '0':
                self.Input_init0_PIN7_radioButton_17.setChecked(True)    
          
          ###################
          #      PORTB      #
          ###################
          elif i == "B":
            if j == 0:
              if Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '1':
                self.Output_init1_PIN0_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '0':
                self.Output_init0_PIN0_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '1': 
                self.Input_init1_PIN0_radioButton_20.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '0':
                self.Input_init0_PIN0_radioButton_19.setChecked(True)
            elif j == 1:
              if Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '1':
                self.Output_init1_PIN1_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '0':
                self.Output_init0_PIN1_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '1': 
                self.Input_init1_PIN1_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '0':
                self.Input_init0_PIN1_radioButton_19.setChecked(True)
            elif j == 2:
              if Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '1':
                self.Output_init1_PIN2_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '0':
                self.Output_init0_PIN2_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '1': 
                self.Input_init1_PIN2_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '0':
                self.Input_init0_PIN2_radioButton_18.setChecked(True)
            elif j == 3:
              if Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '1':
                self.Output_init1_PIN3_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '0':
                self.Output_init0_PIN3_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '1': 
                self.Input_init1_PIN3_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '0':
                self.Input_init0_PIN3_radioButton_18.setChecked(True)
            elif j == 4:
              if Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '1':
                self.Output_init1_PIN4_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '0':
                self.Output_init0_PIN4_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '1': 
                self.Input_init1_PIN4_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '0':
                self.Input_init0_PIN4_radioButton_18.setChecked(True)
            elif j == 5:
              if Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '1':
                self.Output_init1_PIN5_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '0':
                self.Output_init0_PIN5_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '1': 
                self.Input_init1_PIN5_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '0':
                self.Input_init0_PIN5_radioButton_18.setChecked(True)
            elif j == 6:
              if Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '1':
                self.Output_init1_PIN6_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '0':
                self.Output_init0_PIN6_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '1': 
                self.Input_init1_PIN6_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '0':
                self.Input_init0_PIN6_radioButton_18.setChecked(True)
            elif j == 7:
              if Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '1':
                self.Output_init1_PIN7_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '1' and Port_InitValue_List[j+8] == '0':
                self.Output_init0_PIN7_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '1': 
                self.Input_init1_PIN7_radioButton_18.setChecked(True)
              elif Port_Direction_List[j+8] == '0' and Port_InitValue_List[j+8] == '0':
                self.Input_init0_PIN7_radioButton_18.setChecked(True)  
          
          ###################
          #      PORTC      #
          ###################
          elif i == "C":
            if j == 0:
              if Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '1':
                self.Output_init1_PIN0_radioButton_20.setChecked(True)
              elif Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '0':
                self.Output_init0_PIN0_radioButton_20.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '1': 
                self.Input_init1_PIN0_radioButton_21.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '0':
                self.Input_init0_PIN0_radioButton_20.setChecked(True)
            elif j == 1:
              if Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '1':
                self.Output_init1_PIN1_radioButton_20.setChecked(True)
              elif Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '0':
                self.Output_init0_PIN1_radioButton_20.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '1': 
                self.Input_init1_PIN1_radioButton_20.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '0':
                self.Input_init0_PIN1_radioButton_20.setChecked(True)
            elif j == 2:
              if Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '1':
                self.Output_init1_PIN2_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '0':
                self.Output_init0_PIN2_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '1': 
                self.Input_init1_PIN2_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '0':
                self.Input_init0_PIN2_radioButton_19.setChecked(True) 
            elif j == 3:
              if Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '1':
                self.Output_init1_PIN3_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '0':
                self.Output_init0_PIN3_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '1': 
                self.Input_init1_PIN3_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '0':
                self.Input_init0_PIN3_radioButton_19.setChecked(True)
            elif j == 4:
              if Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '1':
                self.Output_init1_PIN4_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '0':
                self.Output_init0_PIN4_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '1': 
                self.Input_init1_PIN4_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '0':
                self.Input_init0_PIN4_radioButton_19.setChecked(True)  
            elif j == 5:
              if Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '1':
                self.Output_init1_PIN5_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '0':
                self.Output_init0_PIN5_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '1': 
                self.Input_init1_PIN5_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '0':
                self.Input_init0_PIN5_radioButton_19.setChecked(True)     
            elif j == 6:
              if Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '1':
                self.Output_init1_PIN6_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '0':
                self.Output_init0_PIN6_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '1': 
                self.Input_init1_PIN6_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '0':
                self.Input_init0_PIN6_radioButton_19.setChecked(True)
            elif j == 7:
              if Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '1':
                self.Output_init1_PIN7_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '1' and Port_InitValue_List[j+16] == '0':
                self.Output_init0_PIN7_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '1': 
                self.Input_init1_PIN7_radioButton_19.setChecked(True)
              elif Port_Direction_List[j+16] == '0' and Port_InitValue_List[j+16] == '0':
                self.Input_init0_PIN7_radioButton_19.setChecked(True)  
            
          ###################
          #      PORTD      #
          ###################
          elif i == "D":
            if j == 0:
              if Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '1':
                self.Output_init1_PIN0_radioButton_11.setChecked(True)
              elif Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '0':
                self.Output_init0_PIN0_radioButton_11.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '1': 
                self.Input_init1_PIN0_radioButton_12.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '0':
                self.Input_init0_PIN0_radioButton_11.setChecked(True)
            elif j == 1:
              if Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '1':
                self.Output_init1_PIN1_radioButton_11.setChecked(True)
              elif Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '0':
                self.Output_init0_PIN1_radioButton_11.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '1': 
                self.Input_init1_PIN1_radioButton_11.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '0':
                self.Input_init0_PIN1_radioButton_11.setChecked(True)
            elif j == 2:
              if Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '1':
                self.Output_init1_PIN2_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '0':
                self.Output_init0_PIN2_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '1': 
                self.Input_init1_PIN2_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '0':
                self.Input_init0_PIN2_radioButton_10.setChecked(True) 
            elif j == 3:
              if Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '1':
                self.Output_init1_PIN3_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '0':
                self.Output_init0_PIN3_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '1': 
                self.Input_init1_PIN3_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '0':
                self.Input_init0_PIN3_radioButton_10.setChecked(True)
            elif j == 4:
              if Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '1':
                self.Output_init1_PIN4_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '0':
                self.Output_init0_PIN4_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '1': 
                self.Input_init1_PIN4_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '0':
                self.Input_init0_PIN4_radioButton_10.setChecked(True)  
            elif j == 5:
              if Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '1':
                self.Output_init1_PIN5_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '0':
                self.Output_init0_PIN5_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '1': 
                self.Input_init1_PIN5_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '0':
                self.Input_init0_PIN5_radioButton_10.setChecked(True)     
            elif j == 6:
              if Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '1':
                self.Output_init1_PIN6_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '0':
                self.Output_init0_PIN6_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '1': 
                self.Input_init1_PIN6_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '0':
                self.Input_init0_PIN6_radioButton_10.setChecked(True)
            elif j == 7:
              if Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '1':
                self.Output_init1_PIN7_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '1' and Port_InitValue_List[j+24] == '0':
                self.Output_init0_PIN7_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '1': 
                self.Input_init1_PIN7_radioButton_10.setChecked(True)
              elif Port_Direction_List[j+24] == '0' and Port_InitValue_List[j+24] == '0':
                self.Input_init0_PIN7_radioButton_10.setChecked(True)  
        
      Loaded_Port_File.close()  
    # LoadPorts  

  
    #########################################################
    # Function Called When Load pushbutton is Pressed
    # Responsible for loading Config File of AVR Ports 
    # into DIO_Configurator tool
    #########################################################
    global counter
    counter = ''
    def LoadFunction(self):
      global counter
      if counter == "!!!!!!!":
        counter = ''  
      plain_text=self.textEdit_2.toPlainText()
      if os.path.isfile(plain_text):
        self.LoadpushButton.clicked.connect(self.DIOgroupBox.show)
        self.LoadgroupBox.clicked.connect(self.LoadgroupBox.hide)
        self.LoadpushButton.clicked.connect(self.dockWidget.hide)
        self.LoadPorts()
      else:  
        self.textEdit_2.setPlainText("INVALID PATH"+counter+"")
        counter += "!"  
    # LoadFunction
    
      
    
    #########################################################
    # Function Called When Generate_pushbutton is Pressed
    # Responsible for Generating Config File of AVR Ports
    #########################################################
    def GenerateFunction(self):
      global counter
      if counter == "!!!!!!!":
        counter = ''
      if not(os.path.isdir(self.lineEdit.text())):
        self.lineEdit.setText("INVALID PATH"+counter+"")
        counter += "!"
      else:
        PORT_Handler = open(self.lineEdit.text() + r'\PORT_config.h','w')
      
        PORT_Handler.write("/************************************************/\n")
        PORT_Handler.write("/*Author	:           				                  */\n")
        PORT_Handler.write("/*Version	:   								                  */\n")
        PORT_Handler.write("/*Date 		:           					                */\n")
        PORT_Handler.write("/************************************************/\n")
        PORT_Handler.write("\n/*Output = 1 .. Input = 0*/\n")
        #PORTA
        PORT_Handler.write("\n/*************PORTA*************/\n")
        if self.Output_init0_PIN0_radioButton_18.isChecked(): 
          PORT_Handler.write("#define PORTA_PIN0_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN0_INIT_VALUE   0\n")
        elif self.Output_init1_PIN0_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTA_PIN0_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN0_INIT_VALUE   1\n")
        elif self.Input_init0_PIN0_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTA_PIN0_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN0_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTA_PIN0_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN0_INIT_VALUE   1\n")
      
        
        if self.Output_init0_PIN1_radioButton_18.isChecked(): 
          PORT_Handler.write("#define PORTA_PIN1_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN1_INIT_VALUE   0\n")
        elif self.Output_init1_PIN1_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTA_PIN1_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN1_INIT_VALUE   1\n")
        elif self.Input_init0_PIN1_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTA_PIN1_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN1_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTA_PIN1_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN1_INIT_VALUE   1\n")
            
        
        if self.Output_init0_PIN2_radioButton_17.isChecked(): 
          PORT_Handler.write("#define PORTA_PIN2_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN2_INIT_VALUE   0\n")
        elif self.Output_init1_PIN2_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN2_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN2_INIT_VALUE   1\n")
        elif self.Input_init0_PIN2_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN2_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN2_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTA_PIN2_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN2_INIT_VALUE   1\n")    
          
        
        if self.Output_init0_PIN3_radioButton_17.isChecked(): 
          PORT_Handler.write("#define PORTA_PIN3_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN3_INIT_VALUE   0\n")
        elif self.Output_init1_PIN3_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN3_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN3_INIT_VALUE   1\n")
        elif self.Input_init0_PIN3_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN3_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN3_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTA_PIN3_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN3_INIT_VALUE   1\n")      
          
        
        if self.Output_init0_PIN4_radioButton_17.isChecked(): 
          PORT_Handler.write("#define PORTA_PIN4_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN4_INIT_VALUE   0\n")
        elif self.Output_init1_PIN4_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN4_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN4_INIT_VALUE   1\n")
        elif self.Input_init0_PIN4_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN4_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN4_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTA_PIN4_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN4_INIT_VALUE   1\n")  
        
        
        if self.Output_init0_PIN5_radioButton_17.isChecked(): 
          PORT_Handler.write("#define PORTA_PIN5_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN5_INIT_VALUE   0\n")
        elif self.Output_init1_PIN5_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN5_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN5_INIT_VALUE   1\n")
        elif self.Input_init0_PIN5_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN5_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN5_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTA_PIN5_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN5_INIT_VALUE   1\n")
        
        
        if self.Output_init0_PIN6_radioButton_17.isChecked(): 
          PORT_Handler.write("#define PORTA_PIN6_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN6_INIT_VALUE   0\n")
        elif self.Output_init1_PIN6_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN6_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN6_INIT_VALUE   1\n")
        elif self.Input_init0_PIN6_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN6_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN6_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTA_PIN6_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN6_INIT_VALUE   1\n")  
        
        
        if self.Output_init0_PIN7_radioButton_17.isChecked(): 
          PORT_Handler.write("#define PORTA_PIN7_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN7_INIT_VALUE   0\n")
        elif self.Output_init1_PIN7_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN7_DIR          1\n")
          PORT_Handler.write("#define PORTA_PIN7_INIT_VALUE   1\n")
        elif self.Input_init0_PIN7_radioButton_17.isChecked():  
          PORT_Handler.write("#define PORTA_PIN7_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN7_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTA_PIN7_DIR          0\n")
          PORT_Handler.write("#define PORTA_PIN7_INIT_VALUE   1\n")  
                
        
        #PORTB
        PORT_Handler.write("\n\n/*************PORTB*************/\n")  
        if self.Output_init0_PIN0_radioButton_19.isChecked(): 
          PORT_Handler.write("#define PORTB_PIN0_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN0_INIT_VALUE   0\n")
        elif self.Output_init1_PIN0_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTB_PIN0_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN0_INIT_VALUE   1\n")
        elif self.Input_init0_PIN0_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTB_PIN0_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN0_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTB_PIN0_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN0_INIT_VALUE   1\n")
        
        
        if self.Output_init0_PIN1_radioButton_19.isChecked(): 
          PORT_Handler.write("#define PORTB_PIN1_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN1_INIT_VALUE   0\n")
        elif self.Output_init1_PIN1_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTB_PIN1_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN1_INIT_VALUE   1\n")
        elif self.Input_init0_PIN1_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTB_PIN1_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN1_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTB_PIN1_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN1_INIT_VALUE   1\n")
            
      
        if self.Output_init0_PIN2_radioButton_18.isChecked(): 
          PORT_Handler.write("#define PORTB_PIN2_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN2_INIT_VALUE   0\n")
        elif self.Output_init1_PIN2_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN2_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN2_INIT_VALUE   1\n")
        elif self.Input_init0_PIN2_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN2_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN2_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTB_PIN2_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN2_INIT_VALUE   1\n")
          
      
        if self.Output_init0_PIN3_radioButton_18.isChecked(): 
          PORT_Handler.write("#define PORTB_PIN3_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN3_INIT_VALUE   0\n")
        elif self.Output_init1_PIN3_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN3_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN3_INIT_VALUE   1\n")
        elif self.Input_init0_PIN3_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN3_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN3_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTB_PIN3_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN3_INIT_VALUE   1\n")
          
      
        if self.Output_init0_PIN4_radioButton_18.isChecked(): 
          PORT_Handler.write("#define PORTB_PIN4_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN4_INIT_VALUE   0\n")
        elif self.Output_init1_PIN4_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN4_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN4_INIT_VALUE   1\n")
        elif self.Input_init0_PIN4_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN4_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN4_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTB_PIN4_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN4_INIT_VALUE   1\n")
      
      
        if self.Output_init0_PIN5_radioButton_18.isChecked(): 
          PORT_Handler.write("#define PORTB_PIN5_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN5_INIT_VALUE   0\n")
        elif self.Output_init1_PIN5_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN5_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN5_INIT_VALUE   1\n")
        elif self.Input_init0_PIN5_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN5_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN5_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTB_PIN5_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN5_INIT_VALUE   1\n")
        
      
        if self.Output_init0_PIN6_radioButton_18.isChecked(): 
          PORT_Handler.write("#define PORTB_PIN6_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN6_INIT_VALUE   0\n")
        elif self.Output_init1_PIN6_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN6_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN6_INIT_VALUE   1\n")
        elif self.Input_init0_PIN6_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN6_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN6_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTB_PIN6_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN6_INIT_VALUE   1\n")
      
      
        if self.Output_init0_PIN7_radioButton_18.isChecked(): 
          PORT_Handler.write("#define PORTB_PIN7_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN7_INIT_VALUE   0\n")
        elif self.Output_init1_PIN7_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN7_DIR          1\n")
          PORT_Handler.write("#define PORTB_PIN7_INIT_VALUE   1\n")
        elif self.Input_init0_PIN7_radioButton_18.isChecked():  
          PORT_Handler.write("#define PORTB_PIN7_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN7_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTB_PIN7_DIR          0\n")
          PORT_Handler.write("#define PORTB_PIN7_INIT_VALUE   1\n")
  
  
        #PORTC
        PORT_Handler.write("\n\n/*************PORTC*************/\n")
        if self.Output_init0_PIN0_radioButton_20.isChecked(): 
          PORT_Handler.write("#define PORTC_PIN0_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN0_INIT_VALUE   0\n")
        elif self.Output_init1_PIN0_radioButton_20.isChecked():  
          PORT_Handler.write("#define PORTC_PIN0_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN0_INIT_VALUE   1\n")
        elif self.Input_init0_PIN0_radioButton_20.isChecked():  
          PORT_Handler.write("#define PORTC_PIN0_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN0_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTC_PIN0_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN0_INIT_VALUE   1\n")
      
    
        if self.Output_init0_PIN1_radioButton_20.isChecked(): 
          PORT_Handler.write("#define PORTC_PIN1_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN1_INIT_VALUE   0\n")
        elif self.Output_init1_PIN1_radioButton_20.isChecked():  
          PORT_Handler.write("#define PORTC_PIN1_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN1_INIT_VALUE   1\n")
        elif self.Input_init0_PIN1_radioButton_20.isChecked():  
          PORT_Handler.write("#define PORTC_PIN1_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN1_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTC_PIN1_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN1_INIT_VALUE   1\n")
            
      
        if self.Output_init0_PIN2_radioButton_19.isChecked(): 
          PORT_Handler.write("#define PORTC_PIN2_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN2_INIT_VALUE   0\n")
        elif self.Output_init1_PIN2_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN2_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN2_INIT_VALUE   1\n")
        elif self.Input_init0_PIN2_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN2_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN2_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTC_PIN2_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN2_INIT_VALUE   1\n")
          
      
        if self.Output_init0_PIN3_radioButton_19.isChecked(): 
          PORT_Handler.write("#define PORTC_PIN3_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN3_INIT_VALUE   0\n")
        elif self.Output_init1_PIN3_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN3_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN3_INIT_VALUE   1\n")
        elif self.Input_init0_PIN3_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN3_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN3_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTC_PIN3_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN3_INIT_VALUE   1\n")
          
      
        if self.Output_init0_PIN4_radioButton_19.isChecked(): 
          PORT_Handler.write("#define PORTC_PIN4_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN4_INIT_VALUE   0\n")
        elif self.Output_init1_PIN4_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN4_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN4_INIT_VALUE   1\n")
        elif self.Input_init0_PIN4_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN4_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN4_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTC_PIN4_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN4_INIT_VALUE   1\n")
      
      
        if self.Output_init0_PIN5_radioButton_19.isChecked(): 
          PORT_Handler.write("#define PORTC_PIN5_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN5_INIT_VALUE   0\n")
        elif self.Output_init1_PIN5_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN5_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN5_INIT_VALUE   1\n")
        elif self.Input_init0_PIN5_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN5_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN5_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTC_PIN5_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN5_INIT_VALUE   1\n")
        
      
        if self.Output_init0_PIN6_radioButton_19.isChecked(): 
          PORT_Handler.write("#define PORTC_PIN6_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN6_INIT_VALUE   0\n")
        elif self.Output_init1_PIN6_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN6_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN6_INIT_VALUE   1\n")
        elif self.Input_init0_PIN6_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN6_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN6_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTC_PIN6_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN6_INIT_VALUE   1\n")
      
      
        if self.Output_init0_PIN7_radioButton_19.isChecked(): 
          PORT_Handler.write("#define PORTC_PIN7_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN7_INIT_VALUE   0\n")
        elif self.Output_init1_PIN7_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN7_DIR          1\n")
          PORT_Handler.write("#define PORTC_PIN7_INIT_VALUE   1\n")
        elif self.Input_init0_PIN7_radioButton_19.isChecked():  
          PORT_Handler.write("#define PORTC_PIN7_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN7_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTC_PIN7_DIR          0\n")
          PORT_Handler.write("#define PORTC_PIN7_INIT_VALUE   1\n")
  
  
        #PORTD
        PORT_Handler.write("\n\n/*************PORTD*************/\n")
        if self.Output_init0_PIN0_radioButton_11.isChecked(): 
          PORT_Handler.write("#define PORTD_PIN0_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN0_INIT_VALUE   0\n")
        elif self.Output_init1_PIN0_radioButton_11.isChecked():  
          PORT_Handler.write("#define PORTD_PIN0_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN0_INIT_VALUE   1\n")
        elif self.Input_init0_PIN0_radioButton_11.isChecked():  
          PORT_Handler.write("#define PORTD_PIN0_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN0_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTD_PIN0_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN0_INIT_VALUE   1\n")
      
      
        if self.Output_init0_PIN1_radioButton_11.isChecked(): 
          PORT_Handler.write("#define PORTD_PIN1_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN1_INIT_VALUE   0\n")
        elif self.Output_init1_PIN1_radioButton_11.isChecked():  
          PORT_Handler.write("#define PORTD_PIN1_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN1_INIT_VALUE   1\n")
        elif self.Input_init0_PIN1_radioButton_11.isChecked():  
          PORT_Handler.write("#define PORTD_PIN1_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN1_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTD_PIN1_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN1_INIT_VALUE   1\n")
            
      
        if self.Output_init0_PIN2_radioButton_10.isChecked(): 
          PORT_Handler.write("#define PORTD_PIN2_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN2_INIT_VALUE   0\n")
        elif self.Output_init1_PIN2_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN2_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN2_INIT_VALUE   1\n")
        elif self.Input_init0_PIN2_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN2_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN2_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTD_PIN2_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN2_INIT_VALUE   1\n")
          
      
        if self.Output_init0_PIN3_radioButton_10.isChecked(): 
          PORT_Handler.write("#define PORTD_PIN3_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN3_INIT_VALUE   0\n")
        elif self.Output_init1_PIN3_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN3_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN3_INIT_VALUE   1\n")
        elif self.Input_init0_PIN3_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN3_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN3_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTD_PIN3_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN3_INIT_VALUE   1\n")
          
      
        if self.Output_init0_PIN4_radioButton_10.isChecked(): 
          PORT_Handler.write("#define PORTD_PIN4_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN4_INIT_VALUE   0\n")
        elif self.Output_init1_PIN4_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN4_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN4_INIT_VALUE   1\n")
        elif self.Input_init0_PIN4_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN4_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN4_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTD_PIN4_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN4_INIT_VALUE   1\n")
      
      
        if self.Output_init0_PIN5_radioButton_10.isChecked(): 
          PORT_Handler.write("#define PORTD_PIN5_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN5_INIT_VALUE   0\n")
        elif self.Output_init1_PIN5_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN5_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN5_INIT_VALUE   1\n")
        elif self.Input_init0_PIN5_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN5_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN5_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTD_PIN5_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN5_INIT_VALUE   1\n")
        
      
        if self.Output_init0_PIN6_radioButton_10.isChecked(): 
          PORT_Handler.write("#define PORTD_PIN6_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN6_INIT_VALUE   0\n")
        elif self.Output_init1_PIN6_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN6_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN6_INIT_VALUE   1\n")
        elif self.Input_init0_PIN6_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN6_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN6_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTD_PIN6_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN6_INIT_VALUE   1\n")
      
      
        if self.Output_init0_PIN7_radioButton_10.isChecked(): 
          PORT_Handler.write("#define PORTD_PIN7_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN7_INIT_VALUE   0\n")
        elif self.Output_init1_PIN7_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN7_DIR          1\n")
          PORT_Handler.write("#define PORTD_PIN7_INIT_VALUE   1\n")
        elif self.Input_init0_PIN7_radioButton_10.isChecked():  
          PORT_Handler.write("#define PORTD_PIN7_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN7_INIT_VALUE   0\n")
        else:   
          PORT_Handler.write("#define PORTD_PIN7_DIR          0\n")
          PORT_Handler.write("#define PORTD_PIN7_INIT_VALUE   1\n")

        PORT_Handler.close()
    # GenerateFunction

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"NEW", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"LOAD", None))
        self.DIOgroupBox.setTitle(QCoreApplication.translate("Form", u"DIO_Configurator", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:600;\">  O/P-I.V=0  ==&gt; Output PIN with Initial Value = 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:600;\">  O/P-I.V=1  ==&gt; Output PIN with Initial Value = 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-we"
                        "ight:600;\">  I/P-I.V=0   ==&gt; Input PIN with Initial Value   = 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:600;\">  I/P-I.V=0   ==&gt; Input PIN with Initial Value   = 1</span></p></body></html>", None))
        self.PORTA_groupBox_2.setTitle(QCoreApplication.translate("Form", u"PORTA", None))
        self.All_Output_Init0_pushButton_18.setText(QCoreApplication.translate("Form", u"All_O/P with I.V=0", None))
        self.All_Output_Init1_pushButton_18.setText(QCoreApplication.translate("Form", u"All_O/P with I.V=1", None))
        self.All_Input_Init0_pushButton_18.setText(QCoreApplication.translate("Form", u"All_I/P with I.V=0", None))
        self.All_Input_Init1_pushButton_18.setText(QCoreApplication.translate("Form", u"All_I/P with I.V=1", None))
        self.PIN1_groupBox_18.setTitle(QCoreApplication.translate("Form", u"PIN1", None))
        self.Output_init1_PIN1_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN1_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN1_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN1_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN0_groupBox_17.setTitle(QCoreApplication.translate("Form", u"PIN0", None))
        self.Output_init1_PIN0_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN0_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN0_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN0_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN4_groupBox_17.setTitle(QCoreApplication.translate("Form", u"PIN4", None))
        self.Output_init1_PIN4_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN4_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN4_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN4_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN2_groupBox_17.setTitle(QCoreApplication.translate("Form", u"PIN2", None))
        self.Output_init1_PIN2_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN2_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN2_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN2_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN5_groupBox_17.setTitle(QCoreApplication.translate("Form", u"PIN5", None))
        self.Output_init1_PIN5_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN5_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN5_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN5_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN7_groupBox_17.setTitle(QCoreApplication.translate("Form", u"PIN7", None))
        self.Output_init1_PIN7_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN7_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN7_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN7_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN6_groupBox_17.setTitle(QCoreApplication.translate("Form", u"PIN6", None))
        self.Output_init1_PIN6_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN6_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN6_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN6_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN3_groupBox_17.setTitle(QCoreApplication.translate("Form", u"PIN3", None))
        self.Output_init1_PIN3_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN3_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN3_radioButton_17.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN3_radioButton_17.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTA_tab_2), QCoreApplication.translate("Form", u"PORTA", None))
        self.PORTB_groupBox_2.setTitle(QCoreApplication.translate("Form", u"PORTB", None))
        self.All_Output_Init0_pushButton_19.setText(QCoreApplication.translate("Form", u"All_O/P with I.V=0", None))
        self.All_Output_Init1_pushButton_19.setText(QCoreApplication.translate("Form", u"All_O/P with I.V=1", None))
        self.All_Input_Init0_pushButton_19.setText(QCoreApplication.translate("Form", u"All_I/P with I.V=0", None))
        self.All_Input_Init1_pushButton_19.setText(QCoreApplication.translate("Form", u"All_I/P with I.V=1", None))
        self.PIN1_groupBox_19.setTitle(QCoreApplication.translate("Form", u"PIN1", None))
        self.Output_init1_PIN1_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN1_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN1_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN1_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN0_groupBox_18.setTitle(QCoreApplication.translate("Form", u"PIN0", None))
        self.Output_init1_PIN0_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN0_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN0_radioButton_20.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN0_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN4_groupBox_18.setTitle(QCoreApplication.translate("Form", u"PIN4", None))
        self.Output_init1_PIN4_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN4_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN4_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN4_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN2_groupBox_18.setTitle(QCoreApplication.translate("Form", u"PIN2", None))
        self.Output_init1_PIN2_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN2_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN2_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN2_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN5_groupBox_18.setTitle(QCoreApplication.translate("Form", u"PIN5", None))
        self.Output_init1_PIN5_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN5_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN5_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN5_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN7_groupBox_18.setTitle(QCoreApplication.translate("Form", u"PIN7", None))
        self.Output_init1_PIN7_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN7_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN7_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN7_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN6_groupBox_18.setTitle(QCoreApplication.translate("Form", u"PIN6", None))
        self.Output_init1_PIN6_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN6_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN6_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN6_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN3_groupBox_18.setTitle(QCoreApplication.translate("Form", u"PIN3", None))
        self.Output_init1_PIN3_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN3_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN3_radioButton_18.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN3_radioButton_18.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTB_tab_2), QCoreApplication.translate("Form", u"PORTB", None))
        self.PORTC_groupBox_2.setTitle(QCoreApplication.translate("Form", u"PORTC", None))
        self.All_Output_Init0_pushButton_20.setText(QCoreApplication.translate("Form", u"All_O/P with I.V=0", None))
        self.All_Output_Init1_pushButton_20.setText(QCoreApplication.translate("Form", u"All_O/P with I.V=1", None))
        self.All_Input_Init0_pushButton_20.setText(QCoreApplication.translate("Form", u"All_I/P with I.V=0", None))
        self.All_Input_Init1_pushButton_20.setText(QCoreApplication.translate("Form", u"All_I/P with I.V=1", None))
        self.PIN1_groupBox_20.setTitle(QCoreApplication.translate("Form", u"PIN1", None))
        self.Output_init1_PIN1_radioButton_20.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN1_radioButton_20.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN1_radioButton_20.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN1_radioButton_20.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN0_groupBox_19.setTitle(QCoreApplication.translate("Form", u"PIN0", None))
        self.Output_init1_PIN0_radioButton_20.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN0_radioButton_20.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN0_radioButton_21.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN0_radioButton_20.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN4_groupBox_19.setTitle(QCoreApplication.translate("Form", u"PIN4", None))
        self.Output_init1_PIN4_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN4_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN4_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN4_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN2_groupBox_19.setTitle(QCoreApplication.translate("Form", u"PIN2", None))
        self.Output_init1_PIN2_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN2_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN2_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN2_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN5_groupBox_19.setTitle(QCoreApplication.translate("Form", u"PIN5", None))
        self.Output_init1_PIN5_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN5_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN5_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN5_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN7_groupBox_19.setTitle(QCoreApplication.translate("Form", u"PIN7", None))
        self.Output_init1_PIN7_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN7_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN7_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN7_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN6_groupBox_19.setTitle(QCoreApplication.translate("Form", u"PIN6", None))
        self.Output_init1_PIN6_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN6_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN6_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN6_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN3_groupBox_19.setTitle(QCoreApplication.translate("Form", u"PIN3", None))
        self.Output_init1_PIN3_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN3_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN3_radioButton_19.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN3_radioButton_19.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTC_tab_2), QCoreApplication.translate("Form", u"PORTC", None))
        self.PORTD_groupBox_2.setTitle(QCoreApplication.translate("Form", u"PORTD", None))
        self.All_Output_Init0_pushButton_11.setText(QCoreApplication.translate("Form", u"All_O/P with I.V=0", None))
        self.All_Output_Init1_pushButton_11.setText(QCoreApplication.translate("Form", u"All_O/P with I.V=1", None))
        self.All_Input_Init0_pushButton_11.setText(QCoreApplication.translate("Form", u"All_I/P with I.V=0", None))
        self.All_Input_Init1_pushButton_11.setText(QCoreApplication.translate("Form", u"All_I/P with I.V=1", None))
        self.PIN1_groupBox_11.setTitle(QCoreApplication.translate("Form", u"PIN1", None))
        self.Output_init1_PIN1_radioButton_11.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN1_radioButton_11.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN1_radioButton_11.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN1_radioButton_11.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN0_groupBox_10.setTitle(QCoreApplication.translate("Form", u"PIN0", None))
        self.Output_init1_PIN0_radioButton_11.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN0_radioButton_11.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN0_radioButton_12.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN0_radioButton_11.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN4_groupBox_10.setTitle(QCoreApplication.translate("Form", u"PIN4", None))
        self.Output_init1_PIN4_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN4_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN4_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN4_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN2_groupBox_10.setTitle(QCoreApplication.translate("Form", u"PIN2", None))
        self.Output_init1_PIN2_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN2_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN2_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN2_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN5_groupBox_10.setTitle(QCoreApplication.translate("Form", u"PIN5", None))
        self.Output_init1_PIN5_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN5_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN5_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN5_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN7_groupBox_10.setTitle(QCoreApplication.translate("Form", u"PIN7", None))
        self.Output_init1_PIN7_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN7_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN7_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN7_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN6_groupBox_10.setTitle(QCoreApplication.translate("Form", u"PIN6", None))
        self.Output_init1_PIN6_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN6_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN6_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN6_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.PIN3_groupBox_10.setTitle(QCoreApplication.translate("Form", u"PIN3", None))
        self.Output_init1_PIN3_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=1", None))
        self.Input_init0_PIN3_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=0", None))
        self.Input_init1_PIN3_radioButton_10.setText(QCoreApplication.translate("Form", u"I/P-I.V=1", None))
        self.Output_init0_PIN3_radioButton_10.setText(QCoreApplication.translate("Form", u"O/P-I.V=0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTD_tab_2), QCoreApplication.translate("Form", u"PORTD", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"Enter Output Path here", None))
        self.LoadgroupBox.setTitle(QCoreApplication.translate("Form", u"Load", None))
        self.LoadpushButton.setText(QCoreApplication.translate("Form", u"Load", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Please Enter The Path of The File You Want To Load</span></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"BACK", None))
        self.label.setText("")
    # retranslateUi


# Create the Qt Application
app = QApplication(sys.argv)
# Create the Qt Widget that will hold the Form/s
widget = QWidget()
# Create and show the form
form = Ui_Form()
form.setupUi(widget)
# Show what's inside the widget
widget.show()
# Run the main Qt loop
# Run the Application or execute it
app.exec_()
sys.exit()