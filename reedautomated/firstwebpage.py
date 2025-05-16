from chromesettings import ChromeSettings
from inputs import Inputs
import random
import time
from selenium.webdriver.common.by import By




class FirstWebPage():
    
    def __init__(self,chromesettings:ChromeSettings,inputs_instance:Inputs):
        
        self.chromesettings = chromesettings
        self.inputs_instance = inputs_instance
        self.jobtitle_firstwp = None
        self.joblocation_firstwp = None
        self.what = None
        self.where = None
        
        
    def webpage_interaction_firstwp(self):

       
        time.sleep(10)
        accept_button = self.chromesettings.driver.find_element(
        By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/button"
        )
        time.sleep(self.chromesettings.random_time)
        accept_button.click()
        
        

        self.jobtitle_firstwp = random.choice(self.inputs_instance.jobtitle_list)
        self.what = self.chromesettings.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[4]/div/section[1]/main/form/div/div/div/div[1]/span/input",
        )
        time.sleep(self.chromesettings.random_time)
        self.what.send_keys(self.jobtitle_firstwp)

        self.joblocation_firstwp = random.choice(self.inputs_instance.joblocation_list)
        self.where = self.chromesettings.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[4]/div/section[1]/main/form/div/div/div/div[2]/span/input",
        )
        time.sleep(self.chromesettings.random_time)
        self.where.send_keys(random.choice(self.joblocation_firstwp))
        

        search_jobs = self.chromesettings.driver.find_element(By.ID, "homepageSearchButton")
        time.sleep(self.chromesettings.random_time)
        search_jobs.click()