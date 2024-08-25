from seleniumpagefactory import PageFactory

class Edit_contact_details(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'contact_name': ('id','ContentPlaceHolder1_tbName'),
        'contact_number': ('id,','ContentPlaceHolder1_tbContactNumber'),
        'check_box': ('xpath','//*[@id="ContentPlaceHolder1_RadioButtonList1"]/tbody/tr/td[1]/label'),
        'primary_mail': ('id','ContentPlaceHolder1_tbEmail'),
        'address_line': ('id','ContentPlaceHolder1_tbPALine1'),
        'permanent_residence_city': ('id','ContentPlaceHolder1_tbPACity'),
        'permanent_residence_state': ('id','id="ContentPlaceHolder1_ddlPAState"'),
        'current_address_line': ('xpath','//*[@id="ContentPlaceHolder1_tbCALine1"]'),
        'current_city': ('xpath','//*[@id="ContentPlaceHolder1_tbCACity"]'),
        'current_state': ('xpath','//*[@id="ContentPlaceHolder1_ddlCAState"]'),
        'cancel': ('id','ContentPlaceHolder1_btncancel'),
        'save_details': ('id','ContentPlaceHolder1_btnSubmit')
    }

    def enter_contact_name(self):
        self.contact_name.send_keys()

    def enter_contact_number(self):
        self.contact_number.send_keys()

    def click_check_box(self):
        self.check_box.click()

    def enter_primary_mail(self):
        self.primary_mail.send_keys()

    def enter_address_line(self):
        self.address_line.send_keys()

    def enter_permanent_city(self):
        self.permanent_residence_city.send_keys()

    def enter_permanent_state(self):
        self.permanent_residence_state.send_keys()

    def enter_current_address(self):
        self.current_address_line.send_keys()

    def enter_current_city(self):
        self.current_city.send_keys()

    def enter_current_state(self):
        self.current_state.send_keys()

    def click_cancel(self):
        self.cancel.click()

    def click_save(self):
        self.save_details.click()