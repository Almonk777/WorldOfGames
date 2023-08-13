from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
my_driver = webdriver.Chrome(service=Service('~/Downloads/chromedriver'))


#1
#a
my_driver.get('http://www.walla.co.il')

input()
#b
my_geko_driver = webdriver.Firefox(service=Service('~/Downloads/geckodriver'))
my_driver.get('https://www.ynet.co.il/home/0,7340,L-8,00.html')

input()
my_geko_driver.get("http://www.ynet.co.il")

#2
my_driver.get('http://www.walla.co.il')
get_title = my_driver.title
my_driver.refresh()

if get_title==my_driver.title:
    print("equal")

#3. Open a few browsers, locate any element, does the element has the same locator in the other browser?
# yes, the elements are located on the same position

#4
my_driver.get("https://translate.google.com/")
my_driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys('שיעור')

input()

#5
my_driver.get("https://www.youtube.com")

search_input = my_driver.find_element(By.NAME, "search_query")
search_input.send_keys("Frank Ocean - Pink + White")

search_input.send_keys(Keys.ENTER)

input()

#6
a = my_driver.find_element(By.ID, "gt-submit")
b = my_driver.find_element(By.NAME, "jfk-button")
c = my_driver.find_element(By.XPATH, "//input[@type='submit']")

print(a)
print(b)
print(c)

#7
my_driver.get("https://www.facebook.com/")
my_driver.find_element(By.ID, "email").send_keys("almonk@gmail.com")
my_driver.find_element(By.ID, "pass").send_keys("Almog1234567890")
my_driver.find_element(By.NAME, 'login').click()

input()

#8
my_driver.get('http://www.walla.co.il')
my_driver.delete_all_cookies()

remaining_cookies = my_driver.get_cookies()
print("Remaining Cookies")
for cookie in remaining_cookies:
    print(cookie)

my_driver.quit()

#9
my_driver.get('https://github.com/')
field = my_driver.find_element(By.NAME, "q")
field.send_keys("Selenium")
field.send_keys(Keys.ENTER)

input()

#10
#a
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

#b
geko_driver = webdriver.Firefox(service=Service('~/Downloads/geckodriver'))
profile = webdriver.FirefoxProfile()
profile.set_preference("extensions.enabled", False)

#c
#Explorer my_driver is not supported on mac

#11

chromedriver_path = '~/Downloads/chromedriver'
service = Service(chromedriver_path)
options = Options()
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(service=service, options=options)