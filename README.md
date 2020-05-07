# Automate github

This is an automation script written in Python using the Selenium web automation tool. It is useful for creating empty repositories on the go to which you could push your existing projects. It helps ease a little with all the hassle that goes into logging into Github and then following the traditional procedure of creating an empty Repo. 

## Installation

```bash
pip install python
pip install selenium
```
    
- Install Chrome Webdriver: https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.106/


## Usage

Steps to be followed:
1)  OPEN & EDIT gp.json
    - Add your GitHub username 
    - Add your GitHub password
2) RUN autogit.py file
    - python autogit.py
3) Enter the name of repository, description, and select public/private when prompted. 

Having run the script you would be returned with a link to the newly created empty Repository to which you could then push your project.
