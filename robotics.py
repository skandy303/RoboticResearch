from datetime import datetime
from RPA.Browser.Selenium import Selenium
from SeleniumLibrary.errors import ElementNotFound
from RPA.Browser.Selenium import BrowserNotFoundError

br = Selenium()


class Robot:
    def __init__(self, name, url="https://wikipedia.org"):
        self.name = name

    def format_date(self, date):
        """Converts a date string to a datetime object"""
        return datetime.strptime(date, '%Y-%m-%d')

    def say_hello(self):
        """Prints a greeting message"""
        print("Hello, my name is " + self.name)

    def open_webpage(self, webpage):
        """Opens a webpage in the default browser"""
        try:
            br.open_available_browser(webpage)
        except BrowserNotFoundError:
            print("Unable to open browser, try installing Chrome/Firefox")
            return -1
        return None

    def close_webpage(self):
        """Closes all open browser windows"""
        br.close_all_browsers()
        return None

    def search_wikipedia(self, search_term):
        """Searches for a term on Wikipedia"""
        try:
            br.input_text("css:#searchInput", search_term)         
            br.click_button("css:#search-form > fieldset > button")
        except ElementNotFound:
            print("Could not find search field.")
            return False
        if search_term.lower().replace(" ", "_") not in br.get_location().split("/")[-1].lower():
            return False
        return True

    def go_home(self):
        """Navigates to the Wikipedia homepage"""
        br.go_to("https://wikipedia.org")

    def get_first_paragraph(self):
        """Returns the first paragraph of the Wikipedia article"""
        try:
            text_field = br.find_element("css:#mw-content-text > div.mw-parser-output > p:not([id]):not([class])")
            return text_field.text
        except ElementNotFound:
            return "First paragraph not found."

    def get_birth_date(self):
        """Returns the birthdate of the scientist"""
        try:
            birthdate = br.find_element("css:.bday")
            birthdate = birthdate.get_attribute("innerHTML")
            birthdate = self.format_date(birthdate)
            return birthdate
        except ElementNotFound:
            print("Birthdate not found.")
            return None

    def get_death_date(self):
        """Returns the deathdate of the scientist"""
        try:
            deathdate = br.find_element("//span[@class='bday']/ancestor::tr/following-sibling::tr[1]/td[1]/span")
            deathdate = deathdate.get_attribute("innerHTML")
            deathdate = self.format_date(deathdate.strip("()"))
        except ElementNotFound:
            deathdate = None
        return deathdate