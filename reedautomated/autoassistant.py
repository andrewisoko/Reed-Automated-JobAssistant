from inputs import Inputs
from chromesettings import ChromeSettings
from firstwebpage import FirstWebPage
from credentials import Credentials
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time 
import random



class AutoAssistant():
    
    
    def __init__(self, chromesettings:ChromeSettings,inputs_instance:Inputs,firstwp:FirstWebPage):
        
        self.chromesettings = chromesettings
        self.inputs_instance = inputs_instance
        self.firstwp = firstwp


    def job_process(self):

        
        wait = WebDriverWait(self.chromesettings.driver, 10)
        
        last_week = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[3]/aside/div[2]/div/div[7]/div[2]/div/select/option[4]")))
        time.sleep(self.chromesettings.random_time)
        last_week.click()

        job_card_bodies = self.chromesettings.driver.find_elements(By.CSS_SELECTOR, "div.job-card_jobCard__body__86jgk.card-body")

        if len(job_card_bodies) == 0:
            return False
        
        else:
            for job_card_body in job_card_bodies:
                job_location = job_card_body.find_element(By.CSS_SELECTOR, "li[data-qa='job-card-location']")
                job_title = job_card_body.find_element(By.CSS_SELECTOR, "[data-qa='job-card-title']")
                
                job_location_text = job_location.text
                job_title_text = job_title.text
                
                print(f'Job found: THE CITY IS: {job_location_text}, THE NAME IS: {job_title_text}')
                    
                job_spec_name = ''
                location_spec_name = ''
                
                what_jobprocess = self.chromesettings.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="searchKeywordInput"]')
                where_jobprocess = self.chromesettings.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="searchLocationInput"]')

                what_value = what_jobprocess.get_attribute("value")
                where_value = where_jobprocess.get_attribute("value")

                print(f'what_value={what_value}, where_value={where_value}')
                
                if what_value == self.firstwp.jobtitle_firstwp:
                    job_spec_name = self.firstwp.joblocation_firstwp
                    
                if where_value == self.firstwp.joblocation_firstwp:
                     location_spec_name = self.firstwp.joblocation_firstwp
                
                print(f'Checking condition for: job_spec_name={job_spec_name} job_title_text={job_title_text}\nlocation_spec_name={location_spec_name} job_location_text={job_location_text}')
                    
                    