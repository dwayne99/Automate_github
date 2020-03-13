from selenium import webdriver
import json 

with open("gp.json", "r") as f:
    data = json.load(f)

username = data['un']
password = data['p']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=chrome_options)
#go to signin link
driver.get('https://github.com/login')
#username
ele = driver.find_element_by_id('login_field')
ele.send_keys(username)
#pass
ele = driver.find_element_by_id('password')
ele.send_keys(password)
#login button
ele = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
ele.click()
#Select new_repo create button
ele = driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a')
ele.click()
#Repo name
repo_name = input('Enter Repository name: ')
ele = driver.find_element_by_xpath('//*[@id="repository_name"]')
ele.send_keys(repo_name)
#Repo description
desc = input('Enter Repository description: ')
ele = driver.find_element_by_id('repository_description')
ele.send_keys(desc)
#private or public
if(int(input('Enter 1 for private, 0 for public repo: '))):
    ele = driver.find_element_by_id('repository_visibility_private') 
    ele.click()
#create_button
ele = driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
ele.click()
#returning the git link
ele = driver.find_element_by_xpath('//*[@id="empty-setup-clone-url"]')
print(ele.get_attribute("value"))
#Logout 
# ele = driver.find_element_by_xpath('/html/body/div[1]/header/div[5]/details/details-menu/form/button') 
# ele.click()
driver.quit()
