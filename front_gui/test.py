from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import json
import requests
import sys
import random

class ListWidget(QWidget):
    def __init__(self, parent=None):
        super(ListWidget,self).__init__()

        ListWidgetLayout = QHBoxLayout(self)
        self.Todo_Label = QLabel()
        self.Complete = QPushButton("Complete")
        self.Complete.clicked.connect(self.complete_todo)
        self.num = []
        ListWidgetLayout.addWidget(self.Todo_Label)
        ListWidgetLayout.addWidget(self.Complete)

    def complete_todo(self):
        print("Yes")
class Example(QMainWindow):
    def __init__(self):
        super(Example,self).__init__()

        frame_layout = QVBoxLayout()
        #Hor_Frame_Layout = QHBoxLayout()

        framest = QFrame(self)
        framest.setGeometry(20,25,500,50)
        framest.setStyleSheet("background: lightblue")

        framest_layout = QHBoxLayout(framest)
        self.input_todo = QLineEdit(framest)
        self.enter_todo = QPushButton("Enter a Todo", framest)
        self.enter_todo.clicked.connect(self.Enter_Todo)
        self.delete_todo = QPushButton("Delete",framest)
        self.delete_todo.clicked.connect(self.delete)
        framest_layout.addWidget(self.input_todo)
        framest_layout.addWidget(self.enter_todo)
        framest_layout.addWidget(self.delete_todo)
        frame_layout.addWidget(framest)

        list_frame = QFrame(self)
        list_frame.setGeometry(20,75,500,700)
        
        self.Todo_List = QListWidget(list_frame)
        self.Todo_List.setGeometry(0,0,500,700)
        frame_layout.addWidget(list_frame)

        """Note_Frame = QFrame()
        Note_Frame.setGeometry(20,20,100,100)
        Note_Frame.setStyleSheet("background: red")
        Hor_Frame_Layout.addWidget(Note_Frame)


        frame_layout.addLayout(Hor_Frame_Layout)"""
        main = QWidget(self)
        main.setGeometry(50,50,900,700)
        self.show()
    def Enter_Todo(self):
        text = self.input_todo.text()
        self.item = QListWidgetItem()

        TodoWidget = ListWidget()
        TodoWidget.Todo_Label.setText(text)
        TodoWidget.num.append(self.index + 1)

        self.item.setSizeHint(TodoWidget.sizeHint())

        self.Todo_List.addItem(self.item)
        self.Todo_List.setItemWidget(self.item, TodoWidget)

    def delete(self):
        TodoWidget = ListWidget()
        print(TodoWidget.num)




app = QApplication(sys.argv)
window = Example()
app.exec()