import re
from threading import Thread
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time



def OpenSite(stock_name, count):
    site = "https://www.marketwatch.com/investing/stock/" + stock_name
    list_data = []
    html_content = requests.get(site).text
    reg_str = '<bg-quote class="value" field="Last" format="0,0.00"(.*?)/bg-quote>'
    reg_str2 = '<bg-quote field="change" format="0,0.00" (.*?)/bg-quote></span>'
    reg_str3 = '<bg-quote field="percentchange" format="0,0.00%"(.*?)/bg-quote>'

    res = re.findall(reg_str, html_content)
    list_data.append(res.pop())
    res += re.findall(reg_str2, html_content)
    list_data.append(res.pop())
    res += re.findall(reg_str3, html_content)
    list_data.append(res.pop())
    Write_Data(list_data, stock_name, count)

def Write_Data(list, stock_name, count):
    reg_str4 = ">(.*?)<"
    with open("StockPrice.csv", "a+") as f:
        f.write(stock_name + "," + "count:"+count + ",")
        for item in list:
            item = re.findall(reg_str4, item)
            item = str(item).strip().replace("]", "").replace("[", "").replace("'", "")
            f.write(item + ",")
        f.write("\n")

def main():
    open("StockPrice.csv", "w").close()
    with open(r"C:\Users\dylan\PycharmProjects\Search_bot\FileManager\Combiner.csv", "r") as f:
        for stock in f:
            stock = stock.split(",")
            count = stock[1].replace("\n", "")
            try:
                try:
                    if float(count) >= 5:
                        OpenSite(stock[0], count)
                except ValueError:
                    continue
            except IndexError:
                continue



main()