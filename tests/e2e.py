from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
my_driver = webdriver.Chrome(service=Service('/Users/user/Downloads/chromedriver'))
def test_scores_service(applicationURL):
    my_driver.get(applicationURL)
    response = my_driver.find_element(By.ID,"nav_exercises")
    score = response.text
    return 1 <= int(score) <= 1000

def main_function():
    status = test_scores_service("https://www.w3schools.com/whatis/whatis_fullstack.asp")
    if status == True:
        return 0
    else:
        return -1

main_function()