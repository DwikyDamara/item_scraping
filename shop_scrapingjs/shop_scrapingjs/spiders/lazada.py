import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class LazadaSpider(scrapy.Spider):
    name = "lazada"

    def start_requests(self):
        s = Service("D:/Selenium/chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(service=s, options=options)
        driver.get(
            "https://www.lazada.co.id/beli-makanan-minuman-hasil-segar/?spm=a2o4j.searchlist.cate_10.5.95203bbe9DgTFB")
        xpath = '//*[@data-qa-locator="product-item"] //a[text()]'
        link_elements = driver.find_elements(By.XPATH, xpath)
        for link_el in link_elements:
            href = link_el.get_attribute("href")
            yield scrapy.Request(href)
        driver.quit()

    def parse(self, response):
        # Lakukan parsing halaman di sini
        name = response.css("h1::text").get()
        price = response.css(".pdp-price_color_orange::text").get()
        yield {
            'name': name,
            'price': price
        }
