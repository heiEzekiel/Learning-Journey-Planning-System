#Just run the script to test and rmb to pip install libs
import unittest, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.frontend_test.url import url as temp_url
from sqlalchemy.sql import text
from tests.frontend_test.db import engine as temp_engine
    
class TC209(unittest.TestCase):
    def test_temp(self):
        def read_file(filename):
            fh = open(filename, "r")
            try:
                return fh.read()
            finally:
                fh.close()
        res = False
        sql_query = read_file("test_related_db/LJPS3.sql")
        engine = temp_engine
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql = str(text(sql_query))
        text_list = sql.split(";")
        for row in text_list:
            if row != "":
                row = row + ";"
                cursor.execute(row)
                connection.commit()
        cursor.close()
        connection.close()

        url = temp_url + "frontend/learner/journey_step_two.html?job=Software%20Developer&id=601"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        ChromeDriverManager(log_level=0)
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--window-size=1920,1080') 
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        browser.get(url)
        element_present = EC.presence_of_element_located((By.ID, 'job_skills'))
        WebDriverWait(browser, 2).until(element_present)
        
        try:
            all_courses = browser.find_elements(By.ID, "all_courses")[0]
            if all_courses:
                all_courses.click()
                time.sleep(0.5)
                browser.get(browser.current_url)
                time.sleep(0.5)
                skill = browser.find_element(By.ID, "501")
                if skill:
                    skill.click()
                    checkbox = browser.find_element(By.ID, "check_501_COR001")
                    checkbox.click()
                    time.sleep(1)
                    create_btn = browser.find_element(By.ID, "modal_btn")
                    create_btn.click()
                    time.sleep(0.5)
                    verify_one = browser.find_element(By.ID, "verify_COR001")
                    if verify_one:
                        lj_name_box = browser.find_element(By.ID, "learningJourneyName")
                        lj_name_box.send_keys("LJ name LJ name LJ name LJ name LJ name L")
                        create_lj_btn = browser.find_element(By.ID, "createLJ")
                        create_lj_btn.click()
                    else:
                        self.assertTrue(res, "Failed")
                else:
                    self.assertTrue(res, "Failed")
                alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
                alert_text = alert.text
                if "Journey name has reached the maximum of 40 characters" in alert_text:
                    res = True
                    self.assertTrue(res, "Passed")
                else:
                    self.assertTrue(res, "Failed")
            else:
                self.assertTrue(res, "Failed")
        except:
            self.assertTrue(res, "Failed")
        browser.quit()
        
if __name__ == '__main__':
    unittest.main()