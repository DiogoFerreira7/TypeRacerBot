from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Handler:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://play.typeracer.com")
        self.text = ""
        self.wpm = 500
        self.number_of_races = 0

    def race(self):
        # Wait for correct timings for the website to load up so that all of the accessed elements are loaded
        sleep(3)
        self.enter_race()
        sleep(4)
        self.parse_text()
        sleep(0.5)
        self.type_text()
        self.number_of_races += 1

    def enter_race(self):
        if self.number_of_races == 0:
            race_button = self.driver.find_element_by_link_text("Practice Yourself")
        else:
            race_button = self.driver.find_element_by_link_text("New race")
        race_button.click()
    
    def parse_text(self):
        # Select all of the spans which are unselectable
        # Need to wait for it to be accessible
        text_elements = self.driver.find_elements_by_xpath("//span[@unselectable='on']")
        text_elements = [element.text for element in text_elements]

        if len(text_elements) == 3:
            text_elements[1] += " "
        else:
            text_elements[0] += " "

        self.text = "".join(text_elements)
        self.text = self.text.split(" ")

    def type_text(self):
        input_box = self.driver.find_element_by_xpath("//input[@autocorrect='off' and @autocapitalize='off']")
        
        for word in self.text[:-1]:
            sleep(60 / self.wpm)
            input_box.send_keys(word + " ")

        # Send the last word without a space because the element becomes not interactible
        print(self.text)
        if len(self.text) != 1:
            input_box.send_keys(self.text[-1])

    def quit(self):
        self.driver.quit()
