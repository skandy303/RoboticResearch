from robotics import Robot
from time import sleep
from datetime import datetime


SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin", "Alan Guth"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    """Introduces the robot to the user"""
    robot.say_hello()

def display_data(info):
    """displays the data in a readable format"""
    for scientist in info:
        name, birthdate, deathdate, first_paragraph = scientist
        print(f"\nScientist: {name}")
        if birthdate:
            print(f"Birthdate: {birthdate.date()}")
        else:
            print("Birthdate not available.")
        if deathdate:
            print(f"Died: {deathdate.date()}")
            if birthdate:
                print(f"Age at death: {(deathdate - birthdate).days //365}")
        else:
            print("Age: This scientist might still be alive, or the death information is not available.")
        print(f"First Paragraph from Wikipedia: {first_paragraph}\n")

def main():
    """
    Main function, parses the Wikipedia pages of the scientists in SCIENTISTS
    and prints their birthdate, deathdate, and the first paragraph of their Wikipedia page.
    """
    introduce_yourself()
    robot.open_webpage('https://wikipedia.org')
    info = []
    for scientist in SCIENTISTS:
        print(f"Searching for {scientist}...")
        if not robot.search_wikipedia(scientist):
            print(f"\nCould not find {scientist} on Wikipedia.\n")
            robot.go_home()
            continue  # Continue to next scientist if search was unsuccessful
        # robot.search_wikipedia(scientist)
        first_paragraph = robot.get_first_paragraph()
        birthdate = robot.get_birth_date()
        deathdate = robot.get_death_date()
        info.append((scientist, birthdate, deathdate, first_paragraph))
        robot.go_home()
    display_data(info)

if __name__ == "__main__":
    main()
