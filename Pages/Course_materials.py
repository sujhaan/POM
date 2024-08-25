from seleniumpagefactory import PageFactory

class Course_materials(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
       'css3': ('xpath','//*[@id="ContentPlaceHolder1_divCommonSub"]/fieldset/div/div/ul/li[1]/a'),
        'html_css': ('xpath','//*[@id="ContentPlaceHolder1_divCommonSub"]/fieldset/div/div/ul/li[2]/a'),
        'html5': ('xpath','//*[@id="ContentPlaceHolder1_divCommonSub"]/fieldset/div/div/ul/li[3]/a'),
        'java_script': ('xpath','//*[@id="ContentPlaceHolder1_divCommonSub"]/fieldset/div/div/ul/li[4]/a'),
        'django_material': ('xpath','//*[@id="spec"]/div/div/ul/li[1]/a'),
        'mysql_material': ('xpath','//*[@id="spec"]/div/div/ul/li[2]/a'),
        'python_material': ('xpath','//*[@id="spec"]/div/div/ul/li[3]/a'),
        'blood_relations': ('xpath','//*[@id="ContentPlaceHolder1_divAptitude"]/fieldset/div/div/ul/li[1]/a'),
        'coding_decoding': ('xpath','//*[@id="ContentPlaceHolder1_divAptitude"]/fieldset/div/div/ul/li[2]/a'),
        'data_interpretation': ('xpath','//*[@id="ContentPlaceHolder1_divAptitude"]/fieldset/div/div/ul/li[3]/a'),
        'ratios': ('xpath','//*[@id="ContentPlaceHolder1_divAptitude"]/fieldset/div/div/ul/li[4]/a'),
        'seating_arrangement': ('xpath','//*[@id="ContentPlaceHolder1_divAptitude"]/fieldset/div/div/ul/li[5]/a'),
        'time_work':('xpath','//*[@id="ContentPlaceHolder1_divAptitude"]/fieldset/div/div/ul/li[6]/a'),
        'time_distance': ('xpath','//*[@id="ContentPlaceHolder1_divAptitude"]/fieldset/div/div/ul/li[7]/a'),
        'hr_interview_questions': ('xpath','//*[@id="ContentPlaceHolder1_divIntMat"]/fieldset/div/div/ul/li[1]/a'),
        'data_science_questions': ('xpath','//*[@id="ContentPlaceHolder1_divIntMat"]/fieldset/div/div/ul/li[2]/a'),
        'django_questions': ('xpath','//*[@id="ContentPlaceHolder1_divIntMat"]/fieldset/div/div/ul/li[3]/a  '),
        'mysql_questions': ('xpath','//*[@id="ContentPlaceHolder1_divIntMat"]/fieldset/div/div/ul/li[4]/a'),
        'python_coding_questions': ('xpath','//*[@id="ContentPlaceHolder1_divIntMat"]/fieldset/div/div/ul/li[5]/a'),
        'python_question_answers': ('xpath','//*[@id="ContentPlaceHolder1_divIntMat"]/fieldset/div/div/ul/li[6]/a')
    }


    def click_css3(self):
        self.css3.click()

    def click_html_css(self):
        self.html_css.click()

    def click_html5(self):
        self.html5.click()

    def click_java_script(self):
        self.java_script.click()

    def click_django(self):
        self.django_material.click()

    def click_mysql(self):
        self.mysql_material.click()

    def click_python(self):
        self.python_material.click()

    def click_blood_relations(self):
        self.blood_relations.click()

    def click_coding_decoding(self):
        self.coding_decoding.click()

    def click_data_interpretation(self):
        self.data_interpretation.click()

    def click_ratios(self):
        self.ratio.click()

    def click_seating_arrangement(self):
        self.seating_arrangement.click()

    def click_time_work(self):
        self.time_work.click()

    def click_time_distance(self):
        self.time_distance.click()

    def click_hr_interview_qna(self):
        self.hr_interview_questions.click()

    def click_data_science(self):
        self.data_science_questions.click()

    def click_django_questions(self):
        self.django_questions.click()

    def click_mysql_questions(self):
        self.mysql_questions.click()

    def click_python_coding_questions(self):
        self.python_coding_questions.click()

    def click_python_questions(self):
        self.python_question_answers.click()

