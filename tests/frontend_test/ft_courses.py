from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = "http://127.0.0.1:5500/frontend/hr/view_course.html"

def main(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.get(url)
    element_present = EC.presence_of_element_located((By.ID, 'table'))
    WebDriverWait(browser, 2).until(element_present)
    print("\n\n===== Results =====")
    try:
        pass
        thead = browser.find_element(By.ID, "table_head")
        tbody = browser.find_element(By.ID, "table_body")
        if thead and tbody:
            print(f"\n{url}\nTest passed!")
    except:
        print(f"\n{url}\nTest failed!")
    browser.quit()
    
main(url)