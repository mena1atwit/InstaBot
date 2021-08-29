from selenium import webdriver
driver = webdriver.Chrome("")

driver.get("https://www.youtube.com/channel/UC5nsAaNa20Qu8g7HtX3ElTA")
subcount = driver.find_element_by_id("subscriber-count")
print(subcount)