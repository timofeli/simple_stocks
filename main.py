# Get stocks - web scrapping
# get data from the following websites
# https://smart-lab.ru/q/shares/
# excel / google sheet/document
# columns: company, international name, current price, % change
# Название, тикер, цена, изм %
# Checks !!!! try catch + reconnect
# Logging <- HOMEWORK 24.09.2021
# Timer - how much time it took < HOMEWORK 24.09.2021

import logger
logger.basicConfig(level=logger.DEBUG)

import time     # timer
tic = time.perf_counter()  # start timer

from fibo import fibo   # set of tasks, To check the timer
logger.info('program start')
class Stocks:
    def get_data_from_smart_lab(self):
        print('Getting data has started:')
        #try catch, reconnect
        #web scrapping = data(columns + values)
        data = 'data'
        logger.info('data from smart lab')
        logger.debug(data)
        result = fibo(1000)   # to check the timer

        return data

    def make_excel(self, data):
        logger.info('make excel')
        #formatting
        print('Formatting excel')
        #save excel
        print('Saving excel')

    def make_google_sheet(self, data):
        logger.info('make google sheet')
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



# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print(f"Вычисление заняло {toc - tic:0.4f} секунд")
    main()
    logger.info('Program stop')