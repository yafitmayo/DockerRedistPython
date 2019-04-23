from selenium import webdriver

chrome_driver = None


# initialize chrome driver
def initialize():
    global chrome_driver

    # load chrome driver
    chrome_driver = webdriver.Chrome(executable_path="C:\\temp\\chromedriver.exe")
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    return chrome_driver


# close chrome driver
def close_driver():
    global chrome_driver
    chrome_driver.quit()

