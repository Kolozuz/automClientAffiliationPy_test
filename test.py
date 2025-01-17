from selenium.webdriver.common.by import By
from fns import webPage, loginPage, nose

myPage = webPage("http://corevida.dllosura.com/PASJava/index.html")

URLSTR = myPage.url

myloginPage = loginPage(myPage)
myloginPage.urltext = URLSTR
print(URLSTR)

#start() #   Loads web page (Oipa)

myloginPage.geturl()

myloginPage.login() #   Asks for login credentials (username & password) in console.    
                  #   Alternatively you can send them as parameters like this ->  
                  #   login("your_username", "your_password") so that you don't 
                  #   have to type them every time you run the script

nose()  #   Opens the form, fills the fields and creates a natural client
