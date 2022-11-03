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
    
class TC142(unittest.TestCase):
    def test_temp(self):
        def read_file(filename):
            fh = open(filename, "r")
            try:
                return fh.read()
            finally:
                fh.close()
        res = False
        sql_query = read_file("test_related_db/LJPS.sql")
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

        url = temp_url + "frontend/hr/skills.html"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        ChromeDriverManager(log_level=0)
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--window-size=1920,1080') 
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        browser.get(url)
        element_present = EC.presence_of_element_located((By.ID, 'table'))
        WebDriverWait(browser, 2).until(element_present)

        try:
            thead = browser.find_element(By.ID, "table_head")
            tbody = browser.find_element(By.ID, "table_body")
            skill = browser.find_element(By.ID, "Python 3")
            edit_btn = browser.find_element(By.ID, "edit_Python 3")
            if thead and tbody and skill and edit_btn:
                edit_btn.click()
                time.sleep(1)
                browser.get(browser.current_url)
                skill_name_box = browser.find_element(By.ID, "skill_Name")
                skill_desc_box = browser.find_element(By.ID, "skill_Description")
                if skill_name_box and skill_desc_box:
                    skill_name_box.clear()
                    skill_name_box.send_keys("PythonPythonPythonPythonPythonPythonPythonPythonPyt")
                    skill_desc_box.clear()
                    skill_desc_box.send_keys("Python is the best")
                    
                    update_btn = browser.find_element(By.ID, "update_btn")
                    update_btn.click()
                alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
                alert_text = alert.text
                if "Update skill name has reached the maximum of 50 characters" in alert_text:
                    browser.switch_to.alert.accept()
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