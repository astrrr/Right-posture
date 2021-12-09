from main import LoginWindow
from modules import UILoginFunctions

class Login_Buttons(LoginWindow):

    def defineButtons(self):
        button = self.ui
        # ADD BUTTON
        # ///////////////////////////////////////////////////////////////
        self.ui.btn_Login.clicked.connect(self.buttonInterface)
        self.ui.btn_Register.clicked.connect(self.buttonInterface)
        self.ui.btn_Fpassword.clicked.connect(self.buttonInterface)

        self.ui.btn_Com_Register.clicked.connect(self.buttonInterface)
        self.ui.btn_Reg_Back.clicked.connect(self.buttonInterface)

        self.ui.btn_Forget_Email.clicked.connect(self.buttonInterface)
        self.ui.btn_Forget_Back.clicked.connect(self.buttonInterface)

        # KEY PRESS EVENT
        # ///////////////////////////////////////////////////////////////
        self.ui.username.keyReleaseEvent = self.enter_login
        self.ui.password.keyReleaseEvent = self.enter_login

        self.ui.Reg_username.keyReleaseEvent = self.enter_regis
        self.ui.Reg_password.keyReleaseEvent = self.enter_regis
        self.ui.Reg_password_2.keyReleaseEvent = self.enter_regis
        self.ui.Reg_email.keyReleaseEvent = self.enter_regis

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_Login":
            self.check_login()

        if btnName == "btn_Register":
            self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Register_page)

        if btnName == "btn_Fpassword":
            UILoginFunctions.animation_to_Forget(self)

        if btnName == "btn_Reg_Back":
            self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Login_page)

        if btnName == "btn_Forget_Back":
            UILoginFunctions.animation_back_to_Login(self)

        if btnName == "btn_Com_Register":
            self.check_register()