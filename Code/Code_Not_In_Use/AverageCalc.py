from datetime import datetime
import csv
def Get_Hour():

    return datetime.now().strftime("%H")

def Get_File(hour):
    list_data = CSV_To_List("/home/dylan/Documents/StockBot/outfiles/Average_files/" + hour + ".csv")
    stock_list = []
    for val in list_data:
        for stock in stock_list:
            if val[0] == stock[0]:
                print("hi")

def CSV_To_List(Csv):
    with open(Csv, newline='') as f:
        reader = csv.reader(f)
    return list(reader)

def main():
    hour = Get_Hour()
    Get_File(hour)


main()