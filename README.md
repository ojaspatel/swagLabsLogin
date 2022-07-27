# Swag Labs Login Test  
The materials in this repository support QA testing for merch website
functionality. It's structured for BDD using behave, a semi-formal python
implementation of Cucumber, and selenium page object modeling.
## Test Criteria  
This section outlines requirements.
### User Story  
As a Swag Labs customer who is not locked out, I need to be able to log in so  
that I can purchase Sauce Labs merch.  
### Acceptance Criteria  
#### Scenario 1: Successful Login  
Given I am on the Sauce Demo Login Page,  
When I fill the account information for account StandardUser into the Username  
field and the Password field,  
And I click the Login Button,  
Then I am redirected to the Sauce Demo Main Page,  
And I verify the App Logo exists,  
#### Scenario 2: Failed Login  
Given I am on the Sauce Demo Login Page,  
When I fill the account information for account LockedOutUser into the  
Username field and the Password field,  
And I click the Login Button,  
Then I verify the Error Message contains the text "Sorry, this user has been  
banned."
### Test URL  
https://www.saucedemo.com/  
### Logins  
#### User 1: Standard User  
Username: standard_user  
Password: secret_sauce  
#### User 2: Locked Out User  
Username: locked_out_user  
Password: secret_sauce  
## System Requirements  
This test requires Google Chrome to be installed on the testing machine.  
In addition, the python packages webdriver-manager, selenium, and behave must  
be installed on the testing machine. All three packages can be installed  
using pip. The syntax for installation is `pip install <package name>`.  
## Execution instructions  
To run the test, clone this repository to the testing machine. Navigate to the  
root folder `swagLabs` in terminal or Command Prompt and run `behave`.
