# Get stocks - web scrapping
# get data from the following websites
# https://smart-lab.ru/q/shares/
# excel / google sheet/document
# columns: company, international name, current price, % change
# Название, тикер, цена, изм %
# Checks !!!! try catch + reconnect
# Logging <- HOMEWORK 24.09.2021
# Timer - how much time it took < HOMEWORK 24.09.2021

class Stocks:
    def get_data_from_smart_lab(self):
        print('Getting data has started:')
        #try catch, reconnect
        #web scrapping = data(columns + values)
        data = 'data'
        return data

    def make_excel(self, data):
        #formatting
        print('Formatting excel')
        #save excel
        print('Saving excel')

    def make_google_sheet(self, data):
        #formatting
        print('Formatting google sheet')
        #save google sheet to your drive
        print('Saving google sheet')


def main():
    x1 = Stocks()
    data = x1.get_data_from_smart_lab()
    x1.make_excel(data)
    x1.make_google_sheet(data)




# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    main()