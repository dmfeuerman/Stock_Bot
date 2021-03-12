import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import csv

COUNT_FILTER_VALUE = 40
PRICE_FILTER_VALUE = 40

def Create_New_CSV(infile1, infile2):

    df1 = pd.read_csv(infile1, error_bad_lines=False, low_memory=False)
    df2 = pd.read_csv(infile2, error_bad_lines=False, low_memory=False)
    merged = df1.merge(df2, on="Date", how="left").fillna("")
    merged.to_csv(infile2, index=False)

def Sort_Final_Data():
    list_data = Clean_Data()
    df = pd.DataFrame(list_data)
    df.to_csv('/home/dylan/Documents/StockBot/outfiles/Graphs/Graph_total.csv', index=False, header=False)


def Clean_Data():
    list_data = CSV_To_List("/home/dylan/Documents/StockBot/outfiles/Graphs/Graph_total.csv")
    stock_list = CSV_To_List("/home/dylan/Documents/StockBot/outfiles/Stock_data.csv")
    new_list = []
    new_stocks = []
    new_list.append(list_data[0])
    for val in list_data:
        for stock in stock_list:
            if val[0] == stock[0]:
                if (float(val[1]) >= COUNT_FILTER_VALUE) and (float(stock[2]) <= PRICE_FILTER_VALUE):
                    new_list.append(val)
                    new_stocks.append(stock)

    df = pd.DataFrame(new_stocks)
    df.to_csv('/home/dylan/Documents/StockBot/outfiles/Stock_data.csv', index=False, header=False)
    return new_list


def Get_Date_Time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m %H:%M")
    return dt_string

def Create_Final_CSV():

    word_list = CSV_To_List("/home/dylan/Documents/StockBot/outfiles/Combiner.csv")
    word_list.pop(0)

    new_list = []
    search_words = Create_list("/home/dylan/Documents/StockBot/Data_collection/Search_words.txt")
    for item in word_list:
        substring_in_list = any(item[0] in string for string in search_words)
        if substring_in_list:
            try:
                if float(item[1]) >= 20:
                    new_list.append(item)
            except ValueError:
                continue
    Create_Graph_Data(new_list)



def Create_Graph_Data(word_list):
    fs = open("/home/dylan/Documents/StockBot/outfiles/Graphs/Graph_Data.csv", "r+")
    fs.write("Date," + Get_Date_Time() + "\n")

    for item in word_list:
        fs.write(item[0] + ",")
        fs.write(item[1])
        fs.write("\n")




def Create_list(file):
    with open(file, "r") as f:
        search = f.read().splitlines()
    f.close()
    return search

def Graph_Data():
    df = pd.read_csv('/home/dylan/Documents/StockBot/outfiles/Graphs/Graph_total.csv', index_col='Date')
    df = df.T
    df.plot(legend=True)  # plot usa column
    plt.savefig("/home/dylan/Documents/StockBot/outfiles/Sorted_data/Graph.pdf")

def CSV_To_List(Csv):
    with open(Csv, newline='') as f:
        reader = csv.reader(f)
        return list(reader)
def main():

    Create_Final_CSV()
    Create_New_CSV("/home/dylan/Documents/StockBot/outfiles/Graphs/Graph_Data.csv", "/home/dylan/Documents/StockBot/outfiles/Graphs/Graph_total.csv")
    Sort_Final_Data()
    Graph_Data()



main()
