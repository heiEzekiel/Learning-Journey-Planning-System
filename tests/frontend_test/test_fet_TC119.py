#Just run the script to test and rmb to pip install libs
import unittest
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

class TC119(unittest.TestCase):
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

        url = temp_url + "frontend/hr/HR_roles.html"
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
            check_list = ["Data Analyst", "Software Developer"]
            thead = browser.find_element(By.ID, "table_head")
            tbody = browser.find_element(By.ID, "table_body")
            list_table_body = tbody.find_elements(By.TAG_NAME, "tr")
            for row in list_table_body:
                list_row = row.find_elements(By.TAG_NAME, "td")
                role_name = list_row[0].get_attribute('innerText')
                if role_name in check_list:
                    check_list.remove(role_name)
            if thead and tbody and not check_list:
                res = True
                self.assertTrue(res, "Passed")
            else:
                self.assertTrue(res, "Failed")
        except:
            self.assertTrue(res, "Failed")
        browser.quit()