# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 596)
        MainWindow.setStyleSheet("background-color: rgb(10, 25, 49);\n"
"color: rgb(255, 201, 71);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("color: rgb(24, 90, 219);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(4)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 9, 0, 1, 2)
        self.input_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_button.sizePolicy().hasHeightForWidth())
        self.input_button.setSizePolicy(sizePolicy)
        self.input_button.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_button.setFont(font)
        self.input_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 201, 71);\n"
"color: rgb(10, 25, 49);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(10, 25, 49);\n"
"color: rgb(255, 201, 71);\n"
"}\n"
"\n"
"")
        self.input_button.setObjectName("input_button")
        self.gridLayout_4.addWidget(self.input_button, 2, 0, 1, 1)
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("background-color: rgb(255, 73, 122);\n"
"color: rgb(10, 25, 49);")
        self.title_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.title_label.setMidLineWidth(0)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.gridLayout_4.addWidget(self.title_label, 0, 0, 1, 2)
        self.bw_g_label = QtWidgets.QLabel(self.centralwidget)
        self.bw_g_label.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bw_g_label.setFont(font)
        self.bw_g_label.setStyleSheet("background-color: rgb(24, 90, 219);\n"
"color: rgb(239, 239, 239);")
        self.bw_g_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bw_g_label.setObjectName("bw_g_label")
        self.gridLayout_4.addWidget(self.bw_g_label, 4, 0, 1, 1)
        self.transfroms_label = QtWidgets.QLabel(self.centralwidget)
        self.transfroms_label.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.transfroms_label.setFont(font)
        self.transfroms_label.setStyleSheet("background-color: rgb(24, 90, 219);\n"
"color: rgb(239, 239, 239);")
        self.transfroms_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.transfroms_label.setObjectName("transfroms_label")
        self.gridLayout_4.addWidget(self.transfroms_label, 7, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gamma_label = QtWidgets.QLabel(self.centralwidget)
        self.gamma_label.setMaximumSize(QtCore.QSize(60, 30))
        self.gamma_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gamma_label.setObjectName("gamma_label")
        self.gridLayout_2.addWidget(self.gamma_label, 0, 2, 1, 1)
        self.negative_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.negative_button.sizePolicy().hasHeightForWidth())
        self.negative_button.setSizePolicy(sizePolicy)
        self.negative_button.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.negative_button.setFont(font)
        self.negative_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 201, 71);\n"
"color: rgb(10, 25, 49);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(10, 25, 49);\n"
"color: rgb(255, 201, 71);\n"
"}\n"
"\n"
"")
        self.negative_button.setObjectName("negative_button")
        self.gridLayout_2.addWidget(self.negative_button, 0, 0, 1, 1)
        self.gamma_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.gamma_lineEdit.setMaximumSize(QtCore.QSize(80, 25))
        self.gamma_lineEdit.setFrame(True)
        self.gamma_lineEdit.setObjectName("gamma_lineEdit")
        self.gridLayout_2.addWidget(self.gamma_lineEdit, 0, 3, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setMinimumSize(QtCore.QSize(5, 80))
        self.line_4.setStyleSheet("color: rgb(24, 90, 219);\n"
"")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 7, 1, 1)
        self.c_gamma_label = QtWidgets.QLabel(self.centralwidget)
        self.c_gamma_label.setMaximumSize(QtCore.QSize(30, 30))
        self.c_gamma_label.setAlignment(QtCore.Qt.AlignCenter)
        self.c_gamma_label.setObjectName("c_gamma_label")
        self.gridLayout_2.addWidget(self.c_gamma_label, 0, 4, 1, 1)
        self.gamma_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gamma_button.sizePolicy().hasHeightForWidth())
        self.gamma_button.setSizePolicy(sizePolicy)
        self.gamma_button.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gamma_button.setFont(font)
        self.gamma_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 201, 71);\n"
