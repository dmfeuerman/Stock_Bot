from Reddit_Get_Data import Reddit_Get_Data_Main
from Graph import Make_Graph
from Clean_Data import Clean_Data_Main
from StockData2 import Stock_Data_Main
from upload import Upload_Main
from Once_daily import Once_Daily_Main
from MergeAndClear import Merge_Clear_Main
from Create_Graph_Data import Create_Graph_Data_Main
from datetime import datetime


def Get_Hour():
    return datetime.now().strftime("%H")


def main():
    hour = float(Get_Hour())

    Reddit_Get_Data_Main()
    if hour == 11:
        Once_Daily_Main()
    if 7 <= hour <= 19:
        if hour >= 11:
            Clean_Data_Main(20, 40)
        else:
            Clean_Data_Main(40, 40)

        Stock_Data_Main()
        Create_Graph_Data_Main()
        Make_Graph()
        Upload_Main()

    if hour == 0:
        Merge_Clear_Main()


main()
