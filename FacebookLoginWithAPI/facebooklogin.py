import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By





class FacebookLogin:

        
    def __init__(self,username,password):
        self.username = ""
        self.password = ""


if __name__ == '__main__':
        username = str(sys.argv[1])
        password = str(sys.argv[2])


driver = webdriver.Chrome()


driver.get("http://facebook.com/login")
driver.implicitly_wait(2)
email = driver.find_element(By.NAME, "email")

email.send_keys(username)

passw =  driver.find_element(By.NAME, "pass")
passw.send_keys(password)


loginbtn = driver.find_element(By.ID, "loginbutton")
loginbtn.click()


