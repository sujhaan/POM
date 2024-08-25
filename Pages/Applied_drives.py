from seleniumpagefactory import PageFactory

class Applied_drives(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'go_to_home': ('xpath','//*[@id="content"]/div[1]/div[1]/div/div/div/div[1]/fieldset/div[2]/a')
    }

    def applied_drives_back(self):
        self.go_to_home.click()