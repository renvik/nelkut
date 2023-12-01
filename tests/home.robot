*** Settings ***

Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Click Link Add
    Click Link  Add new reference
    Add Page Should Be Open


*** Keywords ***
Go To Main Page
    Go To  ${HOME_URL}
    Home Page Should Be Open