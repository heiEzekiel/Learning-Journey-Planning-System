#Just run the script to test and rmb to pip install libs
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
    result = browser.find_element(By.ID, "res")
    if result:
        if result.get_attribute('innerText') == "No records found":
            print(f"\n{url}\nTest passed!")
    else:
        print(f"\n{url}\nTest failed!")
        print('Error occured')
except:
    print(f"\n{url}\nTest failed!")
browser.quit()