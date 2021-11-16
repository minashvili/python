from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("A")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#driver.close()






























#import requests
#from bs4 import BeautifulSoup
#
#ret = requests.get('https://2ip.ru/')
##print(ret.text)
#soup = BeautifulSoup(ret.text, 'html.parser')
#el = soup.find(id='d_clip_button')
#ip = el.text
#print(ip)
#




#import requests
# ret = requests.get('https://2ip.ru/')
# #print(ret.text)

# id_pos = ret.text.find('id="d_clip_button"')
# ip_start_pos = ret.text.find('<span>', id_pos) + 6
# ip_end_pos = ret.text.find('</', ip_start_pos)
# ip = ret.text[ip_start_pos:ip_end_pos]

# print(ip)



