from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

URL = "<link to jobs search, Easy Apply needs to be checked"
MY_EMAIL = "<your email>"
MY_PASSWORD = "<your password>"
PHONE = "<your number>"


def abort_application():
    # click close button
    close_app_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_app_button.click()

    time.sleep(2)
    # click discard button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# click sign-in button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# sign in
time.sleep(4)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(MY_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(MY_PASSWORD)
password_field.send_keys(Keys.ENTER)

# get listings
time.sleep(4)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# apply for jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # click apply button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # insert phone number
        # find an <input> element where the id contains phoneNumber
        time.sleep(4)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # check submit button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("dara-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped")
            continue
        else:
            # click submit
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # click close button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped")
        continue

time.sleep(4)
driver.quit()
