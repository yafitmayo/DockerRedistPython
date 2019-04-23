import time
import Driver

# initialize chrome driver
Driver.initialize()
time.sleep(2)

# open web site
url_website = "http://192.168.99.100:5000/"
Driver.chrome_driver.get(url_website)

# get site text
text = Driver.chrome_driver.find_element_by_xpath("/html/body").get_attribute("textContent").strip(' \n\t')

# print site text
print(text)

# close chrome driver
Driver.close_driver()
