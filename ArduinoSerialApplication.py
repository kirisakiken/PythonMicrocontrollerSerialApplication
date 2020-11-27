import sys
import sqlite3
import serial
import serial.tools.list_ports as PortDetect
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem

from register import *
from login import *
from communication import *
from portError import *
from info import *

from time import sleep

global curs
global con

app = QtWidgets.QApplication(sys.argv)
MainWindow_login = QtWidgets.QMainWindow()
Ui_login = Ui_Login()
Ui_login.setupUi(MainWindow_login)
MainWindow_login.show()

MainWindow_register = QtWidgets.QMainWindow()
Ui_register = Ui_Register()
Ui_register.setupUi(MainWindow_register)

MainWindow_communication = QtWidgets.QMainWindow()
Ui_communication = Ui_Communication()
Ui_communication.setupUi(MainWindow_communication)

MainWindow_error = QtWidgets.QMainWindow()
Ui_error = Ui_Error()
Ui_error.setupUi(MainWindow_error)

MainWindow_info = QtWidgets.QMainWindow()
Ui_info = Ui_Info()
Ui_info.setupUi(MainWindow_info)

Ui_communication.tableWidget.setColumnWidth(0, 320);
Ui_communication.tableWidget.setColumnWidth(1, 90);



con = sqlite3.connect('maindb.db')
curs = con.cursor()

curs.execute("CREATE TABLE IF NOT EXISTS tblIDPW (ID INTEGER not null primary key autoincrement, Username TEXT not null, Password TEXT not null)")
curs.execute("CREATE TABLE IF NOT EXISTS tblDATA (Data TEXT not null, Status TEXT not null)")
con.commit()

def voidLogin():
    
    newID = Ui_login.textBox_id.text()
    newPW = Ui_login.textBox_pw.text()
    
    curs.execute("SELECT * FROM tblIDPW WHERE Username = '{}'".format(newID))
    data = curs.fetchall()
    con.commit()
    checkID = " "
    checkPW = " "
    
    for i in data:
        checkID = i[1]
        checkPW = i[2]
        
    if (checkID == newID and checkPW == newPW):
        
        MainWindow_login.hide()
        MainWindow_communication.show()
        
    else:
        Ui_login.textBox_id.setText("")
        Ui_login.textBox_pw.setText("")
        Ui_login.label_wrongidpw.setText("Invalid Username or Password!")
   
def voidRegister():
    
    pwPass = True
    
    regID = Ui_register.textBox_ID.text()
    regPW1 = Ui_register.textBox_PW1.text()
    regPW2 = Ui_register.textBox_PW2.text()
    
    if (regPW1 != regPW2):
        
        Ui_register.label_alreadyExists.setText("Passwords must match!")
        pwPass = False
        
    curs.execute("SELECT * FROM tblIDPW WHERE Username = '{}'".format(regID))
    data = curs.fetchall()
    con.commit()
    checkID = " "
    
    for i in data:
        
        checkID = i[1]
        
    if (regID == checkID):
        
        Ui_register.label_alreadyExists.setText("User already exists!")
        
    elif(pwPass == True):
        
        Ui_register.label_alreadyExists.setText("Register succeed!")
        Ui_register.textBox_ID.setText("")
        Ui_register.textBox_PW1.setText("")
        Ui_register.textBox_PW2.setText("")
        
        curs.execute("INSERT INTO tblIDPW(Username, Password) VALUES(?, ?)", (regID, regPW1))
        con.commit()

def voidPopRegister():
    
    MainWindow_login.hide()
    MainWindow_register.show()
    
def voidBacktoLogin():
    
    MainWindow_register.hide()
    MainWindow_login.show()
   
def voidSearchPorts():
    
    portData = PortDetect.comports()
    
    for i in range(0, len(portData)):
        portName = str(portData[i])
        portName = portName.split(" ")
        portName = str(portName[0])
        Ui_communication.comboBox_port.addItem(portName)

