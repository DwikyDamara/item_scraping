from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s=Service("D:/Selenium/chromedriver.exe")
driver=webdriver.Chrome (service=s)
driver.get("https://www.lazada.co.id/beli-makanan-minuman-hasil-segar/?spm=a2o4j.searchlist.cate_10.5.95203bbe9DgTFB")

xpath='//*[@data-qa-locator="product-item"] //a[text()]'
link_elements = driver.find_elements(By.XPATH, xpath)
links=[]
for link_el in link_elements:
    href = link_el.get_attribute("href")
    print(href)
    links.append(href)
print(len(links))

driver.quit()