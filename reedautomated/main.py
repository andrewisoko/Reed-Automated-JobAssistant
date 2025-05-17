from inputs import Inputs
from chromesettings import ChromeSettings
from firstwebpage import FirstWebPage
from credentials import Credentials
from reed_autoassistant import Reed_AutoAssistant


def main():
    
    inputs = Inputs()
    chrosettings = ChromeSettings()
    firstwp = FirstWebPage(chrosettings,inputs)
    cred = Credentials(chrosettings,inputs)
    autoassistant = Reed_AutoAssistant(chrosettings,inputs,firstwp)
    
    inputs.input_collection()
    firstwp.webpage_interaction_firstwp()
    cred.webpage_interaction_credentials()
    
    while chrosettings.loop_duration_time:
        
        autoassistant.job_selection()
        if not autoassistant.job_selection():
            print("No more jobs found or an error occurred")
            # self.driver.close()
            break


if __name__ == "__main__":
    main()