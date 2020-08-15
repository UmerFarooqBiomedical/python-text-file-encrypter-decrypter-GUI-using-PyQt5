# -*- coding: utf-8 -*-
"""

Created on Sat Aug 15 14:23:16 2020

GUI File
"""

from PyQt5.QtWidgets import QComboBox, QMessageBox, QFileDialog, QLineEdit, QLabel, QGridLayout, QApplication, QPushButton, QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import sys
from datetime import datetime


class MyWindow(QWidget):

  def __init__(self, parent=None):
    super(MyWindow, self).__init__(parent)
    
    self.title = "Text File Encrypter"
    self.top = 50
    self.left = 50
    self.width = 600
    self.height = 300

    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)
    self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
    self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

    self.InitUI()
    self.show() 
    
  def InitUI(self):
    grid = QGridLayout()
    
    self.button = QPushButton(QtGui.QIcon("open_file_icon.png"),  "Browse", self)
    self.button1 = QPushButton(QtGui.QIcon("run_icon.png"),  "Run", self)
    
    self.lineedit = QLineEdit(self)
    self.lineedit1 = QLineEdit()
    self.lineedit2 = QLineEdit()
    
    self.label1 = QLabel("Process type: ")
    self.label2 = QLabel("Encryption Key [ Range 1 - 90 ]: ")
    self.label3 = QLabel("Input File name: ")
    self.label4 = QLabel("Output filename: ")
    
    self.combo = QComboBox()
    self.combo.addItem("Encryption")
    self.combo.addItem("Decryption")
    
    self.button.clicked.connect(self.openFileNameDialog)
    self.lineedit1.setFixedSize(90,15)
    self.lineedit1.setText("0")
    self.lineedit1.setAlignment(Qt.AlignLeft)
    self.label2.setAlignment(Qt.AlignRight)
    self.validator1 = QtGui.QIntValidator(1, 90, self)
    self.lineedit1.setValidator(self.validator1)
    self.lineedit2.setFixedSize(90,15)
    self.button1.clicked.connect(self.ciphering)    
    
    grid.addWidget(self.label1, 2, 1)
    grid.addWidget(self.combo, 2, 2)
    grid.addWidget(self.label3, 1, 1)
    grid.addWidget(self.button, 1, 3)
    grid.addWidget(self.lineedit, 1, 2)
    grid.addWidget(self.lineedit1, 3, 2)
    grid.addWidget(self.label2, 3, 1)
    grid.addWidget(self.lineedit2, 4, 2)
    grid.addWidget(self.label4, 4, 1)
    grid.addWidget(self.button1, 6, 3)
    
    self.setLayout(grid)
    
  def openFileNameDialog(self):
      options = QFileDialog.Options()
      options |= QFileDialog.DontUseNativeDialog
      global filelist
      fileName, _ = QFileDialog.getOpenFileName(self,"Select Text file", "","Text Files (*.txt)", options=options)
      if not fileName:
        fileName = None
      print(fileName)
      self.lineedit.setText(fileName)
        
  def ciphering(self):
    self.filename = self.lineedit.text()
    self.optfilename = self.lineedit2.text()
    self.process = self.combo.currentText()
    self.key = self.lineedit1.text()

    ##########################

    password_key = int(self.key)
    store = ''
    Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz' \
              '!@#$%&*(){}[]<>/\|";:\n-=+.,?0123456789'
    now=datetime.now()
    print(now)

    option_1 = self.process
    if option_1 == 'Encryption':
        print('Ok Sir!..You Selected({0})'.format(option_1))
        file = self.filename
        if password_key == 0:
          QMessageBox.critical(self, "Incorrect Encryption Key Entered", "Please enter Encryption key in range of 1 - 90.")
        else:
            print("password key: ", password_key)
            if file.endswith('.txt'):
                try:
                    file = open(file, 'r').read()
                    print('Congratualtions output file saved.')
                except:
                    print('Filename Error: Please! Enter File name in txt form/Enter correct address of file.')
                for i in file:
                    if i in Letters:
                        number = Letters.find(i)
                        try:
                            number = number + int(password_key)
                        except:
                            print('Key Error: You Enter a Incorrect key.')
                            break
                        if number >= len(Letters):
                            number = number - len(Letters)
                        elif number < 0:
                            number = number + len(Letters)
                        store = store + Letters[number]
                    else:
                        store = store + i
                    save_file = open('{}.txt'.format(self.optfilename), 'w')
                    save_file.write(store)
                    save_file.close()
                QMessageBox.about(self, "Process completed.", "Congratulations! {} successfully done.".format(self.process))
            else:
                QMessageBox.critical(self, "Filename Error", "Please! Enter txt form only.")
        
          
    elif option_1 == 'Decryption':
        print('Ok Sir!..You Selected({0})'.format(option_1))

        file = self.filename
        if password_key == 0:
          QMessageBox.critical(self, "Incorrect Encryption Key Entered", "Please enter Encryption key in range of 1 - 90.")
        else:
            if file.endswith('.txt'):
                try:
                    file = open(file, 'r').read()
                    print('Congratualtions output file saved.')

                except:
                    print('Filename Error: Please! Enter File name in txt form.')
                for i in file:
                    if i in Letters:
                        number = Letters.find(i)
                        try:
                            number = number - int(password_key)
                        except:
                            print('Key Error: You Enter a Incorrect key.')
                            break
                        if number >= len(Letters):
                            number = number - len(Letters)
                        elif number < 0:
                            number = number + len(Letters)
                        store = store + Letters[number]
                    else:
                        store = store + i
                    save_file = open('{}.txt'.format(self.optfilename), 'w')
                    save_file.write(store)
                    save_file.close() 
                QMessageBox.about(self, "Process completed.", "Congratulations! {} successfully done.".format(self.process))
            else:
                QMessageBox.critical(self, "Filename Error", "Please! Enter txt form only.")

if __name__ == "__main__":    
  App = QApplication(sys.argv)
  window = MyWindow()
  sys.exit(App.exec())