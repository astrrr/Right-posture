from main import AuthWindow
from modules.ui_login_function import UILoginFunctions
from modules.app_auth import Auth_system

class Auth_buttons(AuthWindow):

    def defineButtons(self):
        button = self.ui

        # LOGIN BUTTON
        button.btn_Login.clicked.connect(self.Login_button_Interface)
        button.btn_Register.clicked.connect(self.Login_button_Interface)
        button.btn_Fpassword.clicked.connect(self.Login_button_Interface)

        # REGISTER BUTTON
        button.btn_Com_Register.clicked.connect(self.Login_button_Interface)
        button.btn_Reg_Back.clicked.connect(self.Login_button_Interface)

        # FORGET BUTTON
        button.btn_Forget_Email.clicked.connect(self.Login_button_Interface)
        button.btn_Forget_Back.clicked.connect(self.Login_button_Interface)

        # KEY PRESS EVENT
        # ///////////////////////////////////////////////////////////////
        button.username.keyReleaseEvent = self.enter_login
        button.password.keyReleaseEvent = self.enter_login

        button.Reg_username.keyReleaseEvent = self.enter_regis
        button.Reg_password.keyReleaseEvent = self.enter_regis
        button.Reg_password_2.keyReleaseEvent = self.enter_regis
        button.Reg_email.keyReleaseEvent = self.enter_regis

    def buttonClick(self):
        button = self.ui
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_Login":
            Auth_system.check_login(self)

        if btnName == "btn_Com_Register":
            Auth_system.check_register(self)

        if btnName == "btn_Register":
            button.Login_stackedWidget.setCurrentWidget(button.Register_page)

        if btnName == "btn_Fpassword":
            UILoginFunctions.animation_to_Forget(self)

        if btnName == "btn_Reg_Back":
            button.Login_stackedWidget.setCurrentWidget(button.Login_page)

        if btnName == "btn_Forget_Back":
            UILoginFunctions.animation_back_to_Login(self)

        if btnName == "btn_Forget_Email":
            Auth_system.check_email(self)