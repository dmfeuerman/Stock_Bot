import pandas as pd
import csv


def Clean_Data(file, bool_val, COUNT, PRICE):
    list_data = CSV_To_List(file)
    stock_list = CSV_To_List("/home/dylan/Documents/StockBot/outfiles/Stock_data.csv")

    hold_val = []
    new_list = []
    stock_names = []

    hold_val = Extract_Title(bool_val, hold_val, list_data)

    for val in list_data:
        if Check_Search_Words(val[0]):
            for stock in stock_list:
                try:
                    if (float(val[1]) >= COUNT) and (float(stock[2]) <= PRICE):
                        if val[0] not in stock_names:
                            new_list.append(val)
                            stock_names.append(val[0])
                except ValueError:
                    continue

    Add_Back_Title(bool_val, hold_val, new_list)
    df = pd.DataFrame(new_list)
    df.to_csv(file, index=False, header=False)



def Add_Back_Title(bool_val, hold_val, new_list):
    if bool_val:
        new_list.insert(0, hold_val)


def Extract_Title(bool_val, hold_val, list_data):
    if bool_val:
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


def Clean_Data_Main(count, price):
    Clean_Data("/home/dylan/Documents/StockBot/outfiles/Total_data.csv", True, count, price)
    Clean_Data("/home/dylan/Documents/StockBot/outfiles/Stock_data.csv", False, count, price)
    Clean_Data("/home/dylan/Documents/StockBot/outfiles/Graphs/Graph_total.csv", True, count, price)
