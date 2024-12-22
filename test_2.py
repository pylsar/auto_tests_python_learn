from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://takapulta.ru/')


time.sleep(5)
# получаем все дивы с одинак классом
card_blocks = driver.find_elements(By.CLASS_NAME, 'cat-item')
# print(card_blocks)

for card in card_blocks:
    card_link = card.find_element(By.TAG_NAME, 'a')
    # print(card_link)
    # получаем атрибут href
    print(card_link.get_attribute('href'))





driver.quit()