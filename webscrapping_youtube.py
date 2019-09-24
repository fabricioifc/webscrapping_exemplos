import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox(executable_path='/home/fabricio/Desktop/webscrapping/geckodriver')
driver.get('')

