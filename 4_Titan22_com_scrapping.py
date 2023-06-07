from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")               #enter the link you wnat to scrape
  return driver

def main():
  driver = get_drvier()
  driver.find_element(by="id", value="CustomerEmail").send_keys("YOUR GMAIL")                           #enter your gmail
  time.sleep(2)
  driver.find_element(by="id", value="CustomerPassword").send_keys("your PASSWORD" + Keys.RETURN)         #enter your password
  time.sleep(2)
  driver.find_element(by="xpath", value='/html/body/header/div[1]/div[1]/div/div[2]/nav[1]/ul/li[3]/a').click()
  print(driver.current_url)

print(main())