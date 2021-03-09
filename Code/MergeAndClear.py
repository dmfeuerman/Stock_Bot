import pandas as pd
from datetime import date

def Clear_file(files, onBool):
    f = open(files, "w")
    
    f.write("Date" +",")
    f.close()

def Create_New_CSV(infile1, infile2):
    df1 = pd.read_csv(infile1, error_bad_lines=False)
    df2 = pd.read_csv(infile2, error_bad_lines=False)
    merged = df1.merge(df2, on="Date", how="outer").fillna("")
    merged.to_csv(infile2, index=False)
    return df2


def main():
    df = Create_New_CSV("/home/dylan/Documents/StockBot/outfiles/Combiner.csv", "/home/dylan/Documents/StockBot/outfiles/Total_data.csv")
    Clear_file("/home/dylan/Documents/StockBot/outfiles/Combiner.csv", True)
    #Clear_file("/home/pi/Search/outfiles/Sorted_data/Sorted_by_cost.csv", False)
    #Clear_file("/home/pi/Search/outfiles/Sorted_data/Sorted_by_count.csv", False)
    #Clear_file("/home/pi/Search/outfiles/Sorted_data/Sorted_by_percentage.csv", False)
    #Clear_file("/home/pi/Search/outfiles/Sorted_data/Sorted_by_points.csv", False)

main()