def voidOpenPort():
    
    global ser
    
    portName = str(Ui_communication.comboBox_port.currentText())
    portBaud = int(Ui_communication.comboBox_baud.currentText())
    
    try:
        ser = serial.Serial(port = portName, baudrate = portBaud, timeout = 1)
    except (NameError, serial.SerialException, ModuleNotFoundError):
        MainWindow_error.show()
        Ui_error.label.setText("Connection Failed!")
    else:
        sleep(1.1)
        Ui_communication.label_portStatus.setText("Connection Succeed!")
    
def voidClosePort():
    
    try:
        ser.close()
    except (NameError, serial.SerialException, ModuleNotFoundError):
        MainWindow_error.show()
        Ui_error.label.setText("Connect first!")
    else:
        Ui_communication.label_portStatus.setText("Disconnected!")

def voidSendData():
    
    global boolSend
    
    boolSend = True
    dStatus = "Sent"
    
    try:
        data = Ui_communication.textBox_data.text()
        ser.write(data.encode('utf-8'))  
    except: 
        MainWindow_error.show()
        Ui_error.label.setText("Connect first!")
    else:
        Ui_communication.label_dataStatus.setText("Data sent!")
        Ui_communication.textBox_data.setText("")
    
        curs.execute("INSERT INTO tblDATA(Data, Status) VALUES(?, ?)", (data, dStatus))
    
        reWrite()

def voidReadData():
    
    try:
        ser.readline()
    except (NameError, serial.SerialException, ModuleNotFoundError):
        MainWindow_error.show()
        Ui_error.label.setText("Connect first!")
    else:
        Ui_communication.label_Reading.setText("Waiting for data. . .")
        Ui_communication.label_dataStatus.setText("")
        
        while True:
            
            QtCore.QCoreApplication.processEvents()
            arduinoData = ser.readline()
            arduinoData = str(arduinoData)
            
            if len(arduinoData) > 3:
                
                dStatus = "Recieved"
                data = arduinoData[:-5]
                data = data[2:]
                
                curs.execute("INSERT INTO tblDATA(Data, Status) VALUES(?, ?)", (data, dStatus))
            
                reWrite()
            
                break

def reWrite():

    data = curs.execute("SELECT * FROM tblDATA")
     
    Ui_communication.tableWidget.clear()
    Ui_communication.tableWidget.setHorizontalHeaderLabels(["Message", "Sent/Recieved"])
    
    fdata = data.fetchall()
    expander = len(fdata)
    
    for row, columnvalues in enumerate(fdata):
        
        for column, value in enumerate(columnvalues):
            
            Ui_communication.tableWidget.setItem(row, column, QTableWidgetItem(str(value)))
            
            if (int(expander) > 7):
        
                Ui_communication.tableWidget.setRowCount(expander)
                
    Ui_communication.label_Reading.setText("")
    
def voidInfo():
    
    MainWindow_info.show()
    
    
def errorHide():
    
    MainWindow_error.hide()

#Login butons
Ui_login.buton_login.clicked.connect(voidLogin)
Ui_login.buton_register.clicked.connect(voidPopRegister)

#Register butons
Ui_register.buton_back.clicked.connect(voidBacktoLogin)
Ui_register.buton_register.clicked.connect(voidRegister)

#Communication butons
Ui_communication.pushButton_searchPorts.clicked.connect(voidSearchPorts)
Ui_communication.pushButton_openPort.clicked.connect(voidOpenPort)
Ui_communication.pushButton_closePort.clicked.connect(voidClosePort)
Ui_communication.pushButton_send.clicked.connect(voidSendData)
Ui_communication.pushButton_startRead.clicked.connect(voidReadData)
Ui_communication.pushButton.clicked.connect(voidInfo)
#Ui_communication.pushButton_stopRead.clicked.connect(voidStopReading)

Ui_error.pushButton_ok.clicked.connect(errorHide)
#-----------------------#
sys.exit(app.exec_())












