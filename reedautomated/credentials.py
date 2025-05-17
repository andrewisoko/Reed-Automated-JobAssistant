from inputs import Inputs
from chromesettings import ChromeSettings
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class Credentials():
    
     def __init__(self, chromesettings:ChromeSettings,inputs_instance:Inputs):
        
        self.chromesettings = chromesettings
        self.inputs_instance = inputs_instance
        
        
        
     def webpage_interaction_credentials(self):
        
         
        """Process the credentials into the webpage."""
         
        self.chromesettings.driver.refresh()
        time.sleep(5)
        sign_in = self.chromesettings.driver.find_element(
          By.XPATH, "/html/body/div[1]/nav/div/div[2]/div/ul/li[2]/a")
        sign_in.click() 


        time.sleep(10)
        email_bar = self.chromesettings.driver.find_element(By.ID, "signin_email")
        time.sleep(self.chromesettings.random_time)
        email_bar.send_keys(self.inputs_instance.email + Keys.ENTER)


        password_bar = self.chromesettings.driver.find_element(By.ID, "signin_password")
        time.sleep(self.chromesettings.random_time)
        password_bar.send_keys(self.inputs_instance.password)


        continue_button = self.chromesettings.driver.find_element(By.ID, "signin_button")
        time.sleep(self.chromesettings.random_time)
        continue_button.click()
        
        last_week = self.chromesettings.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[3]/aside/div[2]/div/div[7]/div[2]/div/select/option[4]")))
        time.sleep(self.chromesettings.random_time)
        last_week.click()