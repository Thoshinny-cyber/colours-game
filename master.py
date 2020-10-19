
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtCore import  QTimer 
import random 
import os
import time

# ---------- We dont Touch --------------------
class Ui_Outsecure(object):
    """
    LOGIN PAGE
    """
    def setupUi(self, Outsecure):
        Outsecure.setObjectName("Outsecure")
        Outsecure.resize(529, 342)
        Outsecure.setMouseTracking(True)
        Outsecure.setStyleSheet("background-color: rgb(8, 8, 8);")
        self.line = QtWidgets.QFrame(Outsecure)
        self.line.setGeometry(QtCore.QRect(10, 80, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.l_title = QtWidgets.QLabel(Outsecure)
        self.l_title.setGeometry(QtCore.QRect(170, 20, 231, 41))
        self.l_title.setStyleSheet("color: rgb(242, 247, 247);\n"
                                   "font: 30pt \".SF NS Text\";")
        self.l_title.setObjectName("l_title")
        self.btn_Submit = QtWidgets.QPushButton(Outsecure)
        self.btn_Submit.setGeometry(QtCore.QRect(180, 200, 161, 31))
        self.btn_Submit.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(134, 15, 148);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 14pt \"Arial\";")
        self.btn_Submit.setObjectName("btn_Submit")
        self.btn_newuser = QtWidgets.QPushButton(Outsecure)
        self.btn_newuser.setGeometry(QtCore.QRect(180, 240, 161, 31))
        self.btn_newuser.setStyleSheet("color: rgb(250, 255, 255);\n"
                                       "background-color: rgb(134, 15, 148);\n"
                                       "border-style:outset;\n"
                                       "border-radius:10px;\n"
                                       "font: 14pt \"Arial\";")
        self.btn_newuser.setObjectName("btn_newuser")
        '''
        self.l_copyright = QtWidgets.QLabel(Outsecure)
        self.l_copyright.setGeometry(QtCore.QRect(150, 310, 261, 21))
        self.l_copyright.setStyleSheet("color: rgb(252, 0, 28);")
        self.l_copyright.setObjectName("l_copyright") '''
        self.txt_username = QtWidgets.QLineEdit(Outsecure)
        self.txt_username.setGeometry(QtCore.QRect(130, 100, 275, 31))
        self.txt_username.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_username.setObjectName("txt_username")
        self.txt_password = QtWidgets.QLineEdit(Outsecure)
        self.txt_password.setGeometry(QtCore.QRect(130, 150, 271, 31))
        self.txt_password.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_password.setObjectName("txt_password")

        self.retranslateUi(Outsecure)
        QtCore.QMetaObject.connectSlotsByName(Outsecure)

    def retranslateUi(self, Outsecure):
        _translate = QtCore.QCoreApplication.translate
        Outsecure.setWindowTitle(_translate("Outsecure", "Form"))
        self.l_title.setText(_translate("Outsecure", "Login Page"))
        self.btn_Submit.setText(_translate("Outsecure", "Submit"))
        self.btn_newuser.setText(_translate("Outsecure", "New User"))
        #self.l_copyright.setText(_translate("Outsecure", "This software belongs to OutSecure "))
        self.txt_username.setPlaceholderText(_translate("Outsecure", "Enter UserName"))
        self.txt_password.setPlaceholderText(_translate("Outsecure", "Enter Password"))

class Ui_NewUser(object):
    """
    NEW USERS
    """
    def setupUi(self, NewUser):
        NewUser.setObjectName("NewUser")
        NewUser.resize(555, 372)
        NewUser.setStyleSheet("background-color: rgb(14, 14, 14);")
        self.l_newuser = QtWidgets.QLabel(NewUser)
        self.l_newuser.setGeometry(QtCore.QRect(180, 10, 181, 31))
        self.l_newuser.setStyleSheet("font: 24pt \".SF NS Text\";\n"
                                     "color: rgb(234, 239, 238);\n"
                                     "")
        self.l_newuser.setAlignment(QtCore.Qt.AlignCenter)
        self.l_newuser.setObjectName("l_newuser")
        self.line = QtWidgets.QFrame(NewUser)
        self.line.setGeometry(QtCore.QRect(10, 50, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txt_firstname = QtWidgets.QLineEdit(NewUser)
        self.txt_firstname.setEnabled(True)
        self.txt_firstname.setGeometry(QtCore.QRect(30, 80, 230, 41))
        self.txt_firstname.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                         "border-style:outset;\n"
                                         "border-radius:10px;\n"
                                         "font: 14pt \"Arial\";")
        self.txt_firstname.setText("")
        self.txt_firstname.setObjectName("txt_firstname")
        self.txt_lastname = QtWidgets.QLineEdit(NewUser)
        self.txt_lastname.setGeometry(QtCore.QRect(290, 80, 229, 41))
        self.txt_lastname.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_lastname.setObjectName("txt_lastname")
        self.txt_phone = QtWidgets.QLineEdit(NewUser)
        self.txt_phone.setGeometry(QtCore.QRect(30, 140, 230, 41))
        self.txt_phone.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                     "border-style:outset;\n"
                                     "border-radius:10px;\n"
                                     "font: 14pt \"Arial\";")
        self.txt_phone.setObjectName("txt_phone")
        self.txt_email = QtWidgets.QLineEdit(NewUser)
        self.txt_email.setGeometry(QtCore.QRect(290, 140, 229, 41))
        self.txt_email.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                     "border-style:outset;\n"
                                     "border-radius:10px;\n"
                                     "font: 14pt \"Arial\";")
        self.txt_email.setObjectName("txt_email")
        self.txt_username = QtWidgets.QLineEdit(NewUser)
        self.txt_username.setGeometry(QtCore.QRect(30, 200, 230, 41))
        self.txt_username.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_username.setObjectName("txt_username")
        self.lineEdit = QtWidgets.QLineEdit(NewUser)
        self.lineEdit.setGeometry(QtCore.QRect(290, 200, 231, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "font: 14pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.btn_submit = QtWidgets.QPushButton(NewUser)
        self.btn_submit.setGeometry(QtCore.QRect(190, 270, 159, 31))
        self.btn_submit.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(134, 15, 148);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 14pt \"Arial\";")
        self.btn_submit.setObjectName("btn_submit")
        self.Back = QtWidgets.QPushButton(NewUser)
        self.Back.setGeometry(QtCore.QRect(190, 320, 159, 31))
        self.Back.setStyleSheet("color: rgb(250, 255, 255);\n"
                                "background-color: rgb(134, 15, 148);\n"
                                "border-style:outset;\n"
                                "border-radius:10px;\n"
                                "font: 14pt \"Arial\";")
        self.Back.setObjectName("Back")

        self.retranslateUi(NewUser)
        QtCore.QMetaObject.connectSlotsByName(NewUser)

    def retranslateUi(self, NewUser):
        _translate = QtCore.QCoreApplication.translate
        NewUser.setWindowTitle(_translate("NewUser", "Form"))
        self.l_newuser.setText(_translate("NewUser", "New User"))
        self.txt_firstname.setPlaceholderText(_translate("NewUser", "Enter your First Name"))
        self.txt_lastname.setPlaceholderText(_translate("NewUser", "Enter your Last Name"))
        self.txt_phone.setPlaceholderText(_translate("NewUser", "Enter your Email Address"))
        self.txt_email.setPlaceholderText(_translate("NewUser", "Confirm your Email Address "))
        self.txt_username.setPlaceholderText(_translate("NewUser", "Enter Username"))
        self.btn_submit.setText(_translate("NewUser", "Submit"))
        self.Back.setText(_translate("NewUser", "Back"))
class Ui_ColourWindow(object):         
    def setupUi(self, ColourWindow):
        ColourWindow.setObjectName("ColourWindow")
        ColourWindow.resize(356, 468)
        self.centralwidget = QtWidgets.QWidget(ColourWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.greyzy_colour = QtWidgets.QLabel(self.centralwidget)
        self.greyzy_colour.setGeometry(QtCore.QRect(0, 0, 361, 421))
        self.greyzy_colour.setStyleSheet("background-Color: rgb(188, 54, 96);")
        self.greyzy_colour.setText("")
        self.greyzy_colour.setPixmap(QtGui.QPixmap("F:/UI/images/black.jpg"))
        self.greyzy_colour.setScaledContents(True)
        self.greyzy_colour.setObjectName("greyzy_colour")
        self.instructions = QtWidgets.QLabel(self.centralwidget)
        self.instructions.setGeometry(QtCore.QRect(30, 80, 271, 20))
        self.instructions.setStyleSheet("font: 12pt \"Century\";\n"
"Color: rgb(255, 255, 255);")
        self.instructions.setObjectName("instructions")
        self.description1 = QtWidgets.QLabel(self.centralwidget)
        self.description1.setGeometry(QtCore.QRect(30, 90, 321, 31))
        self.description1.setStyleSheet("font: 12pt \"MV Boli\";\n"
"Color: rgb(255, 255, 255);")
        self.description1.setObjectName("description1")
        self.description2 = QtWidgets.QLabel(self.centralwidget)
        self.description2.setGeometry(QtCore.QRect(30, 110, 311, 21))
        self.description2.setStyleSheet("font: 12pt \"MV Boli\";\n"
"Color: rgb(255, 255, 255);")
        self.description2.setObjectName("description2")
        self.note = QtWidgets.QLabel(self.centralwidget)
        self.note.setGeometry(QtCore.QRect(0, 120, 281, 31))
        self.note.setStyleSheet("Color: rgb(255, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.note.setObjectName("note")
        self.start_reset = QtWidgets.QPushButton(self.centralwidget)
        self.start_reset.setGeometry(QtCore.QRect(110, 160, 131, 31))
        self.start_reset.setStyleSheet("font: 11pt \"Century\";\n"
"background-Color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"Color: rgb(255, 255, 255);\n"
"")
        self.start_reset.setObjectName("start_reset")
        #self.start_reset.clicked.connect(self.start_action)
        self.name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line.setGeometry(QtCore.QRect(100, 310, 171, 31))
        self.name_line.setStyleSheet("font: 14pt \"MV Boli\";")
        self.name_line.setText("")
        self.name_line.setObjectName("name_line")
        self.name_line.setDisabled(True)
        #self.name_line.returnPressed.connect(self.input_action)
        self.Colour_name = QtWidgets.QLabel(self.centralwidget)
        self.Colour_name.setGeometry(QtCore.QRect(100, 260, 171, 31))
        self.Colour_name.setStyleSheet("font: 16pt \"Century\";\n"
"Color: rgb(255, 255, 255);")
        self.Colour_name.setObjectName("Colour_name") 
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 370, 61, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("Color: rgb(255, 255, 255);\n"
"background-Color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.pushButton_2.setObjectName("pushButton_2") 
        self.colour_game = QtWidgets.QLabel(self.centralwidget)
        self.colour_game.setGeometry(QtCore.QRect(70, 30, 221, 31))
        self.colour_game.setStyleSheet("font: 18pt \"Lucida Calligraphy\";\n"
"Color: rgb(255, 255, 255);")
        self.colour_game.setObjectName("colour_game")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 210, 141, 31))
        self.label.setStyleSheet("font: 16pt \"Century\";\n"
"Color: rgb(255, 255, 255);\n"
";\n"
"background-Color: rgb(134, 15, 148);")
        self.label.setObjectName("label")
        '''
        ColourWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ColourWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 356, 21))
        self.menubar.setObjectName("menubar")
        ColourWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ColourWindow)
        self.statusbar.setObjectName("statusbar")
        ColourWindow.setStatusBar(self.statusbar)'''

        self.retranslateUi(ColourWindow)
        QtCore.QMetaObject.connectSlotsByName(ColourWindow)
        '''
        self.timer = QtCore.QTimer() 
        self.timer.timeout.connect(self.show_time) 
        self.timer.start(1000) '''

    def retranslateUi(self, ColourWindow):
        _translate = QtCore.QCoreApplication.translate
        ColourWindow.setWindowTitle(_translate("ColourWindow", "MainWindow"))
        self.instructions.setText(_translate("ColourWindow", "INSTRUCTIONS:-"))
        self.description1.setText(_translate("ColourWindow", "Enter the colour not the text!! "))
        self.description2.setText(_translate("ColourWindow", "Press Start button to start the game"))
        self.note.setText(_translate("ColourWindow", "NOTE:-Time limit for game is 30 seconds"))
        self.start_reset.setText(_translate("ColourWindow", "START/RESET"))
        self.Colour_name.setText(_translate("ColourWindow", "COLOUR NAME"))
        self.pushButton_2.setText(_translate("ColourWindow", "30"))
        self.colour_game.setText(_translate("ColourWindow", "COLOUR GAME"))
        self.label.setText(_translate("ColourWindow", "    SCORE : 0"))
'''
class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(351, 541)
        self.label = QtWidgets.QLabel(Dialog1)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 541))
        self.label.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog1)
        self.label_2.setGeometry(QtCore.QRect(100, 190, 131, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("F:/UI/images/GREZY_REVIVAL1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog1)
        self.label_3.setGeometry(QtCore.QRect(100, 500, 171, 41))
        self.label_3.setStyleSheet("font: 8pt \"Franklin Gothic Medium\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog1", "Dialog1"))
        self.label.setText(_translate("Dialog1", "TextLabel"))
        self.label_3.setText(_translate("Dialog1", "Copyrights Reserved"))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 536)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 551))
        self.label.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 200, 221, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("F:/UI/images/Backup_of_GREZY_REVIVAL.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 564)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -20, 401, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Sri Ramajayam/Desktop/UI/Phases/Phases.ui/Phase 1.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog")) '''



# ----------------------------------------------

class Login(QtWidgets.QWidget,Ui_Outsecure):
    switch_window = QtCore.pyqtSignal()
    switch_window1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.btn_newuser.clicked.connect(self.btn_newuser_handler)
        self.btn_Submit.clicked.connect(self.btn_submit_handler)

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def bool_check_username(self):
        if len(self.txt_password.text()) <= 1:
            self.pop_message(text='Enter Valid Username and Password !')
        else:
            username = self.txt_username.text()
            password = self.txt_password.text()
            conn = sqlite3.connect('Data.db')
            cursor = conn.cursor()
            cursor.execute("SELECT username,password FROM credentials")
            val = cursor.fetchall()
            if len(val) >= 1:

                for x in val:
                    if username in x[0] and password in x[1]:
                        return True
                    else:
                        pass
            else:
                self.pop_message(text="No users Found ")
                return False

    def btn_submit_handler(self):
        val = self.bool_check_username()

        if (val):
            self.pop_message(text="Welcome ")
            self.switch_window1.emit()

        else:
            self.pop_message("Invalid username or password ")

    def btn_newuser_handler(self):
        self.switch_window.emit()

class Newuser(QtWidgets.QWidget, Ui_NewUser):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.Back.clicked.connect(self.back_handler)
        self.btn_submit.clicked.connect(self.btn_submit_handler)

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


    def btn_submit_handler(self):
        self.create_db_newuser()

    def back_handler(self):
        self.switch_window.emit()

    def create_db_newuser(self):

        txt_firstname_v = self.txt_firstname.text()
        txt_lastname_v = self.txt_lastname.text()
        txt_phone_v = self.txt_phone.text()
        txt_emailid_v = self.txt_email.text()
        txt_username_v =self.txt_username.text()
        txt_password_v =self.lineEdit.text()

        if (len(txt_firstname_v) <= 1
                and len(txt_lastname_v) <= 1 and
        len(txt_phone_v) <= 9  and
        len(txt_emailid_v) <= 1  and
        len(txt_username_v) <= 1  and
        len(txt_password_v) <=1):

            """
            Logic to see if users Enter all Feilds Correctly 
            """
            self.pop_message(text = "Please Enter All Feilds ")

        else:

            conn=sqlite3.connect('Data.db')
            cursor = conn.cursor()

            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS credentials 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    fname TEXT, 
                    lname TEXT, 
                    Phone TEXT, 
                    email TEXT,
                    username TEXT, 
                    password TEXT)""")

            cursor.execute(""" INSERT INTO credentials 
                    (fname,
                    lname,
                    Phone,
                    email,
                    username, 
                    password)
                    
                VALUES 
                (?,?,?,?,?,?)
                """,(txt_firstname_v, txt_lastname_v, txt_phone_v, txt_emailid_v,txt_username_v,txt_password_v))

            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message(text="Added to Database ! ")

class Colourwindow(QtWidgets.QWidget, Ui_ColourWindow):
    #switch_window1 = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self) 
        #self.setWindowTitle("Python ")  
        #self.setGeometry(100, 100, 500, 500) 
        self.setupUi(self)    
        self.count_value = 30
        self.score_value = 0
        self.start_Flag = False
        self.Colour_list= ['Red', 'Blue', 'Green', 'Pink', 'Black', 
                   'Yellow', 'Orange', 'Purple', 'Brown','White']
        self.start_reset.clicked.connect(self.start_action)
        self.name_line.returnPressed.connect(self.input_action)
        self.timer = QtCore.QTimer() 
        self.timer.timeout.connect(self.show_time) 
        self.timer.start(1000)

    def show_time(self): 
  
        if self.start_Flag:  
            self.pushButton_2.setText(str(self.count_value))  
            if self.count_value == 0:  
                self.start_Flag = False 
                self.name_line.setDisabled(True)  
            self.count_value -= 1
    def start_action(self):  
        self.start_Flag = True 
        self.label.setText("Score : 0") 
        self.score_value = 0 
        self.count_value = 30 
        self.name_line.clear()  
        self.name_line.setEnabled(True)  
        self.random_Colour = random.choice(self.Colour_list)  
        self.random_Colour.lower() 
        self.Colour_name.setStyleSheet("font: 16pt \"Century\";\n""Color : " + self.random_Colour + ";") 
        random_text = random.choice(self.Colour_list)  
        self.Colour_name.setText(random_text) 
    def input_action(self): 
        text = self.name_line.text()  
        text.lower() 
        if text == self.random_Colour:  
            self.name_line.clear()  
            self.score_value += 1
            self.label.setText("Score : " + str(self.score_value)) 
            self.random_Colour = random.choice(self.Colour_list)  
            self.random_Colour.lower()  
            self.Colour_name.setStyleSheet("font: 16pt \"Century\";\n""Color : " + self.random_Colour + ";")  
            random_text = random.choice(self.Colour_list) 
            self.Colour_name.setText(random_text)
'''class Logo(QtWidgets.QWidget, Ui_Dialog1):
    #switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
class Wordlogo(QtWidgets.QWidget, Ui_Dialog):
    #switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self) '''

class Controller:

    def __init__(self):
        pass
    '''
    def time_sleeper(self):
        #os.popen('F:/UI/Logo/Logo.ui/Logo.py')
        self.logo=Logo()
        self.logo.show()
        time.sleep(5)
        #os.popen('F:/UI/Logo/Logo.py/Wordlogo.py')
        self.wordlogo=Wordlogo()
        self.wordlogo.show()
        time.sleep(5)
        os.popen('/greyzy_main.py')
        time.sleep(5)
        os.popen('F:/UI/Phases/Phases.py/Phase1.py')
        time.sleep(2)
        
        os.popen('/colours.py')
        time.sleep(1000)'''
    def show_login_page(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_newuser_page)
        self.login.switch_window1.connect(self.show_colour_page)
        self.login.show()

    def show_newuser_page(self):
        self.newuser = Newuser()
        self.newuser.switch_window.connect(self.show_login_page)
        self.login.close()
        self.newuser.show()
    def show_colour_page(self):
        self.colourwindow=Colourwindow()
        #self.colourwindow.switch_window.connect(self.show_login_page)
        ColourWindow = QtWidgets.QMainWindow()
        ui = Ui_ColourWindow()
        ui.setupUi(ColourWindow)
        self.login.close()
        self.colourwindow.show()




def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login_page()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()










