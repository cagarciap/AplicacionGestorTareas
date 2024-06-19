from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout

class TaskItem(QWidget):
    def __init__(self, task_name, delete_callback):
        super().__init__()
        self.layout = QHBoxLayout()

        self.task_label = QLabel(task_name)
        self.delete_button = QPushButton("Delete Task")
        self.delete_button.clicked.connect(delete_callback)

        self.layout.addWidget(self.task_label)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)
