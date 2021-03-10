import pandas as pd
import csv
import operator


def Orginize_Data(index, out):
    df = open("/home/dylan/Documents/StockBot/outfiles/Stock_data.csv",
              'r')
    next(df)
    read_df = csv.reader(df, delimiter=',')
    sort = sorted(read_df, key=lambda x: float(x[index]), reverse=True)
    f = open(out, "w")
    f.write("Stock,Count,Price,Points,Percentage\n")
    wr = csv.writer(f, dialect='excel')
    wr.writerows(sort)
    f.close()
    df.close()

def main():
    # Stock Name
    #Orginize_Data(0, "/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_Stock_name.csv")
    # Count
    Orginize_Data(1, "/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_count.csv")
    # Price
    Orginize_Data(2, "/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_price.csv")
    # Points
    Orginize_Data(3, "/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_points.csv")
    # Percent
    Orginize_Data(4, "/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_percentage.csv")


main()
