from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time
  
print('Welcome.Enter the gmail adrress and password')
gmail = input("email: ") 
password = input("password: ") 

try:
    # Added maximized browser window option
    myOptions = EdgeOptions()
    myOptions.add_argument('start-maximized')
    # Making browser instance and using get method to fetch gmail login page
    driver = Edge(service=Service(EdgeChromiumDriverManager().install()), options=myOptions)
    driver.get('https://accounts.google.com/AccountChooser/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser')
    #method used to wait for finding elements or execute commands.It's called once
    driver.implicitly_wait(15) 

    # Finding login box element with Xpath and sending email data
    loginElement = driver.find_element(By.XPATH, '//*[@id ="identifierId"]')
    loginElement.send_keys(gmail)

    # Finding NEXT button to procede to next page
    nextButton = driver.find_elements(By.XPATH, '//*[@id ="identifierNext"]')
    nextButton[0].click()

  
    # Finding password box and passing password data to it
    passwordElement = driver.find_element(By.XPATH, 
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    passwordElement.send_keys(password)
   
    # Finding NEXT button to procede to next page
    nextButton = driver.find_elements(By.XPATH, '//*[@id ="passwordNext"]')
    nextButton[0].click()
    
    time.sleep(5)
    # closing browser instance
    driver.quit() 
    print('Login Successful...!!')
except:
    print('Login Failed')
