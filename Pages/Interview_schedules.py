from seleniumpagefactory import PageFactory

class Interview_schedule(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'intesched': ('xpath','//*[@id="content"]/div[1]/div[1]/div/div/div/div/div[2]/fieldset/div[4]/a')
    }

    def click_go_home_is(self):
        self.intesched.click()