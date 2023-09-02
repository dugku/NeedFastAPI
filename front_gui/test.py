from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import json
import requests
import sys
import random

class ListWidget(QWidget):
    def __init__(self,Todo_List, parent=None):
        super(ListWidget,self).__init__(parent)

        self.Todo_List = Todo_List


        ListWidgetLayout = QHBoxLayout(self)
        self.Todo_Label = QLabel()
        self.Complete = QPushButton("Complete")
        self.Complete.clicked.connect(self.complete_todo)

        self.delete = QPushButton("Delete")
        self.delete.clicked.connect(self.delete_Task)

        self.hidden_labelId = QLabel()
        self.hidden_labelId.hide()
        
        ListWidgetLayout.addWidget(self.Todo_Label)
        ListWidgetLayout.addWidget(self.Complete)
        ListWidgetLayout.addWidget(self.delete)
        ListWidgetLayout.addWidget(self.hidden_labelId)

    def complete_todo(self):
        self.Todo_Label.setText("Completed")
        idNum = self.hidden_labelId.text()
        completeRequest = requests.put(f'http://127.0.0.1:8000/complete/{idNum}') 

    def delete_Task(self, e):
        selected_item = self.Todo_List.currentItem()
        if selected_item:
            self.Todo_List.takeItem(self.Todo_List.row(selected_item))
        #need to make it so that tasks are deleted too
        idNum = int(self.hidden_labelId.text())
        deleteRequest = requests.delete(f'http://127.0.0.1:8000/delete/{idNum}')

class Example(QWidget):
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


        self.index = 0

        my_tasks = requests.get("http://127.0.0.1:8000/todo")
        JsonTask = my_tasks.json()
        for i in JsonTask:
            self.item = QListWidgetItem()
            TodoWidget = ListWidget(self.Todo_List)
            TodoWidget.Todo_Label.setText(i['String_Todo'])
            TodoWidget.hidden_labelId.setText(str(i['task_id']))
            #Need to add request so that I can query the API

            self.item.setSizeHint(TodoWidget.sizeHint())

            self.Todo_List.addItem(self.item)
            self.Todo_List.setItemWidget(self.item, TodoWidget)

        """Note_Frame = QFrame()
        Note_Frame.setGeometry(20,20,100,100)
        Note_Frame.setStyleSheet("background: red")
        Hor_Frame_Layout.addWidget(Note_Frame)


        frame_layout.addLayout(Hor_Frame_Layout)"""
        main = QWidget(self)
        main.setGeometry(900,700,50,50)
        self.show()

    def Enter_Todo(self):

        text = self.input_todo.text()
        self.item = QListWidgetItem()
        TodoWidget = ListWidget(self.Todo_List)
        TodoWidget.Todo_Label.setText(text)
        #Need to add request so that I can query the API
        postDict = {
            'task': self.input_todo.text(),
            'due_date': "WIP",
            'complete': False
        }
        TodoPost = requests.post('http://127.0.0.1:8000/todo/',json=postDict)



        self.item.setSizeHint(TodoWidget.sizeHint())

        self.Todo_List.addItem(self.item)
        self.Todo_List.setItemWidget(self.item, TodoWidget)

    def delete(self):
        print("Hi")




app = QApplication(sys.argv)
window = Example()
app.exec()