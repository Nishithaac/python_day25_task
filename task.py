"""
Using Python Selenium, Explicit Wait, Expected Conditions and Chrome webdriver kindly do
the following task mentioned below:-
1) Go to https://www.imdb.com/search/name/
2) Fill the data given in the input Boxes, select Boxes and Drop Down menu on the
   webpage and do a search
3) DO not use sleep() method for the task
"""




# Importing necessary modules from selenium

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# Creating class for performing IMDB search
class IMDB_search:
    def __init__(self, url):
        # Initialize Chrome WebDriver with automatic driver installation
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Initialize WebDriverWait with a timeout of 10 seconds
        self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait with 10 seconds timeout
        # Store the URL for IMDb search page
        self.url = url

# Method to perform search
    def search(self):
        try:
            # Maximize the browser window
            self.driver.maximize_window()
            # Navigate to the IMDb search page
            self.driver.get(self.url)
            # Scroll down the page by 500 pixels
            self.driver.execute_script('window.scrollBy(0, 500)')

            # Click on the name option
            name_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='accordion-item-nameTextAccordion']")))
            # Clicking on the "Name" option
            self.driver.execute_script("arguments[0].click();", name_option)

            # Find the input box for name search and enter "Audrey Hepburn"
            name_input = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@data-testid='test-nametext']")))
            # Entering "Audrey Hepburn" into the name input box
            name_input.send_keys("Audrey Hepburn")



            # Click on the "Birth Date" option
            birth_option=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label[@for='accordion-item-birthDateAccordion']")))
            # Clicking on the "Birth Date" option
            self.driver.execute_script("arguments[0].click();", birth_option)

            # Fill the birth date range
            birth_input1=self.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@data-testid='birthYearMonth-start']")))
            # Entering start year "1929"
            birth_input1.send_keys("1929")
            birth_input2=self.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@data-testid='birthYearMonth-end']")))
            # Entering end year "1993"
            birth_input2.send_keys("1993")

            # Click on the "Birthday" option
            birthday=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label[@for='accordion-item-birthdayAccordion']")))
            # Clicking on the "Birthday" option
            self.driver.execute_script("arguments[0].click();", birthday)


            # Fill the exact birthday
            birthday_input=self.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@data-testid='birthday-input-test-id']")))
            # Entering exact birthday "05-04"
            birthday_input.send_keys("05-04")



            # Click on the "Awards" option
            awards_option=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label[@for='accordion-item-awardsAccordion']")))
            # Clicking on the "Awards" option
            self.driver.execute_script("arguments[0].click();", awards_option)
            # Select the "Oscar Best Actress Winners" button
            awards_input=self.wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@data-testid='test-chip-id-oscar_best_actress_winners']")))
            # Clicking on "Oscar Best Actress Winners" button
            self.driver.execute_script("arguments[0].click();", awards_input)

            # Click on the "Search" button to submit the form
            search_box=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-testid='adv-search-get-results']")))
            # Clicking on the "Search" button
            self.driver.execute_script("arguments[0].click();", search_box)


        except NoSuchElementException as e:
            # Handle the case where any element is not found and print an error message
            print(f"Element not found: {e}")
        finally:
            # Quit the WebDriver session regardless of whether the try block completes successfully or not
            self.driver.quit()


# URL of the IMDb search page for names
url = "https://www.imdb.com/search/name/"
# Creating an instance of IMDB_search class with IMDb URL
imdb = IMDB_search(url)
# Calling the start method to initiate the search
imdb.search()
