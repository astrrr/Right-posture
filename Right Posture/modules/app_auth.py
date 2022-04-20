from main import AuthWindow, QTimer
from modules import AppFunctions
from modules.app_temp import Debug_path
from modules.ui_login_function import UILoginFunctions

import sqlite3
import os
import re

auth_key = None
cwd = os.getcwd()
cwd = cwd+Debug_path.path
acc_path = f"{cwd}/bin/Data/Accounts.db"
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check_email(email):
    if re.fullmatch(regex, email):
        # print("Valid Email")
        return True
    else:
        # print("Invalid Email")
        return False

class Auth_system(AuthWindow):

    def change_password(self):
        global auth_key
        new_password = self.ui.Auth_new_password.text()
        email = self.ui.Forget_Email.text()
        if self.ui.Auth_key.text() == str(auth_key):
            try:
                conn = sqlite3.connect(acc_path)
                cur = conn.cursor()
                query = f"UPDATE login_info set password  = \'{new_password}\' WHERE email = \'{email}\'"
                cur.execute(query)
                conn.commit()
                conn.close()
            except sqlite3.Error as error:
                self.ui.Auth_Status.setText(error)
                Auth_system.auth_fail(self)
            finally:
                if conn:
                    conn.close()
            self.ui.Auth_Status.setText(f"Change password successfully")
            self.ui.Auth_Status.setStyleSheet("#Auth_Status { color: #50fa7b }")
            self.ui.Auth_key.setStyleSheet("#Auth_key:focus { border: 2px solid #50fa7b; }")
            self.ui.Auth_new_password.setStyleSheet("#Auth_new_password:focus { border: 2px solid #50fa7b; }")
        else:
            self.ui.Auth_Status.setText(f"Auth incorrect please try again.")
            Auth_system.auth_fail(self)

    def check_forget(self):
        global auth_key
        username = self.ui.Forget_Username.text()
        email = self.ui.Forget_Email.text()
        if len(username) == 0 or len(email) == 0:
            self.ui.Forget_Status.setText(f"Please input all fields.")
            Auth_system.forget_fail(self)
        else:
            if check_email(email):
                # SQL
                conn = sqlite3.connect(acc_path)
                cur = conn.cursor()
                query = f"SELECT email FROM login_info WHERE username = \'{username}\'"
                cur.execute(query)
                try:
                    result_pass = cur.fetchone()[0]
                    if result_pass == email:
                        auth_key = AppFunctions.generate_auth_key(5)
                        try:
                            AppFunctions.send_Email(self, text=f"Your auth key is {auth_key}", to_emails=[email])
                            UILoginFunctions.animation_to_Auth_key(self)
                            self.ui.Forget_Status.setText(f"Auth key is send to {email} please check your email.")
                            self.ui.Forget_Status.setStyleSheet("#Forget_Status { color: #50fa7b }")
                            self.ui.Forget_Username.setStyleSheet("#Forget_Username:focus { border: 2px solid #50fa7b; }")
                            self.ui.Forget_Email.setStyleSheet("#Forget_Email:focus { border: 2px solid #50fa7b; }")
                        except:
                            self.ui.Forget_Status.setText(f"No internet connection !!!")
                            Auth_system.forget_fail(self)
                            AppFunctions.notifyMe(self, "Notification", f"Fail Sending to email {email}")
                    else:
                        self.ui.Forget_Status.setText(f"Username or email is mismatch")
                        Auth_system.forget_fail(self)
                except Exception as e:
                    print(e)
                    self.ui.Forget_Status.setText(f"Username or email is mismatch")
                    Auth_system.forget_fail(self)
            else:
                Auth_system.forget_fail(self)
                self.ui.Forget_Status.setText("Invalid Email.")

    def check_login(self, guest):
        # print('acc_path : ', acc_path )
        if guest:
            self.ui.Login_Status.setText(f"Welcome Guest !")
            self.ui.Login_Status.setStyleSheet("#Login_Status { color: #50fa7b }")
            QTimer.singleShot(1200, lambda: self.open_main(True))
        if not guest:
            username = self.ui.username.text()
            password = self.ui.password.text()

            if len(username) == 0 or len(password) == 0:
                self.ui.Login_Status.setText("Please input all fields.")
                Auth_system.login_fail(self)
            else:
                conn = sqlite3.connect(acc_path)
                cur = conn.cursor()
                query = f"SELECT password FROM login_info WHERE username = \'{username}\'"
                cur.execute(query)
                try:
                    result_pass = cur.fetchone()[0]
                    if result_pass == password:
                        self.ui.Login_Status.setText(f"Welcome {username} !")
                        self.ui.Login_Status.setStyleSheet("#Login_Status { color: #50fa7b }")
                        self.ui.username.setStyleSheet("#username:focus { border: 2px solid #50fa7b; }")
                        self.ui.password.setStyleSheet("#password:focus { border: 2px solid #50fa7b; }")
                        QTimer.singleShot(1200, lambda: self.open_main(False))
                    else:
                        self.ui.Login_Status.setText("Invalid username or password")
                        Auth_system.login_fail(self)
                except Exception as e:
                    print(e)
                    self.ui.Login_Status.setText("Invalid username or password")
                    Auth_system.login_fail(self)

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
            if check_email(email):
                conn = sqlite3.connect(acc_path)
                cur = conn.cursor()
                try:
                    user_info = [username, password, email, 0, 0, 0, 0, 0, 0, 0, 0]
                    cur.execute('INSERT INTO login_info (username, password, email, period, sensitive, sitting, '
                                'dnd, discord, s_cam, s_detail, camera) VALUES (?,?,?,?,?,?,?,?,?,?,?)', user_info)
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
                except Exception as e:
                    print(e)
                    Auth_system.regis_fail(self)
                    self.ui.Reg_Status.setText("This username is already registered in the database.")
            else:
                Auth_system.regis_fail(self)
                self.ui.Reg_Status.setText("Invalid Email.")

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

    def forget_fail(self):
        self.ui.Forget_Status.setStyleSheet("#Forget_Status { color: #ff5555 }")
        self.ui.Forget_Username.setStyleSheet("#Forget_Username:focus { border: 2px solid #ff5555; }")
        self.ui.Forget_Email.setStyleSheet("#Forget_Email:focus { border: 2px solid #ff5555; }")
        UILoginFunctions.shake_window(self)

    def auth_fail(self):
        self.ui.Auth_Status.setStyleSheet("#Auth_Status { color: #ff5555 }")
        self.ui.Auth_key.setStyleSheet("#Auth_key:focus { border: 2px solid #ff5555; }")
        self.ui.Auth_new_password.setStyleSheet("#Auth_new_password:focus { border: 2px solid #ff5555; }")
        UILoginFunctions.shake_window(self)