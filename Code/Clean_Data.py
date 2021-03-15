import time

import pandas as pd
import csv


def Clean_Data(file, bool_val, count, price):
    list_data = CSV_To_List(file)
    stock_list = CSV_To_List("/home/dylan/Documents/StockBot/outfiles/Stock_data.csv")
    hold_val = []
    new_list = []

    hold_val = Extract_Title(bool_val, hold_val, list_data)

    for val in list_data:
        if Check_Search_Words(val[0]) and str(val[0]).strip() != "":
            for stock in stock_list:
                if str(stock[0]).strip() == str(val[0]).strip():
                    if (float(stock[2]) <= price) and (float(val[1]) >= count):
                        new_list.append(val)
                    else:
                        continue
    new_list = Add_Back_Title(bool_val, hold_val, new_list)
    df = pd.DataFrame(new_list)
    df.to_csv(file, index=False, header=False)



def Clean_stock_data(price, count):
    stock_list = CSV_To_List("/home/dylan/Documents/StockBot/outfiles/Stock_data.csv")
    out_stocks = []
    for stock in stock_list:
        if (float(stock[1]) >= count) and (float(stock[2]) <= price):
            out_stocks.append(stock)

    df = pd.DataFrame(out_stocks)
    df.to_csv("/home/dylan/Documents/StockBot/outfiles/Stock_data.csv", index=False, header=False)

def Add_Back_Title(bool_val, hold_val, new_list):
    if bool_val:
        new_list.insert(0, hold_val)
    return new_list



def Extract_Title(bool_val, hold_val, list_data):
    if bool_val and len(list_data[0]) > 0:
        hold_val = list_data[0]
        list_data.pop(0)
    return hold_val


def Check_Search_Words(word):
    search_words = Create_list("/home/dylan/Documents/StockBot/Data_collection/Search_words.txt")
    substring_in_list = any(word in string for string in search_words)
    return substring_in_list


def Create_list(file):
    with open(file, "r") as f:
        search = f.read().splitlines()
    f.close()
    return search


def CSV_To_List(Csv):
    with open(Csv, newline='') as f:
        reader = csv.reader(f)
        return list(reader)


def Clean_Data_Main():
    count = 30
    price = 50

    Clean_stock_data(price, count)
    time.sleep(4)
    Clean_Data("/home/dylan/Documents/StockBot/outfiles/Graphs/Graph_total.csv", True, count, price)


