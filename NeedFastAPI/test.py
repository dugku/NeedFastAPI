from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import json
import requests
import sys

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()

        layout = QVBoxLayout(self)

        self.InputTodo = QLineEdit()
        self.sendToDo = QPushButton("Enter")
        self.sendToDo.clicked.connect(self.woosh)

        self.getTaskInput = QLineEdit()
        self.getTaskBut = QPushButton()
        self.getTaskBut.clicked.connect(self.doosh)


        layout.addWidget(self.InputTodo)
        layout.addWidget(self.sendToDo)
        layout.addWidget(self.getTaskInput)
        layout.addWidget(self.getTaskBut)
        widget = QWidget(self)
        widget.setGeometry(200,200,100,100)
        widget.setLayout(layout)
        self.show()
       
    def woosh(self):
        thing = self.InputTodo.text()
        dict = {
            "task":thing, 
            "due_date": "Lalala"
        }
    
        requests.post("http://127.0.0.1:8000/todo/" , json= dict)
    def doosh(self):
        ahh = self.getTaskInput.text()
        data = requests.get(f"http://127.0.0.1:8000/todo/{ahh}")
        temp = data.json()

        print(temp)

app = QApplication(sys.argv)
window = Example()
app.exec()