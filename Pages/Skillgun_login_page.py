from seleniumpagefactory import PageFactory

class Skillgunlogin(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'MobileNumber': ('id', 'ContentPlaceHolder1_tbPhoneNumber'),
        'email': ('id','ContentPlaceHolder1_tbEmail'),
        'password':('id','ContentPlaceHolder1_tbPassword'),
        'checkbox':('id','lblPolicyAgreement'),
        'login_button':('id','ContentPlaceHolder1_btnLogin')

    }
    def enter_mobile_number(self, mbno):
        self.MobileNumber.send_keys(mbno)

    def enter_email(self, emailid):
        self.email.send_keys(emailid)

    def enter_password(self, password):
        self.password.send_keys(password)

    def click_checkbox(self):
        self.checkbox.click()

    def click_login_button(self):
        self.login_button.click()


