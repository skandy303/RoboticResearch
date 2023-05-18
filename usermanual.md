# Robotic Researcher User Manual
This guide will walk you through the steps to setup and run the Robotic Researcher Python application, which automates the process of fetching information about notable scientists from Wikipedia.

## Getting Started
To get started with the Robotic Researcher, make sure you have a Python environment ready with the required packages installed.

Required Python version: Python 3.6+

Required Python Libraries:

 - datetime
 - RPA.Browser.Selenium
 - SeleniumLibrary.errors
## Project Structure
The project consists of two Python files: robotics.py and main.py.

robotics.py: This file contains the Robot class definition with various methods to fetch and process the data from Wikipedia.

main.py: This is the main execution file that uses the Robot class from robotics.py to fetch and display information about a list of predefined scientists.

## Running the Application
To run the Robotic Researcher application, follow these steps:

Open a command line terminal.
Navigate to the directory containing the main.py and robotics.py files.
Run the command python main.py.
This will start the automated process, and the application will begin fetching information about the predefined scientists.

Modifying Scientists List
If you want to modify the list of scientists for whom you want to fetch information, modify the SCIENTISTS list in the main.py file.

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin", "Alan Guth"]
Add or remove the scientist names as per your requirement.

## Testing
The application comes with a suite of unit tests to ensure its proper functioning. To run the tests, execute the command python test_robotics.py.

## Troubleshooting
If you encounter errors related to missing Python libraries, ensure you have installed all the required libraries and their versions are compatible with the Python version you are using.
If the fetched data appears incorrect or incomplete, check the Wikipedia pages for the relevant scientists to ensure that the required information is available and properly formatted.



