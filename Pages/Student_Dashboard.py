from seleniumpagefactory import PageFactory

class Student_dashboard(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'new_placement': ('id','ContentPlaceHolder1_ahrefnewdrive'),
        'interview_schedules': ('id','ContentPlaceHolder1_ahrefInterview'),
        'applied_drives': ('id','ContentPlaceHolder1_ahrefapplieddrive'),
        'attended_drives': ('id','ContentPlaceHolder1_ahrefattenddrive'),
        'course_materials': ('xpath','//*[@id="a1"]'),
        'model_resumes': ('id','ContentPlaceHolder1_a2'),
        'profile_settings': ('xpath','//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[3]/div[3]/a'),
        'get_eguru_otp': ('id','ContentPlaceHolder1_ahrefEguruDetails'),
        'mock_interview_report': ('xpath','//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[4]/div[1]/a'),
        'software_installation': ('xpath','//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[4]/div[2]/a'),
        'coding_test_result': ('xpath','//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[4]/div[3]/a'),
        'mock_interview_tips': ('xpath','//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[4]/div[4]/a'),
        'peer_mock_interview': ('xpath','//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[5]/div[1]/a'),
        'self_introduction': ('xpath','//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[5]/div[2]/a'),
        'upload_coding_test_answer': ('xpath','//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[5]/div[3]/a'),
        'your_QR_code': ('xpath','//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[5]/div[4]/a'),
        'display_attendance': ('xpath','//*[@id="content"]/div/div/div/div/div/div/strong/strong/div[6]/div/a'),
        'logout_button': ('xpath','//*[@id="ContentPlaceHolder1_btnLogout"]')
    }

    def click_new_placement(self):
        self.new_placement.click()

    def click_interview_schedules(self):
        self.interview_schedules.click()

    def click_applied_drives(self):
        self.applied_drives.click()

    def click_attended_drives(self):
        self.attended_drives.click()

    def click_course_materials(self):
        self.course_materials.click()

    def click_model_resumes(self):
        self.model_resumes.click()

    def click_profile_settings(self):
        self.profile_settings.click()

    def click_get_eguru_otp(self):
        self.get_eguru_otp.click()

    def click_mock_interview_report(self):
        self.mock_interview_report.click()

    def click_software_installation(self):
        self.software_installation.click()

    def click_coding_test_result(self):
        self.coding_test_result.click()

    def click_mock_interview_tips(self):
        self.mock_interview_tips.click()

    def click_peer_mock_interview(self):
        self.peer_mock_interview.click()

    def click_self_introduction(self):
        self.self_introduction.click()

    def click_upload_code_test(self):
        self.upload_coding_test_answer.click()

    def click_your_QR_code(self):
        self.your_QR_code.click()

    def click_display_attendance(self):
        self.display_attendance.click()

    def click_logout(self):
        self.logout_button.click()

