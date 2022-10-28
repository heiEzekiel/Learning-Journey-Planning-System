#Just run the script to test and rmb to pip install libs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import url

url = url + "frontend/hr/create_role.html"
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
browser.get(url)
element_present = EC.presence_of_element_located((By.ID, 'title'))
WebDriverWait(browser, 2).until(element_present)

print("\n\n===== Results =====")
try:
    role_name_box = browser.find_element(By.ID, "role_name")
    role_desc_box = browser.find_element(By.ID, "role_desc")
    create_button = browser.find_element(By.ID, "btn")
    element_present = EC.presence_of_element_located((By.ID, 'btn'))
    WebDriverWait(browser, 2).until(element_present)
    if role_name_box and role_desc_box and create_button:
        role_name_box.send_keys("SRE Engineer")
        role_desc_box.send_keys("helloworldhelloworldhelloworldhelloworldhelloworlddhelloworldhelloworldhelloworldhelloworldhelloworlddhelloworldhelloworldhelloworldhelloworldhelloworlddhelloworldhelloworldhelloworldhelloworldhelloworlddhelloworldhelloworldhelloworldhelloworldhelloworldm")
    create_button.click()
    
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    alert_text = alert.text
    
    if "Role successfully created" in alert_text:
        browser.switch_to.alert.accept()
        print(f"\n{url}\nTest passed!")
    else:
        print(f"\n{url}\nTest failed!")
        print('Error occured')
except:
    print(f"\n{url}\nTest failed!")
browser.quit()