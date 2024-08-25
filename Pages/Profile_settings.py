from seleniumpagefactory import PageFactory

class Profile_settings(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'edit_contact_details': ('id','ContentPlaceHolder1_hlEditContact'),
        'edit_education_details': ('id','ContentPlaceHolder1_hlEditEducational'),
        'update_resume': ('id','ContentPlaceHolder1_hlUploadResume')
    }

    def click_edit_contact_details(self):
        self.edit_contact_details.click()

    def click_edit_education_details(self):
        self.edit_education_details()

    def click_update_resume(self):
        self.update_resume.click()

