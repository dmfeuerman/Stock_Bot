import re
import threading
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os.path
from os import path
from datetime import datetime

def OpenSite(stock_name, count, stock_list_data):
    site = "https://www.marketwatch.com/investing/stock/" + stock_name
    
    html_content = requests.get(site).text
   
   
    stock_price = '<bg-quote class="value" field="Last" format="0,0.00"(.*?)/bg-quote>'
    points_change = '<bg-quote field="change" format="0,0.00" (.*?)/bg-quote></span>'
    percentage_change = '<bg-quote field="percentchange" format="0,0.00%"(.*?)/bg-quote>'
    stock_volume = '<span class="primary">Volume(.*?)/span>'
    stock_close = ' <td class="table__cell u-semi"(.*?)/td>'
    daily_open = 'day-open(.*?) '
    daily_low_range = 'bar-low(.*?) '
    daily_high_range = 'bar-high(.*?) '


    # Stock price, change$, Perc
    Get_Stock_Data(html_content, stock_list_data, stock_price)
    Get_Stock_Data(html_content, stock_list_data, points_change)
    Get_Stock_Data(html_content, stock_list_data, percentage_change)

    # Num shares
    stock_data = re.findall(stock_volume, html_content)
    stock_data = str(stock_data).replace(": ", ">")
    #print(stock_data)
    stock_list_data.append(stock_data)

    # open low range high range
    Get_Stock_Data_In_HTML_Tags(daily_open, html_content, stock_list_data)
    Get_Stock_Data(html_content, stock_list_data, stock_close)
    Get_Stock_Data_In_HTML_Tags(daily_low_range, html_content, stock_list_data)
    Get_Stock_Data_In_HTML_Tags(daily_high_range, html_content, stock_list_data)
    Write_Data(stock_list_data, stock_name, count)

def Print_HTML(html):
    print(html)
    quit()
    
def Get_Stock_Data_In_HTML_Tags(daily_open, html_content, stock_list_data):
    stock_data1 = re.findall(daily_open, html_content)[1]
    stock_data1 = str(stock_data1).replace('="', '>').replace('"', '<')
    stock_list_data.append(stock_data1)


def Get_Stock_Data(html_content, stock_list_data, stock_data_input):
    stock_data = re.findall(stock_data_input, html_content)
    stock_list_data.append(stock_data.pop())

def Get_File(stock_name):
    file_out = r"/home/pi/Search/Stock_Csvs/" + stock_name + ".csv"
    if os.path.isfile(file_out):
        return file_out
    else:
        stock_file = open(file_out, "w")
        stock_file.write("Date,Count,Price,Points change,Percentage changed,Volume,Open,Close,Low-Range,High-range\n")
        stock_file.close()
    return file_out

def Write_Data(stock_list, stock_name, count):
    reg_str4 = ">(.*?)<"
    non_dec = re.compile(r'[^0-9-.MTHB]')
    with open(Get_File(stock_name), "a+") as f:
        f.write(Get_Date_Time() + "," + count + ",")
        for item in stock_list:
            item = re.findall(reg_str4, item)
            item = non_dec.sub('', str(item))
            item = str(item).strip()
            item = Convert_Data(item)
            f.write(item + ",")
        f.write("\n")
        f.close()


def Convert_Data(item):
    if "M" in item:
        item = item.replace('M', "")
        item = float(item) * 1000000
        
    elif "B" in item:
        item = item.replace('B', "")
        item = float(item) * 1000000000
    
    elif "T" in item:
        item = item.replace('T', "")
        item = float(item) * 1000
       
    elif "H" in item:
        item = item.replace('H', "")
        item = float(item) * 100
        
    
    item = str(item)
    return item


def Get_Date_Time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def main():
    with open(r"/home/pi/Search/outfiles/Combiner.csv", "r") as f:
        for stock in f:
            stock = stock.split(",")
            count = stock[1].replace("\n", "")
            try:
                try:
                    if float(count) >= 50:
                        stock_list_data = []
                        x = threading.Thread(target =OpenSite, args=(stock[0], count, stock_list_data))
                        x.start()
                except ValueError:
                    continue
            except IndexError:
                continue
        f.close()



#main()
