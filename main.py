import time
import random
from selenium import webdriver
from datetime import datetime
from config import FCPS_PASSWORD, FCPS_EMAIL, NAME, URL, TOPICS, ENABLE_NEGATIVE, ENABLE_POSITIVE, OS

driver_location = None


# Multi OS support coming when I have the time
if OS.upper() == "WINDOWS":
    driver_location = 'driver/chromedriver.exe'
elif OS.upper() == "MAC":
    driver_location = 'driver/chromedriver.exe'
elif OS.upper() == "LINUX":
    driver_location = 'driver/chromedriver.exe'
else:
    print(f'NOT VALID OS OPTION\nYOU PUT "{OS}"')
    exit(405)

if driver_location is None:
    print("ERROR COULD NOT SET DRIVER LOCATION!")
    exit(406)

print(f"Script started - Waiting for 08:31AM!")

while True:
    x = datetime.today().strftime("%A")
    y = datetime.today().strftime("%I:%M%p")
    if x == "Monday" and y == f"08:31AM":
        if ENABLE_NEGATIVE is True:
            max1 = 2
        else:
            max1 = 1
        if ENABLE_POSITIVE is True:
            min1 = 0
        else:
            min1 = 1

        if max1 == 1 and min1 == 1:
            print("BOTH POSITIVE AND NEGATIVE ARE DISABLED THE ONLY VALID OPTION IS MIXED")

        feelings = random.randint(min1, max1)

        random_topic_1 = random.choice(TOPICS)
        random_topic_2 = random.choice(TOPICS)
        while random_topic_1 == random_topic_2:
            random_topic_2 = random.choice(TOPICS)

        option = webdriver.ChromeOptions()
        option.add_argument("--incognito")
        browser = webdriver.Chrome(driver_location, options=option)
        browser.get(f"{URL}")
        if browser.current_url != URL and "https://accounts.google.com/signin/" in str(browser.current_url):
            enter_email = browser.find_elements_by_class_name("whsOnd")
            enter_email[0].send_keys(f"{FCPS_EMAIL}")
            next_button = browser.find_elements_by_class_name("VfPpkd-RLmnJb")
            next_button[0].click()
            time.sleep(3)
            enter_password = browser.find_elements_by_class_name("whsOnd")
            enter_password[0].send_keys(f"{FCPS_PASSWORD}")
            next_button = browser.find_elements_by_class_name("VfPpkd-RLmnJb")
            next_button[0].click()
            time.sleep(3)
        if browser.current_url == URL:
            try:
                text = f"Today I will be working on {random_topic_1}, and {random_topic_2} to get prepared for the week."
                name_box = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
                feeling_boxes = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelText")
                what_am_doing_today = browser.find_elements_by_class_name("quantumWizTextinputPapertextareaInput")
                submit = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")

                name_box[0].send_keys(f"{NAME}")
                feeling_boxes[feelings].click()
                what_am_doing_today[0].send_keys(text)
                submit[0].click()
               #browser.close()
                print(f"Submitted google form at:\nURL: {URL}\nText: {text}\nFeeling Box (0 = Happy 1 = Mixed 2 = Bad): {feelings}")
                exit(0)
            except Exception as e:
                print(e)
                print("")
                print("oh shit there was an error please send me a message w/ the error so ik how to fix LMAO")
                print("Discord: Yousef#9999")
                exit(404)
        else:
            print(f"ERROR! I am supposed to submit a Google Form to {URL} but I was sent to {browser.current_url}")
            exit(403)

    time.sleep(60)


# Exit Codes:
# 404: Failed to submit form error: unknown
# 403: After logging in google sent the browser to a diff URL
# 405: NOT SUPPORTED OS
# 406: Could not set driver location
#
#
# 1: It honestly depends I don't overwrite any codes I just make them
# 0: Script ran as intended (I think)
# -1: Forcefully closed the program (ignore lol)
