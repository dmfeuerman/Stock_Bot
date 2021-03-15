import threading
import urllib
import re
from urllib.error import HTTPError
from urllib import request
def OpenSite(stock_name, count):
    lists = []
    site = "https://markets.businessinsider.com/stocks/" + stock_name + "-stock"
    #time.sleep(5)

    try:
        with urllib.request.urlopen(site) as response:
            html = response.read()
        #Print_HTML(html)
        reg_str = '"category":"Stock"(.*?),"relativeValue":(.*?),"absoluteValue":(.*?),"currentValue":(.*?),'
        res = re.findall(reg_str, str(html))
        #Print_HTML(str(res))
        non_decimal = re.compile(r'[^\d.-]+')
        for item in res:
            for val in item:

                val = non_decimal.sub('', str(val))
                val = str(val).strip()
                try:
                    val = str(round(float(val), 2))
                except ValueError:
                    continue
                lists.insert(0, val)

        lists = list(filter(None, lists))
        Make_File(lists, stock_name, count)
    except HTTPError:
        var = "None"

def Get_File():
    file = "/home/dylan/Documents/StockBot/outfiles/Stock_data.csv"
    with open(file, "w") as f:
        f.write("")
    f.close()
    return file


def Make_File(lists, stock_name, count):
    with open("/home/dylan/Documents/StockBot/outfiles/Stock_data.csv", "a+") as f:
        f.write(stock_name + ',' + count)
        for item in lists:
             f.write("," + item)
        f.write("\n")


def Stock_Data_Main():
    Get_File()
    with open("/home/dylan/Documents/StockBot/outfiles/Combiner.csv", "r") as f:
        for stock in f:
            stock = stock.split(",")
                
            try:
                count = stock[1].replace("\n", "")
                try:
                    
                    if float(count) >= 15:
                        x = threading.Thread(target=OpenSite, args=(stock[0], count))
                        x.start()
                except ValueError:
                        continue
            except IndexError:
                continue
    return True