"color: rgb(10, 25, 49);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(10, 25, 49);\n"
"color: rgb(255, 201, 71);\n"
"}\n"
"\n"
"")
        self.gamma_button.setObjectName("gamma_button")
        self.gridLayout_2.addWidget(self.gamma_button, 0, 6, 1, 1)
        self.c_gamma_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.c_gamma_lineEdit.setMaximumSize(QtCore.QSize(80, 25))
        self.c_gamma_lineEdit.setObjectName("c_gamma_lineEdit")
        self.gridLayout_2.addWidget(self.c_gamma_lineEdit, 0, 5, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(4, 1)
        self.gridLayout_2.setColumnStretch(5, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 8, 0, 1, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.bilateral_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bilateral_button.sizePolicy().hasHeightForWidth())
        self.bilateral_button.setSizePolicy(sizePolicy)
        self.bilateral_button.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bilateral_button.setFont(font)
        self.bilateral_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 201, 71);\n"
"color: rgb(10, 25, 49);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(10, 25, 49);\n"
"color: rgb(255, 201, 71);\n"
"}\n"
"\n"
"")
        self.bilateral_button.setObjectName("bilateral_button")
        self.gridLayout_3.addWidget(self.bilateral_button, 0, 4, 1, 1)
        self.kernel_size_label = QtWidgets.QLabel(self.centralwidget)
        self.kernel_size_label.setMaximumSize(QtCore.QSize(100, 30))
        self.kernel_size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.kernel_size_label.setObjectName("kernel_size_label")
        self.gridLayout_3.addWidget(self.kernel_size_label, 0, 0, 1, 1)
        self.median_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.median_button.sizePolicy().hasHeightForWidth())
        self.median_button.setSizePolicy(sizePolicy)
        self.median_button.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.median_button.setFont(font)
        self.median_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 201, 71);\n"
"color: rgb(10, 25, 49);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(10, 25, 49);\n"
"color: rgb(255, 201, 71);\n"
"}\n"
"\n"
"")
        self.median_button.setObjectName("median_button")
        self.gridLayout_3.addWidget(self.median_button, 0, 3, 1, 1)
        self.kernel_size_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.kernel_size_lineEdit.setMaximumSize(QtCore.QSize(80, 25))
        self.kernel_size_lineEdit.setObjectName("kernel_size_lineEdit")
        self.gridLayout_3.addWidget(self.kernel_size_lineEdit, 0, 1, 1, 1)
        self.sigma_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sigma_lineEdit.setMaximumSize(QtCore.QSize(80, 25))
        self.sigma_lineEdit.setObjectName("sigma_lineEdit")
        self.gridLayout_3.addWidget(self.sigma_lineEdit, 0, 6, 1, 1)
        self.gaussian_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gaussian_button.sizePolicy().hasHeightForWidth())
        self.gaussian_button.setSizePolicy(sizePolicy)
        self.gaussian_button.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gaussian_button.setFont(font)
        self.gaussian_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 201, 71);\n"
"color: rgb(10, 25, 49);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(10, 25, 49);\n"
"color: rgb(255, 201, 71);\n"
"}\n"
"\n"
"")
        self.gaussian_button.setObjectName("gaussian_button")
        self.gridLayout_3.addWidget(self.gaussian_button, 0, 7, 1, 1)
        self.sigma_label = QtWidgets.QLabel(self.centralwidget)
        self.sigma_label.setMaximumSize(QtCore.QSize(70, 30))
        self.sigma_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sigma_label.setObjectName("sigma_label")
        self.gridLayout_3.addWidget(self.sigma_label, 0, 5, 1, 1)
        self.mean_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mean_button.sizePolicy().hasHeightForWidth())
        self.mean_button.setSizePolicy(sizePolicy)
        self.mean_button.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mean_button.setFont(font)
        self.mean_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 201, 71);\n"
