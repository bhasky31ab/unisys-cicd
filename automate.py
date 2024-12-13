from selenium  import webdriver
import time
# we are only import webdriver from entire selenium
 
#loading particular browser of a driver
 
#initialising web driver
chrome_driver = webdriver.Chrome()
 
#opening a web url
 
chrome_driver.get("https://portal.adhocnet.org/")
time.sleep(3)
#Closing my driver / stopping
chrome_driver.quit()