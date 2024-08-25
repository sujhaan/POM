from seleniumpagefactory import PageFactory

class New_placement(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
         'go_home': ('xpath','//*[@id="content"]/div[1]/div[1]/div/div/div/div/div[2]/fieldset/div[2]/div/a')
    }

    def click_go_home(self):
        self.go_home.click()