"color: rgb(10, 25, 49);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(10, 25, 49);\n"
"color: rgb(255, 201, 71);\n"
"}\n"
"\n"
"")
        self.mean_button.setObjectName("mean_button")
        self.gridLayout_3.addWidget(self.mean_button, 0, 2, 1, 1)
        self.laplacian_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.laplacian_button.sizePolicy().hasHeightForWidth())
        self.laplacian_button.setSizePolicy(sizePolicy)
        self.laplacian_button.setMaximumSize(QtCore.QSize(300, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.laplacian_button.setFont(font)
        self.laplacian_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 201, 71);\n"
"color: rgb(10, 25, 49);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(10, 25, 49);\n"
"color: rgb(255, 201, 71);\n"
"}\n"
"\n"
"")
        self.laplacian_button.setObjectName("laplacian_button")
        self.gridLayout_3.addWidget(self.laplacian_button, 2, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 9, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.gridLayout_3.setColumnStretch(4, 1)
        self.gridLayout_3.setColumnStretch(5, 1)
        self.gridLayout_3.setColumnStretch(6, 1)
        self.gridLayout_3.setColumnStretch(7, 1)
        self.gridLayout_3.setColumnStretch(8, 1)
        self.gridLayout_3.setColumnStretch(9, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 11, 0, 1, 2)
        self.filters_label = QtWidgets.QLabel(self.centralwidget)
        self.filters_label.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filters_label.setFont(font)
        self.filters_label.setStyleSheet("background-color: rgb(24, 90, 219);\n"
"color: rgb(239, 239, 239);")
        self.filters_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filters_label.setObjectName("filters_label")
        self.gridLayout_4.addWidget(self.filters_label, 10, 0, 1, 1)
        self.Input_label = QtWidgets.QLabel(self.centralwidget)
        self.Input_label.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Input_label.setFont(font)
        self.Input_label.setStyleSheet("background-color: rgb(24, 90, 219);\n"
"color: rgb(239, 239, 239);")
        self.Input_label.setObjectName("Input_label")
        self.gridLayout_4.addWidget(self.Input_label, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setStyleSheet("color: rgb(24, 90, 219);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 3, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("color: rgb(24, 90, 219);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 6, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.bw_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bw_button.sizePolicy().hasHeightForWidth())
        self.bw_button.setSizePolicy(sizePolicy)
        self.bw_button.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bw_button.setFont(font)
        self.bw_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 201, 71);\n"
"color: rgb(10, 25, 49);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(10, 25, 49);\n"
"color: rgb(255, 201, 71);\n"
"}\n"
"\n"
"")
        self.bw_button.setObjectName("bw_button")
        self.gridLayout.addWidget(self.bw_button, 0, 0, 1, 1)
        self.gray_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gray_button.sizePolicy().hasHeightForWidth())
        self.gray_button.setSizePolicy(sizePolicy)
        self.gray_button.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gray_button.setFont(font)
        self.gray_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 201, 71);\n"
"color: rgb(10, 25, 49);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(10, 25, 49);\n"
"color: rgb(255, 201, 71);\n"
"}\n"
"\n"
"")
        self.gray_button.setObjectName("gray_button")
        self.gridLayout.addWidget(self.gray_button, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 5, 0, 1, 2)
        self.gridLayout_4.setColumnStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_button.setText(_translate("MainWindow", "Select Image"))
        self.title_label.setText(_translate("MainWindow", "Image Processing Toolkit"))
        self.bw_g_label.setText(_translate("MainWindow", "Black & White and Grayscale"))
        self.transfroms_label.setText(_translate("MainWindow", "Intensity Transforms"))
        self.gamma_label.setText(_translate("MainWindow", "Gamma ="))
        self.negative_button.setText(_translate("MainWindow", "Negative Transformation"))
        self.c_gamma_label.setText(_translate("MainWindow", "C ="))
        self.gamma_button.setText(_translate("MainWindow", "Gamma Transformation"))
        self.bilateral_button.setText(_translate("MainWindow", "Bilateral"))
        self.kernel_size_label.setText(_translate("MainWindow", "Kernel size ="))
        self.median_button.setText(_translate("MainWindow", "Median"))
        self.gaussian_button.setText(_translate("MainWindow", "Gauusian"))
        self.sigma_label.setText(_translate("MainWindow", "Sigma ="))
        self.mean_button.setText(_translate("MainWindow", "Mean"))
        self.laplacian_button.setText(_translate("MainWindow", "Laplacian"))
        self.filters_label.setText(_translate("MainWindow", "Spectical Filters"))
        self.Input_label.setText(_translate("MainWindow", "Select Input Image"))
        self.bw_button.setText(_translate("MainWindow", "Black and White"))
        self.gray_button.setText(_translate("MainWindow", "Grayscale"))

