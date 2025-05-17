from inputs import Inputs
from chromesettings import ChromeSettings
from firstwebpage import FirstWebPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 




class Reed_AutoAssistant():
    
    
    def __init__(self, chromesettings:ChromeSettings,inputs_instance:Inputs,firstwp:FirstWebPage):
        
        self.chromesettings = chromesettings
        self.inputs_instance = inputs_instance
        self.firstwp = firstwp
        self.job_spec_name = None
        self.location_spec_name = None
        self.job_location_text = None
        self.job_title_text = None
        self.job_card_bodies = None
        self.job_card_body = None
       
       



    def job_selection(self):

    

        self.job_card_bodies = self.chromesettings.driver.find_elements(By.CSS_SELECTOR, "div.job-card_jobCard__body__86jgk.card-body")

        if len(self.job_card_bodies) == 0:
            return False
        
        else:
            for self.job_card_body in self.job_card_bodies:
                job_location = self.job_card_body.find_element(By.CSS_SELECTOR, "li[data-qa='job-card-location']")
                job_title = self.job_card_body.find_element(By.CSS_SELECTOR, "[data-qa='job-card-title']")
                
                self.job_location_text = job_location.text
                self.job_title_text = job_title.text
                
                print(f'Job found: THE CITY IS: {self.job_location_text}, THE NAME IS: {self.job_title_text}')
                    
                
                what_jobprocess = self.chromesettings.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="searchKeywordInput"]')
                where_jobprocess = self.chromesettings.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="searchLocationInput"]')

                what_value = what_jobprocess.get_attribute("value")
                where_value = where_jobprocess.get_attribute("value")

                print(f'what_value={what_value}, where_value={where_value}')
                
                if what_value == self.firstwp.jobtitle_firstwp:
                    self.job_spec_name = self.firstwp.joblocation_firstwp
                if where_value == self.firstwp.joblocation_firstwp:
                     self.location_spec_name = self.firstwp.joblocation_firstwp
                
                print(f'Checking condition for: job_spec_name={self.job_spec_name} job_title_text={self.job_title_text}\nlocation_spec_name={self.location_spec_name} job_location_text={self.job_location_text}')
            
            
                if self.job_spec_name in self.job_title_text and self.job_location_text == self.location_spec_name:
                    print(f'JOB NAME SELECTED: {self.job_spec_name} \nLOCATION NAME SELECTED: {self.location_spec_name}')
                    

                    try:
                        index_job_card = self.job_card_bodies.index(self.job_card_body)
                        print(f'this is the current amount of card bodies: {len(self.job_card_bodies)}')
                        
                        self.chromesettings.driver.execute_script("arguments[0].scrollIntoView(true);", self.job_card_body)

                        try:
                            main_job_card = self.job_card_body.find_element(By.CSS_SELECTOR, 'button[data-qa="applyJobBtn"]')
                            print(f'{main_job_card.text} existent')
                        
                        except Exception as e:
                            print(f'Exception finding main job card: {e}')
                            job_suggestion = self.job_card_body.find_element(By.CSS_SELECTOR, 'button[data-qa="shortlistBtn"]')
                            time.sleep(self.chromesettings.random_time)
                            job_suggestion.click()
                            print('your job suggestion found !!!')

                        main_jobcard_active = self.job_card_body.find_element(By.CSS_SELECTOR, 'button.job-card_applyBtn__2N2jy.btn.btn-secondary:not(.disabled)')
                        time.sleep(self.chromesettings.random_time)
                        self.chromesettings.driver.execute_script("arguments[0].click();", main_jobcard_active)
                        
                        job_description = self.chromesettings.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.apply-job-modal_buttonGroup__button__6ObMn.btn.btn-primary')))
                        time.sleep(self.chromesettings.random_time)
                        job_description.click()
                        
                        try:
                            ok_button = self.chromesettings.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.application-confirmation-modal_continueButton__i73Dl.btn.btn-primary')))
                            time.sleep(self.chromesettings.random_time)
                            ok_button.click()

                            print(f'this is the current amount of card bodies: {len(self.job_card_bodies)}')
                        
                        except Exception as e:
                            print(f'OK button exception: {e}')
                            x_button = self.chromesettings.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div > div.modal.overflow-auto.fade.show.d-block > div > div > header > button')))
                            x_button.click()

                            self.job_card_bodies.pop(index_job_card)
                            print(f'index of the job card {self.job_card_bodies.index(self.job_card_body)} successfully removed')

                        return True
                    except Exception as e:
                            print(f'Main card jobs NOT FOUND: {e}')
            
            # Else condition
            try:
                next_page_button = self.chromesettings.driver.find_element(By.CSS_SELECTOR, "a.page-link.next[aria-label='Next page']")
                self.chromesettings.driver.execute_script("arguments[0].click();", next_page_button)
                print(f'this is the current amount of card bodies: {len(self.job_card_bodies)}')
                return self.job_selection()
            
            except Exception as e:
                print(f'Next page button exception: {e}')
                return False

        
        