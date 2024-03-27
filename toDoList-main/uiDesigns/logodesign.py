# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logodesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(190, 300, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(50, 175, 200, 30))
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(50, 250, 200, 30))
        self.passwordInput.setObjectName("passwordInput")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(115, 145, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(115, 220, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 281, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.todoLabel = QtWidgets.QLabel(self.frame)
        self.todoLabel.setGeometry(QtCore.QRect(70, 20, 140, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.todoLabel.setFont(font)
        self.todoLabel.setObjectName("todoLabel")
        self.createaccountButton = QtWidgets.QPushButton(self.centralwidget)
        self.createaccountButton.setGeometry(QtCore.QRect(30, 300, 150, 24))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.createaccountButton.setFont(font)
        self.createaccountButton.setObjectName("createaccountButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", " Password"))
        self.todoLabel.setText(_translate("MainWindow", "To-Do List"))
        self.createaccountButton.setText(_translate("MainWindow", "Create Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
