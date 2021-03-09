import re
from threading import Thread
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd


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
    #print(list_data)
    Write_Data(list_data, stock_name, count)

def Write_Data(lists, stock_name, count):
    reg_str4 = ">(.*?)<"
    non_dec = re.compile(r'[^0-9-.]')
    with open("/home/pi/Search/outfiles/Stock_data.csv", "a+") as fs:
        fs.write(stock_name + "," +count + ",")
        for item in lists:
            item = re.findall(reg_str4, item)
            item = non_dec.sub('', str(item))
            item = str(item).strip()
            fs.write(item + ",")
        fs.write("\n")
        
        
    
                       

def main():
    files = open("/home/pi/Search/outfiles/Stock_data.csv", "w")
    files.write("Stock Name, #count, $, points, %,\n")
    files.close()
    with open("/home/pi/Search/outfiles/Combiner.csv", "r") as f:
        for stock in f:
            stock = stock.split(",")
                
            try:
                count = stock[1].replace("\n", "")
                try:
                    
                    if float(count) >= 10:
                        OpenSite(stock[0], count)
                except ValueError:
                        continue
            except IndexError:
                continue

    
    



main()
