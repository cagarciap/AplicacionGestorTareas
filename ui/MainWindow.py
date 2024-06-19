from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox, QDesktopWidget
from ui.TaskItem import TaskItem 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestor de Tareas")
        self.setGeometry(100, 100, 1000, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        input_layout = QHBoxLayout()

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Add new task")
        self.task_input.setFixedSize(500, 50)
        input_layout.addWidget(self.task_input)

        self.add_button = QPushButton("Add Task", self)
        self.add_button.setFixedSize(500, 50)
        self.add_button.clicked.connect(self.add_task)
        input_layout.addWidget(self.add_button)

        self.layout.addLayout(input_layout)

        self.task_list = QListWidget(self)
        self.layout.addWidget(self.task_list)

        self.central_widget.setLayout(self.layout)

        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def add_task(self):
        task_text = self.task_input.text()
        if not task_text.strip():
            QMessageBox.warning(self, "Warning", "The task cannot be empty")
            return

        task_item = TaskItem(task_text, self.delete_task)

        item = QListWidgetItem(self.task_list)
        item.setSizeHint(task_item.sizeHint())
        self.task_list.addItem(item)
        self.task_list.setItemWidget(item, task_item)

        self.task_input.clear()

    def delete_task(self):
        button = self.sender()
        if button:
            task_item = button.parent()
            item = self.task_list.indexAt(task_item.pos()).row()
            self.task_list.takeItem(item)
