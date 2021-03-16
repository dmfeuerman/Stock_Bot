import time

from Reddit_Get_Data import Reddit_Get_Data_Main
from Graph import Make_Graph
from Clean_Data import Clean_Data_Main
from StockData2 import Stock_Data_Main
from upload import Upload_Main
from Once_daily import Once_Daily_Main
from MergeAndClear import Merge_Clear_Main
from Create_Graph_Data import Create_Graph_Data_Main
from datetime import datetime
from SortCSVs import Sort_CSV_main
from Upload_Not_Sorted_Data import Upload_Main_Unsorted


def Get_Hour():
    return datetime.now().strftime("%H")


def main():
    hour = float(Get_Hour())

    Reddit_Get_Data_Main()
    Stock_Data_Main()
    time.sleep(5)
    Upload_Main_Unsorted()
    if hour == 7:
        Once_Daily_Main()
    if 7 <= hour <= 19:
        time.sleep(5)
        Create_Graph_Data_Main()
        time.sleep(5)
        Clean_Data_Main()
        time.sleep(5)
        Sort_CSV_main()
        Make_Graph()
        Upload_Main()

    if hour == 0:
        Merge_Clear_Main()


main()
