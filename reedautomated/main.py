from inputs import Inputs
from chromesettings import ChromeSettings
from firstwebpage import FirstWebPage
from login import Login
from reedautoassistant import AutoAssistant



    
    
def main():
    
    inputs = Inputs()
    chrosettings = ChromeSettings()
    login = Login(chrosettings,inputs)
    firstwp = FirstWebPage(chrosettings,inputs)
    autoassistant = AutoAssistant(chrosettings,inputs,firstwp)
    
    inputs.input_collection()     
    login.loginpage_interaction()
    firstwp.webpage_interaction_firstwp()
    autoassistant.job_selection()

      

if __name__ == "__main__":
    main()