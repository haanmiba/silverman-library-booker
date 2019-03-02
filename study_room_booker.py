from selenium_web_driver import SeleniumWebDriver
from ub_student import UBStudent
import json
import helper_functions as hf
from selenium.webdriver.common.by import By

class StudyRoomBooker(SeleniumWebDriver):

    def __init__(self, driver_path, headless=True, timeout=10):
        SeleniumWebDriver.__init__(self, driver_path, headless=False)
        self.open_url('https://booking.lib.buffalo.edu/reserve/silverman', element_type=By.CLASS_NAME, element_value='fc-content')
    
    def book_room(self, room_number, date_string, time_string, num_hours, student):
        formatted_room_title = hf.format_room_title(time_string, date_string, room_number)
        self.browser.find_element_by_xpath("a[@title='{formatted_room_title}']")
        pass

if __name__ == '__main__':
    students = []
    with open('people.json') as f:
        data = json.load(f)
        for student in data['bookers']:
            new_student = UBStudent(student['first_name'], student['last_name'], student['ubit'])
            students.append(new_student)
    booker = StudyRoomBooker('/Users/hansbas/Programming/projects/silverman-library-auto-booker/chromedriver/chromedriver')