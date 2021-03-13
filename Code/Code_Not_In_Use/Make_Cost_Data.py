import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import csv

COUNT_FILTER_VALUE = 40
PRICE_FILTER_VALUE = 40


def Clean_Data():
    list_data = CSV_To_List("/home/dylan/Documents/StockBot/outfiles/Graphs/Graph_total.csv")
    stock_list = CSV_To_List("/home/dylan/Documents/StockBot/outfiles/Stock_data.csv")
    new_stocks = [list_data[0]]
    for val in list_data:
        for stock in stock_list:
            if val[0] == stock[0]:
                print(stock[2])


    df = pd.DataFrame(new_stocks)
    #df.to_csv('/home/dylan/Documents/StockBot/outfiles/Stock_data.csv', index=False, header=False)
    #return new_list


def Get_Date_Time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m %H:%M")
    return dt_string


def CSV_To_List(Csv):
    with open(Csv, newline='') as f:
        reader = csv.reader(f)
        return list(reader)
def main():

    Clean_Data()



main()
