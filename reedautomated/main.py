from inputs import Inputs
from chromesettings import ChromeSettings
from firstwebpage import FirstWebPage
from login import Login
from reedautoassistant import AutoAssistant
import schedule
import time



class MainInteraction():
    
    def __init__(self):
        self.input_instance = Inputs()
      
    def job_tasks(self):
        
        chrosettings = ChromeSettings()
        login = Login(chrosettings,self.input_instance)
        firstwp = FirstWebPage(chrosettings,self.input_instance)
        autoassistant = AutoAssistant(chrosettings,self.input_instance,firstwp)
    
        login.loginpage_interaction()
        firstwp.webpage_interaction_firstwp()
        autoassistant.job_selection()
        
    
        
maininteraction_instance = MainInteraction()
    

def main():
    
    # print(maininteraction_instance.job_tasks())
    
    schedule.every(10).minutes.do(maininteraction_instance.job_tasks)
    while True:
        schedule.run_pending()
        time.sleep(1)
            


if __name__ == "__main__":
    maininteraction_instance.input_instance.input_collection()
    main()
 