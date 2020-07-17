import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class FirstTestCase(unittest.TestCase):
    def test_one(self): 
                
        driver = webdriver.Remote(command_executor="http://selenium:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
        driver.get("http://www.python.org")
        assert "Python" in driver.title        
