import unittest
from robotics import Robot
from datetime import datetime

class TestRobot(unittest.TestCase):

    def setUp(self):
        """Set up a new object to be tested"""
        self.robot = Robot("TestBot")

    def test_formatDatePass(self):
        """Test formatDate method"""
        result = self.robot.formatDate('2000-01-01')
        expected_result = datetime(2000, 1, 1)
        self.assertEqual(result, expected_result)
    
    def test_formatDateFail(self):
        """Test formatDate method"""
        result = self.robot.formatDate('2000-01-01')
        expected_result = datetime(2000, 1, 2)
        self.assertNotEqual(result, expected_result)
    
    def test_search_wikipediaPass(self):
        """Test search_wikipedia method"""
        self.robot.open_webpage('https://wikipedia.org')
        result = self.robot.search_wikipedia('Albert Einstein')
        self.robot.close_webpage()
        self.assertTrue(result)
    def test_search_wikipediaFail(self):
        """Test search_wikipedia method"""
        self.robot.open_webpage('https://wikipedia.org')
        result = self.robot.search_wikipedia('this is an invalid search term')
        self.robot.close_webpage()
        self.assertFalse(result)
    
    def test_first_paragraphPass(self):
        """Test getFirstParagraph method"""
        self.robot.open_webpage('https://wikipedia.org')
        self.robot.search_wikipedia('Albert Einstein')
        result = self.robot.getFirstParagraph()
        self.robot.close_webpage()
        self.assertTrue(result, 'Albert Einstein was a German-born theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics (alongside quantum mechanics). His work is also known for its influence on the philosophy of science.')

    def test_first_paragraphFail(self):
        """Test getFirstParagraph method"""
        self.robot.open_webpage('https://wikipedia.org')
        self.robot.search_wikipedia('Some random search term')
        result = self.robot.getFirstParagraph()
        self.robot.close_webpage()
        self.assertNotEqual(result, 'This is not the correct first paragraph.')
    
    def test_birthdatePass(self):
        """Test getBirthDate method"""
        self.robot.open_webpage('https://wikipedia.org')
        self.robot.search_wikipedia('Albert Einstein')
        result = self.robot.getBirthDate()
        self.robot.close_webpage()
        self.assertTrue(result.date(), datetime(1879, 3, 14))
    
    def test_BirthdateFail(self):
        """Test getBirthDate method"""
        self.robot.open_webpage('https://wikipedia.org')
        self.robot.search_wikipedia('Albert Einstein')
        result = self.robot.getBirthDate()
        self.robot.close_webpage()
        self.assertNotEqual(result, datetime(1879, 3, 10))
    
    def test_deathdatePass(self):
        """Test getDeathDate method"""
        self.robot.open_webpage('https://wikipedia.org')
        self.robot.search_wikipedia('Albert Einstein')
        result = self.robot.getDeathDate()
        self.robot.close_webpage()
        self.assertTrue(result, datetime(1955, 4, 18))
    
    def test_deathdateFail(self):
        """Test getDeathDate method"""
        self.robot.open_webpage('https://wikipedia.org')
        self.robot.search_wikipedia('Albert Einstein')
        result = self.robot.getDeathDate()
        self.robot.close_webpage()
        self.assertNotEqual(result, datetime(1955, 4, 19))
    

if __name__ == '__main__':
    unittest.main()