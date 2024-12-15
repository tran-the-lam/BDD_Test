import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
)


class EmployeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Human Resource Management")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.form_layout = QHBoxLayout()
        self.main_layout.addLayout(self.form_layout)

        self.label_id = QLabel("ID:")
        self.input_id = QLineEdit()
        self.label_name = QLabel("Name:")
        self.input_name = QLineEdit()
        self.label_birth_year = QLabel("Birth Year:")
        self.input_birth_year = QLineEdit()

        self.form_layout.addWidget(self.label_id)
        self.form_layout.addWidget(self.input_id)
        self.form_layout.addWidget(self.label_name)
        self.form_layout.addWidget(self.input_name)
        self.form_layout.addWidget(self.label_birth_year)
        self.form_layout.addWidget(self.input_birth_year)

        # Save button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.add_employee)
        self.main_layout.addWidget(self.save_button)

        # List of employees
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Birth Year"])
        self.main_layout.addWidget(self.table)

    def add_employee(self):

        emp_id = self.input_id.text()
        emp_name = self.input_name.text()
        emp_birth_year = self.input_birth_year.text()

        if not emp_id or not emp_name or not emp_birth_year:
            print("Please enter all fields")
            return

        # Add new item
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(emp_id))
        self.table.setItem(row_position, 1, QTableWidgetItem(emp_name))
        self.table.setItem(row_position, 2, QTableWidgetItem(emp_birth_year))

        # Clear input fields
        self.input_id.setText("")
        self.input_name.setText("")
        self.input_birth_year.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeApp()
    window.show()
    sys.exit(app.exec_())
