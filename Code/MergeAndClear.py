import pandas as pd
from datetime import date

def Clear_file(files):
    f = open(files, "w")
    
    f.write("Date")
    f.close()

def Create_New_CSV(infile1, infile2):
    df1 = pd.read_csv(infile1, error_bad_lines=False)
    df2 = pd.read_csv(infile2, error_bad_lines=False)
    merged = df1.merge(df2, on="Date", how="outer").fillna("")
    merged.to_csv(infile2, index=False)
    return df2


def Merge_Clear_Main():
    Create_New_CSV("/home/dylan/Documents/StockBot/outfiles/Combiner.csv", "/home/dylan/Documents/StockBot/outfiles/Total_data.csv")
    Clear_file("/home/dylan/Documents/StockBot/outfiles/Combiner.csv")
