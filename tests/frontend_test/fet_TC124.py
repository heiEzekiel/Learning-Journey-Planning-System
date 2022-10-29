#Just run the script to test and rmb to pip install libs
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import url

url = url + "frontend/hr/HR_roles.html"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--window-size=1920,1080') 
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
browser.get(url)
element_present = EC.presence_of_element_located((By.ID, 'table'))
WebDriverWait(browser, 2).until(element_present)

print("\n\n===== Results =====")
try:
    thead = browser.find_element(By.ID, "table_head")
    tbody = browser.find_element(By.ID, "table_body")
    role = browser.find_element(By.ID, "Data Analyst")
    edit_btn = browser.find_element(By.ID, "edit_602")
    if thead and tbody and role and edit_btn:
        edit_btn.click()
        time.sleep(1)
        browser.get(browser.current_url)
        role_name_box = browser.find_element(By.ID, "rname")
        role_desc_box = browser.find_element(By.ID, "roledesc")
        if role_name_box and role_desc_box:
            role_name_box.clear()
            role_name_box.send_keys("Data Analyst Expert")
            role_desc_box.clear()
            role_desc_box.send_keys("Suitable for people who loves number")
            
            update_btn = browser.find_element(By.ID, "update_btn")
            update_btn.click()
        alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
        alert_text = alert.text
        if "Updated successfully" in alert_text:
            browser.switch_to.alert.accept()
            print(f"\n{url}\nTest passed!")
        else:
            print(f"\n{url}\nTest failed!")
            print('Error occured')
    else:
        print(f"\n{url}\nTest failed!")
        print('Error occured')
except:
    print(f"\n{url}\nTest failed!")
browser.quit()