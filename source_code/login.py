from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
import sys

class CustomMessageBox(QMessageBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_text = ""

    def showEvent(self, event):
        self.message_text = self.text()
        super().showEvent(event)
        
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.msg_box = None

    def initUI(self):
        self.setWindowTitle("Login Screen")
        self.setGeometry(100, 100, 300, 200)

        # username
        self.username_label = QLabel("Username:", self)
        self.username_label.move(20, 30)
        self.username_input = QLineEdit(self)
        self.username_input.move(120, 30)

        # password
        self.password_label = QLabel("Password:", self)
        self.password_label.move(20, 70)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.move(120, 70)

        # login button
        self.login_button = QPushButton("Login", self)
        self.login_button.move(120, 110)
        self.login_button.clicked.connect(self.check_login)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "1234":
            self.msg_box = CustomMessageBox()
            self.msg_box.setIcon(QMessageBox.Information)
            self.msg_box.setText("Login Successful")
            self.msg_box.setWindowTitle("Alert")
            self.msg_box.exec_()
            print(f"MessageBox Content: {self.msg_box.message_text}")
        elif len(username) == 0 or len(password) == 0:
            self.msg_box = CustomMessageBox()
            self.msg_box.setIcon(QMessageBox.Warning)
            self.msg_box.setText("Please enter username and password!")
            self.msg_box.setWindowTitle("Error")
            self.msg_box.exec_()
            print(f"MessageBox Content: {self.msg_box.message_text}")
        else:
            self.msg_box = CustomMessageBox()
            self.msg_box.setIcon(QMessageBox.Warning)
            self.msg_box.setText("Wrong username or wrong password!")
            self.msg_box.setWindowTitle("Error")
            self.msg_box.exec_()
            print(f"MessageBox Content: {self.msg_box.message_text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())