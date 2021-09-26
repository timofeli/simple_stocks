# Get stocks - web scrapping
# get data from the following websites
# https://smart-lab.ru/q/shares/
# excel / google sheet/document
# columns: company, international name, current price, % change
# Название, тикер, цена, изм %
# Checks !!!! try catch + reconnect
# Logging <- HOMEWORK 24.09.2021
# Timer - how much time it took < HOMEWORK 24.09.2021

import logging
logging.basicConfig(level=logging.DEBUG)

import time  # timer
tic = time.perf_counter()  # start timer
logging.info('program start')

#Trying to set up a parser and soup
from bs4 import BeautifulSoup
import requests
url = 'https://smart-lab.ru/q/shares/'
page = requests.get(url)
logging.info(page.status_code)
soup = BeautifulSoup(page.text, "html.parser")
print(soup)



class Stocks:
    def get_data_from_smart_lab(self):
        print('Getting data has started:')
        #try catch, reconnect
        #web scrapping = data(columns + values)
        data = 'data'
        logging.info('data from smart lab')
        logging.debug(data)
        return data

    def make_excel(self, data):
        logging.info('make excel')
        #formatting
        print('Formatting excel')
        #save excel
        print('Saving excel')

    def make_google_sheet(self, data):
        logging.info('make google sheet')
        #formatting
        print('Formatting google sheet')
        #save google sheet to your drive
        print('Saving google sheet')


def main():
    x1 = Stocks()
    data = x1.get_data_from_smart_lab()
    x1.make_excel(data)
    x1.make_google_sheet(data)

toc = time.perf_counter()     # stop timer





if __name__ == '__main__':
    print(f"The calculation took {toc - tic: 0.4f} seconds")
    main()
    logging.info('Program stop')
