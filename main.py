from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement

PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)


def setUpDriver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver.get("https://finishline.com/")
    driver.implicitly_wait(10000)

    noThanks = driver.find_element_by_id('bx-element-1455392-ErsXur3')
    noThanks.click()

    return driver


def addToCart_preRelease(driver):


    cartElement = webdriver.Chrome.find_element_by_xpath(driver, '//*[@id="bx-element-1455392-ErsXur3"]/button')
    print(cartElement)


if __name__ == '__main__':
    setUpDriver()
    addToCart_preRelease(driver)
    webdriver.Chrome.implicitly_wait(4000)
