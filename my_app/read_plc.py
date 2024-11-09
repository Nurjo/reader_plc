# main.py
from hmi_popup import hmi_popup_func
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Получение данных из pop-up
data_from_hmi_popup = hmi_popup_func()
print(data_from_hmi_popup)
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
file_path_output = os.path.join(desktop_path, "output.txt")

# Путь к файлу ввода из pop-up
file_path_input = data_from_hmi_popup[2]
with open(file_path_input, 'r') as file:
    content = file.read()
    device_adr = content.split('\n')

arr_len = len(device_adr)
print(arr_len)
for i in range(arr_len):
    device_adr[i] = "https://" + device_adr[i]
print(device_adr)

spread_sheet = list(range(0, arr_len))

def take_screenshot(x1, x2):
    driver = webdriver.Chrome()
    driver.get(x1)
    time.sleep(3)
    try:
        # Код для Selenium
        sign_in_button = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.ID, 'details-button')))
        sign_in_button.click()

        proceed_unsafe_button = driver.find_element(By.ID, 'proceed-link')
        proceed_unsafe_button.click()

        login_field = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.ID, 'username')))
        login_field.send_keys(data_from_hmi_popup[0])

        password_field = driver.find_element(By.ID, 'txtPassword')
        password_field.send_keys(data_from_hmi_popup[1])
        time.sleep(1)

        lets_go_button = driver.find_element(By.ID, 'btnSubmit')
        lets_go_button.click()

        input_element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//td[@id="device_name_cell"]/input[@id="device_name"]')))
        var1 = str(i + 1) + '. Device name: ' + input_element.get_attribute('value')
        driver.save_screenshot(os.path.expanduser("~/Desktop/screenshots/" + x2 + ".png"))

        input_element = driver.find_element(By.XPATH, '//td[@id="description_cell"]/input[@id="dev_description"]')
        var2 = 'Device Description: ' + input_element.get_attribute('value')

        input_element = driver.find_element(By.ID, 'fid')
        var3 = 'Firmware: ' + input_element.get_attribute('textContent')

        input_element = driver.find_element(By.ID, 'serial_number')
        var4 = 'Serial number: ' + input_element.get_attribute('textContent')

        input_element = driver.find_element(By.ID, 'mainTask_bar')
        var5 = 'Task usage:' + input_element.get_attribute('style').replace('width:', '')

        input_element = driver.find_element(By.ID, 'currentProject')
        var6 = 'Current project: ' + input_element.get_attribute('textContent')

        return [var1, var2, var3, var4, var5, var6]
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

for i in range(arr_len):
    spread_sheet[i] = take_screenshot(device_adr[i], "Screen " + str(i))

# Запись результатов
with open(file_path_output, "w") as file:
    for item in spread_sheet:
        file.write(", ".join(item) + "\n")
print(f"Results saved to: {file_path_output}")
