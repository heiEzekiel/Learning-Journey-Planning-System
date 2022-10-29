#Just run the script to test and rmb to pip install libs
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "http://127.0.0.1:5500/frontend/hr/view_course.html"
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
browser.get(url)
element_present = EC.presence_of_element_located((By.ID, 'table'))
WebDriverWait(browser, 2).until(element_present)
print("\n\n===== Results =====")
try:
    thead = browser.find_element(By.ID, "table_head")
    tbody = browser.find_element(By.ID, "table_body")
    assign_button = browser.find_element(By.ID, "COR001")
    assign_button.click()
    browser.get(browser.current_url)
    time.sleep(1)
    element_present = EC.presence_of_element_located((By.ID, 'table'))
    WebDriverWait(browser, 2).until(element_present)
    add_button = browser.find_element(By.ID, "Machine learning")
    add_button.click()
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    alert_text = alert.text
    if alert_text == "Added skill to course successfully":
        browser.switch_to.alert.accept()
        print(f"\n{url}\nTest passed!")
    else:
        print(f"\n{url}\nTest failed!")
        print('Need remove before add')
except:
    print(f"\n{url}\nTest failed!")
browser.quit()