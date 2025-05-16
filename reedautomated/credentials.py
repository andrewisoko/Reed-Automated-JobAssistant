from inputs import Inputs
from chromesettings import ChromeSettings
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class credentials():
    
     def __init__(self, chromesettings:ChromeSettings):
        
        self.chromesettings = chromesettings
        
        
        
     def webpage_interaction_credentials(self):
         
         
        inputs_instance_credentials = Inputs()
        
         
        self.chromesettings.driver.refresh()
        time.sleep(5)
        sign_in = self.chromesettings.driver.find_element(
          By.XPATH, "/html/body/div[1]/nav/div/div[2]/div/ul/li[2]/a")
        sign_in.click() 


        time.sleep(10)
        email_bar = self.chromesettings.driver.find_element(By.ID, "signin_email")
        time.sleep(self.chromesettings.random_time)
        email_bar.send_keys(inputs_instance_credentials.email + Keys.ENTER)


        password_bar = self.chromesettings.driver.find_element(By.ID, "signin_password")
        time.sleep(self.chromesettings.random_time)
        password_bar.send_keys(inputs_instance_credentials.password)


        continue_button = self.chromesettings.driver.find_element(By.ID, "signin_button")
        time.sleep(self.chromesettings.random_time)
        continue_button.click()