from inputs import Inputs
from chromesettings import ChromeSettings
from firstwebpage import FirstWebPage
from credentials import Credentials


def main():
    
    inputs = Inputs()
    chrosettings = ChromeSettings()
    firstwp = FirstWebPage(chrosettings,inputs)
    cred = Credentials(chrosettings,inputs)
    
    inputs.input_collection()
    firstwp.webpage_interaction_firstwp()
    cred.webpage_interaction_credentials()
    

if __name__ == "__main__":
    main()