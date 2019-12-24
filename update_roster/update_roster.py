import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("profile-directory=C:\\Users\\Delbert_F\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe', chrome_options=options)

# driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://fantasy.espn.com/basketball/team?leagueId=78370592&teamId=8&seasonId=2020')
time.sleep(10)

# popup = driver.find_element_by_xpath("//*[@id='disneyid-wrapper']")

# ifram = driver.find_element_by_xpath("//*[@id='disneyid-iframe']")
# print(type(ifram))
# driver.switch_to_frame(ifram)   



# driver.find_element_by_xpath("//*[@id='did-ui-view']/div/section/section/form/section/div[3]/button")


# time.sleep(10)

# username_field = driver.find_element_by_xpath("//*[@id='did-ui-view']/div/section/section/form/section/div[1]/div/label/span[2]/input")
# username_field.send_keys("some test")


# login_button = driver.find_element_by_xpath("//*[@id='espn-analytics']/div/div[5]/div[2]/div[1]/div/div/button")
# login_button.click()
# time.sleep(10)

driver.quit()
