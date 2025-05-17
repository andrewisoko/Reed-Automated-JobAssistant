from inputs import Inputs
from chromesettings import ChromeSettings
from firstwebpage import FirstWebPage
from login import Login
from reed_autoassistant import Reed_AutoAssistant
import pickle


def main():
    
    
    inputs = Inputs()
    chrosettings = ChromeSettings()
    login = Login(chrosettings,inputs)
    firstwp = FirstWebPage(chrosettings,inputs)
    autoassistant = Reed_AutoAssistant(chrosettings,inputs,firstwp)
    
    
    with open("reedautomated/cookies/save-cookies.pkl", 'r') as file_obj:
        first_char = file_obj.read(1)
        
        if not first_char:
            inputs.input_collection()
            login.login_no_cookie()
            
            chrosettings.main_url
           
            with open("reedautomated/cookies/save-cookies.pkl", "rb") as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    chrosettings.driver.add_cookie(cookie)
                    
                chrosettings.main_url
                firstwp.webpage_interaction_firstwp()
            
                while chrosettings.loop_duration_time:
                    
                    autoassistant.job_selection()
                    if not autoassistant.job_selection():
                        print("No more jobs found or an error occurred")
                    break
                
        else:
            
            chrosettings.main_url
           
            with open("reedautomated/cookies/save-cookies.pkl", "rb") as file:
                cookies = pickle.load(file)
                
                for cookie in cookies:
                    chrosettings.driver.add_cookie(cookie)
                    
                chrosettings.main_url
                firstwp.webpage_interaction_firstwp()
            
                while chrosettings.loop_duration_time:
                    
                    autoassistant.job_selection()
                    if not autoassistant.job_selection():
                        print("No more jobs found or an error occurred")
                        break
            


if __name__ == "__main__":
    main()