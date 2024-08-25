from selenium import webdriver
import time
from SRC.Pages.Skillgun_login_page import Skillgunlogin
from SRC.Pages.Student_Dashboard import Student_dashboard
from SRC.Pages.New_placement_drive import New_placement
from SRC.Pages.Interview_schedules import Interview_schedule
from SRC.Pages.Applied_drives import Applied_drives
from SRC.Pages.Attended_drives import Attended_drives

driver = webdriver.Chrome()
driver.get('http://www.skillgun.com/StudentLogin.aspx')
time.sleep(5)

def test_login():
    login = Skillgunlogin(driver)
    driver.maximize_window()
    time.sleep(3)
    login.enter_mobile_number(7780431116)
    time.sleep(3)
    login.enter_email('sujhaan01@gmail.com')
    login.enter_password('M@rchipoya19')
    login.click_checkbox()
    time.sleep(10)
    login.click_login_button()
    time.sleep(5)
    assert 'Home' in driver.current_url

def test_new_placement():
    s_d = Student_dashboard(driver)
    s_d.click_new_placement()
    time.sleep(5)
    assert 'NewPlacementDrive' in driver.current_url


def test_New_placement():
    g_h = New_placement(driver)
    g_h.click_go_home()
    assert 'Home' in driver.current_url

def test_interview_schedules():
    inte = Student_dashboard(driver)
    inte.click_interview_schedules()
    time.sleep(5)
    assert 'Interviews' in driver.current_url

def test_Interview_scheduleback():
    go_b = Interview_schedule(driver)
    go_b.click_go_home_is()
    assert 'Home' in driver.current_url

def test_applied_drives():
    applied = Student_dashboard(driver)
    applied.click_applied_drives()
    time.sleep(5)
    assert 'AppliedDrives' in driver.current_url

def test_Applied_drives():
    g_to_h = Applied_drives(driver)
    g_to_h.applied_drives_back()
    assert 'Home' in driver.current_url

def test_attended_drives():
    attend_drive = Student_dashboard(driver)
    attend_drive.click_attended_drives()
    time.sleep(5)
    assert 'AttendedDriveDetails' in driver.current_url

def test_Attended_drives():
    back_to_home = Attended_drives(driver)
    back_to_home.click_back()
    assert 'Home' in driver.current_url

def test_course_materials():
    cour_mat = Student_dashboard(driver)
    cour_mat.click_course_materials()
    time.sleep(5)
    assert 'CourseMaterial' in driver.current_url
    driver.back()
    time.sleep(3)
    assert 'Home' in driver.current_url

def test_model_resumes():
    mod_res = Student_dashboard(driver)
    mod_res.click_model_resumes()
    time.sleep(5)
    assert 'ModelResumes' in driver.current_url
    driver.back()
    time.sleep(3)
    assert 'Home' in driver.current_url

def test_profile_settings():
    profile_setting = Student_dashboard(driver)
    profile_setting.click_profile_settings()
    time.sleep(5)
    assert 'ProfileSetting' in driver.current_url
    driver.back()
    time.sleep(3)

def test_eguru_otp():
    otp = Student_dashboard(driver)
    otp.click_get_eguru_otp()
    time.sleep(3)
    assert 'EGuruDetails' in driver.current_url
    driver.back()
    time.sleep(3)
    assert 'Home' in driver.current_url


def test_mock_report():
    mock_inter_report = Student_dashboard(driver)
    mock_inter_report.click_mock_interview_report()
    time.sleep(5)
    assert 'MockResult' in driver.current_url
    driver.back()
    time.sleep(3)
    assert 'Home' in driver.current_url

def test_software_install():
    install_software = Student_dashboard(driver)
    install_software.click_software_installation()
    time.sleep(5)
    assert 'SoftwareInstallationHelp' in driver.current_url
    driver.back()
    time.sleep(3)
    assert 'Home' in driver.current_url

def test_code_test_result():
    codeing_test_result = Student_dashboard(driver)
    codeing_test_result.click_coding_test_result()
    time.sleep(5)
    assert 'StudentCodingTestResult' in driver.current_url
    driver.back()
    time.sleep(3)
    assert 'Home' in driver.current_url

def test_interview_tips():
    mock_interview_tips = Student_dashboard(driver)
    mock_interview_tips.click_mock_interview_tips()
    time.sleep(5)
    assert 'MockInterviewTips' in driver.current_url
    driver.back()
    time.sleep(3)
    assert 'Home' in driver.current_url

def test_peer_mock_interview():
    peermock_interview = Student_dashboard(driver)
    peermock_interview.click_peer_mock_interview()
    time.sleep(5)
    assert 'StudentToStudentPeerMockInterview' in driver.current_url
    driver.back()
    time.sleep(3)
    assert 'Home' in driver.current_url

def test_self_introduction():
    self_intro = Student_dashboard(driver)
    self_intro.click_self_introduction()
    time.sleep(5)
    assert 'SelfIntroduction' in driver.current_url
    driver.back()
    time.sleep(3)
    assert 'Home' in driver.current_url


def test_coding_test_answers():
    code_test_answers = Student_dashboard(driver)
    code_test_answers.click_upload_code_test()
    time.sleep(5)
    assert 'UploadCodingTestAnswerPapers' in driver.current_url
    driver.back()
    assert 'Home' in driver.current_url


def test_QR_code():
    qr_code = Student_dashboard(driver)
    qr_code.click_your_QR_code()
    time.sleep(5)
    assert 'Student_QR_Code' in driver.current_url
    driver.back()
    assert 'Home' in driver.current_url


def test_display_attendance():
    attendance = Student_dashboard(driver)
    attendance.click_display_attendance()
    time.sleep(5)
    assert 'DisplayStudentAttendance' in driver.current_url
    driver.back()
    assert 'Home' in driver.current_url


def test_logout_button():
    logout = Student_dashboard(driver)
    logout.click_logout()
    time.sleep(5)









    

