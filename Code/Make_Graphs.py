import pandas as pd
import matplotlib.pyplot as plt

def Graph_Count():
    df = pd.read_csv('/outfiles/Sorted_data/Graph_total.csv', index_col='Date')
    df = df.T
    df.plot(legend=True)  # plot usa column
    plt.savefig("/home/dylan/Documents/StockBot/outfiles/Sorted_data/Graph.pdf")


def Graph_Price():
    df = pd.read_csv('/outfiles/Sorted_data/Graph_total.csv', index_col='Date')
    df = df.T
    df.plot(legend=True)  # plot usa column
    plt.savefig("/home/dylan/Documents/StockBot/outfiles/Sorted_data/Graph.pdf")
