import math
import shutil
import time

import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import csv

def Make_CSV(new_list, file):
    df = pd.DataFrame(new_list)
    df.to_csv(file, index=False, header=False)

def Graph_Data(file):
    df = pd.read_csv(file, index_col='Date')
    df = df.T
    df.plot(legend=True)
    plt.savefig(Switch_CSV_PDF(Out_File_Name(file)))

def Out_File_Name(file):
    sub_str = "Graphs/"
    new_directory = file[:file.index(sub_str) + len(sub_str)]
    sub_str2 = "out_graphs_data/"
    new_file = file[file.index(sub_str2) + len(sub_str2):]
    out_graph_file = new_directory + "out_graphs/" + new_file
    return out_graph_file

def Switch_CSV_PDF(file):
    return file.replace(".csv", ".pdf")

def Graph_files():
    for filename in os.listdir("/home/dylan/Documents/StockBot/outfiles/Graphs/out_graphs_data/"):
        if filename.endswith(".csv"):
            Graph_Data("/home/dylan/Documents/StockBot/outfiles/Graphs/out_graphs_data/" + filename)
            continue
        else:
            continue

def CSV_To_List(Csv):
    with open(Csv, newline='') as f:
        reader = csv.reader(f)
        return list(reader)

def Make_files():

    list_data = CSV_To_List("/home/dylan/Documents/StockBot/outfiles/Graphs/Graph_total.csv")
    header = list_data[0]

    count = 1
    list_len = len(list_data)
    bool_val = False
    while not bool_val:
        plus_ten = count + 10
        if (count + 10) >= list_len:
            new_list = list_data[count:]
            plus_ten = list_len
            bool_val = True
        else:
            new_list = list_data[count:plus_ten]
        new_list.insert(0, header)
        title_val = plus_ten - 1
        file = "/home/dylan/Documents/StockBot/outfiles/Graphs/out_graphs_data/graph_data_num_" + str(title_val) + ".csv"
        Make_CSV(new_list, file)
        new_list.clear()
        count = plus_ten


def Delete_files(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def Make_Graph():
    Delete_files("/home/dylan/Documents/StockBot/outfiles/Graphs/out_graphs_data")
    Delete_files("/home/dylan/Documents/StockBot/outfiles/Graphs/out_graphs")
    time.sleep(2)
    Make_files()
    Graph_files()
