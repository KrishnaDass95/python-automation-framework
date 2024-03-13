from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')


title = driver.title
print(title)

user_name_locator = driver.find_element(by=By.ID, value="user-name")
password_name_locator = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

user_name_locator.send_keys("standard_user")
password_name_locator.send_keys("secret_sauce")

login_button.click()

# xpath example
# backpack_add_to_cart_button = driver.find_element(By.XPATH, "//button[@name='add-to-cart-sauce-labs-backpack']")
# backpack_add_to_cart_button.click()

# how to deal with a dropdown list
dropdown = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))

# printing all the options
options = dropdown.options
for option in options:
    print(option.text)

dropdown.select_by_visible_text("Price (high to low)")

# finding multiple elements and clicking all of them
all_add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn.btn_primary.btn_small.btn_inventory")
for button in all_add_to_cart_buttons:
    button.click()

main_add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
main_add_to_cart_button.click()

# lets use explicit waits and 
wait = WebDriverWait(driver, 2)
checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

# # checkout_button = driver.find_element(By.ID, "checkout")
# print(checkout_button)
# checkout_button.click()

time.sleep(2)

# lets fill the final form
first_name_locator = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
last_name_locator = driver.find_element(By.CSS_SELECTOR, "input#last-name")
zip_locator = driver.find_element(By.CSS_SELECTOR, "input[data-test='postalCode']")

first_name_locator.send_keys("Krishna")
last_name_locator.send_keys("Anko")
zip_locator.send_keys("50000001")

time.sleep(2)

continue_locator = driver.find_element(By.XPATH, "//input[contains(@value, 'Continue')]")
continue_locator.click()

# do the screenshot tomorrow 
finish_button = driver.find_element(By.CSS_SELECTOR, "button.cart_button")
finish_button.click()

driver.save_screenshot("finished-page.png")

time.sleep(5)

driver.quit()