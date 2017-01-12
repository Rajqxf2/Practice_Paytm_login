
"""
Our automated test will do the following:
    #Open Paytm web application
    #On clicking on Wallet it asks to login to view the balance
    #Takes user id and password and clicks on Login
    #Displays the message that the OTP msg sent to **** number
    #Closes the Pop Up frame and quits the browser 
"""

#Import statements.
from selenium import webdriver
import time

#To open a browser and maximize.
driver = webdriver.Chrome()
driver.maximize_window()

#To open paytm website.
driver.get("http://paytm.com")
time.sleep(5) 

#To check whether when click on wallet it indicates to login to view balance.
wallet = driver.find_element_by_xpath("//div[contains(text(),'Paytm Wallet')]")
wallet.click()
print "Clicked on paytm wallet to view the balance"
#To check whether the Wallet tab is clicked or not.
dom_element = None
dom_element = driver.find_element_by_xpath("//a[text()='Log In / Sign Up']")
if (dom_element is not None):
    print "Automation successful clicked on Wallet"
else:
    print "Failed to click on Wallet"   
print "Login to view the balance"

#To click on login tab.
login_tab = driver.find_element_by_xpath("//a[text()='Log In / Sign Up']").click()
print "Clicked on Login tab"
#To check whether the Login tab is clicked or not.
dom_element = None
dom_element = driver.find_element_by_xpath("//md-dialog-content[@id='dialog_8']")
if (dom_element is not None):
    print "Automation successful clicked Login tab"
else:
    print "Failed to click on Login tab"   
time.sleep(5)

#To access the popup frame.
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
time.sleep(3)

#To take user id and password as input and click on log in button.
user_name = driver.find_element_by_xpath("//input[@name='username']")
user_name.send_keys("test@qxf2.com")
time.sleep(2)
print "Username is accepted"
passwd = driver.find_element_by_xpath("//input[@id='input_1']")
passwd.send_keys("TestQxf2")
time.sleep(2)
print "Password is accepted"
login = driver.find_element_by_xpath("//span[contains(text(),' Secure Login')]")
login.click()
print "Clicked on login button"
#To check whether the Login button is clicked or not.
dom_element = None
dom_element = driver.find_element_by_xpath("//input[@id='input_2']")
if (dom_element is not None):
    print "Automation successful clicked Login Button"
else:
    print "Failed to click on Login Button"   
time.sleep(5)

#To print the message that the OTP has sent to particular number.
Element = driver.find_element_by_xpath("//div[@class='success']")
print Element.text
time.sleep(5)

#To come out from the popup frame.
driver.switch_to_default_content()

#To close the pop up and quit the browser.
close_otp_window = driver.find_element_by_xpath("//button[i[contains(@class,'fa-times')]]")
close_otp_window.click()
print "Clicked on close element"
dom_element = None
dom_element = driver.find_element_by_xpath("//a[text()='Log In / Sign Up']")
#To check whether the Close element is clicked or not.
if (dom_element is not None):
    print "Automation successful closed the frame"
else:
    print "Failed to close the frame"   
time.sleep(4)
driver.quit()
