from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from auth.master_password import verify  # import the function

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project Password")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.label = QLabel("Welcome to Project Password")
        self.button = QPushButton("Unlock")
        self.button.clicked.connect(self.unlock)

        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def unlock(self):
        if verify():
            self.label.setText("Unlocked!")
        else:
            self.label.setText("Access Denied")
