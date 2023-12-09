import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')

# driver_path = '/usr/share/doc/chromium-driver'  # Set the executable path here
driver = webdriver.Chrome()

driver.get("https://banks.az/en/services/currency-rates")
time.sleep(2)
x = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'style_one-item__OPF0z')))

# for i in x:
print(x[1].text)
my_dict = {}
for i in range(5, len(x)):
    print(x[i].text)
driver.close()

