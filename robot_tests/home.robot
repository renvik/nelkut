*** Settings ***

Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Click Link Add Inproceeding
    Click Link  Add new reference
    Click Button  Add a reference to an inproceeding
    Add Inproceeding Page Should Be Open

Click Link Add Article
    Click Link  Add new reference
    Click Button  Add a reference to an article
    Add Article Page Should Be Open

Click Link Add Book
    Click Link  Add new reference
    Click Button  Add a reference to a book
    Add Book Page Should Be Open

Click Link Download Bibtex
    Click Link  Download BibTex file
    Home Page Should Be Open    

*** Keywords ***
Go To Main Page
    Go To  ${HOME_URL}
    Home Page Should Be Open