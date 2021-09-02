from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://yandex.ru/')
driver.fullscreen_window()
searchLine = driver.find_element_by_xpath('//*[@id="text"]')
searchLine.send_keys('github')
searchButton = driver.find_element_by_xpath('//*[@class="button mini-suggest__button button_theme_search button_size_search i-bem button_js_inited"]')
searchButton.click()  
#driver.close()