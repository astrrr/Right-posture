from main import LoginWindow
from modules.ui_login_function import UILoginFunctions
import sqlite3

class Auth_system(LoginWindow):

    def check_register(self):
        username = self.ui.Reg_username.text()
        password = self.ui.Reg_password.text()
        con_Password = self.ui.Reg_password_2.text()
        email = self.ui.Reg_email.text()

        if len(username) == 0 or len(password) == 0 or len(con_Password) == 0 or len(email) == 0:
            self.ui.Reg_Status.setText("Please fill in all inputs.")
            Auth_system.regis_fail(self)
        elif password != con_Password:
            self.ui.Reg_Status.setText("Passwords do not match.")
            Auth_system.regis_fail(self)
        else:
            conn = sqlite3.connect("bin/Data/Accounts.db")
            cur = conn.cursor()
            user_info = [username, password, email]
            try:
                cur.execute('INSERT INTO login_info (username, password, email) VALUES (?,?,?)', user_info)
                conn.commit()
                conn.close()
                self.ui.Reg_username.clear()
                self.ui.Reg_password.clear()
                self.ui.Reg_password_2.clear()
                self.ui.Reg_email.clear()
                self.ui.Reg_Status.setStyleSheet("#Reg_Status { color: #50fa7b }")
                self.ui.Reg_username.setStyleSheet("#Reg_username:focus { border: 2px solid rgb(91, 101, 124); }")
                self.ui.Reg_password.setStyleSheet("#Reg_password:focus { border: 2px solid rgb(91, 101, 124); }")
                self.ui.Reg_password_2.setStyleSheet("#Reg_password_2:focus { border: 2px solid rgb(91, 101, 124); }")
                self.ui.Reg_email.setStyleSheet("#Reg_email:focus { border: 2px solid rgb(91, 101, 124); }")
                self.ui.Reg_Status.setText("Register Complete !")
            except:
                self.ui.Reg_Status.setText("This username is already registered in the database.")
                Auth_system.regis_fail(self)

    def regis_fail(self):
        self.ui.Reg_Status.setStyleSheet("#Reg_Status { color: #ff5555 }")
        self.ui.Reg_username.setStyleSheet("#Reg_username:focus { border: 2px solid #ff5555; }")
        self.ui.Reg_password.setStyleSheet("#Reg_password:focus { border: 2px solid #ff5555; }")
        self.ui.Reg_password_2.setStyleSheet("#Reg_password_2:focus { border: 2px solid #ff5555; }")
        self.ui.Reg_email.setStyleSheet("#Reg_email:focus { border: 2px solid #ff5555; }")
        UILoginFunctions.shake_window(self)

    def login_fail(self):
        self.ui.Login_Status.setStyleSheet("#Login_Status { color: #ff5555 }")
        self.ui.username.setStyleSheet("#username:focus { border: 2px solid #ff5555; }")
        self.ui.password.setStyleSheet("#password:focus { border: 2px solid #ff5555; }")
        UILoginFunctions.shake_window(self)