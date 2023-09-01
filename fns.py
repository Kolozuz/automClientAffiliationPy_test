from unittest import case
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def start():
    driver.implicitly_wait(5)
    driver.get("http://corevida.dllosura.com/PASJava/index.html")

def login(user_name = "", user_password = ""):
    # driver.implicitly_wait(30)
    form = driver.find_element(By.ID, "form-container") 
    user_name_input = driver.find_element(By.ID, "userName")
    user_password_input = driver.find_element(By.ID, "password")
    submit_btn = driver.find_element(By.ID, "submit")


    def checkCredentials(user_name = "", user_password = "") :

        while not user_name or not user_password : 
            user_name = input("Type your Username \n")
            user_password = input("Type your Password \n")
            user_name_input.clear()
            user_password_input.clear()
            user_name_input.send_keys(user_name)
            user_password_input.send_keys(user_password)
            submit_btn.click()

            homePage = driver.find_elements(By.ID, "homePage")
            
            errorMessage = driver.find_elements(By.CSS_SELECTOR, "span[data-bind='text:$parent.errorMessage()']")

            if len(homePage) == 0 : # While error message is present
                print("Wrong Username or Password! Try Again")
                user_name = ""
                user_password = ""

    # if user_name_input.is_displayed() and user_password_input.is_displayed() :
    checkCredentials(user_name, user_password)
    #     user_name_input.send_keys(user_name)
    #     user_password_input.send_keys(user_password)
    #     form.submit()
  
    return print("success!")

def nose():
     dropdown_create = driver.find_element(By.ID, "ojChoiceId_Menu_CreateNew")
     dropdown_create.click()
     dropdown_create = driver.find_element(By.ID, "oj-listbox-result-label-3")