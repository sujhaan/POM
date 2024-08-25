from seleniumpagefactory import PageFactory

class Attended_drives(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'drives_back': ('xpath','//*[@id="content"]/div[1]/div[1]/div/div/div/div/div[4]/a')
    }

    def click_back(self):
        self.drives_back.click()
