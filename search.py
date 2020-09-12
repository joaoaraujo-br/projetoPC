from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from time import sleep

def find_hardware(name):
    search_bar = driver.find_element_by_class_name('sprocura')
    search_bar.send_keys(name)
    search_bar.send_keys(Keys.RETURN)
    sleep(3)
    price = driver.find_element_by_class_name('sc-fznWqX')
    return name + ' - ' + price.text

def price_to_float(price):
    #removing 'R$'
    price = price.split(' ')[-1]
    
    #removing ',' and '.'
    price = ''.join(price.replace('.', ',').split(','))

    #transforming string into float
    price = int(price) / 100

    return price

driver = webdriver.Chrome('/home/joaoas/chromedriver_linux64/chromedriver')

driver.get('https://www.kabum.com.br/')

sleep(3)

hardware = []

hardware.append(find_hardware('ryzen 5 3400g'))
hardware.append(find_hardware('hyperx fury 8gb DDR4'))
hardware.append(find_hardware('asus prime 450m am4'))
hardware.append(find_hardware('ssd 240gb wd'))
hardware.append(find_hardware('evga 400w'))

prices_string = [h.split('-')[-1] for h in hardware]
prices = [price_to_float(ps) for ps in prices_string]
prices.append(sum(prices))

with open('prices.csv', 'a') as file:
    file.write('\n' + datetime.today().strftime('%d/%m/%Y') + ',' + ','.join(map(str, prices)))

driver.quit()