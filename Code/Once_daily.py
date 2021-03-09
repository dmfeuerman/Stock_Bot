import re
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import schedule


def Create_Storage():
    global dic
    dic = dict()


Create_Storage()


def Copy_site(site, outfile):
    driver = OpenSite(site)
    
    Search_Link_Text(driver, 30)
    data = Get_Data(driver)
    Make_Dic(data)
    Print_Dic("/home/dylan/Documents/StockBot/Data_collection/Single_scrap2.csv",outfile)

    Driver_Close(driver)


def Get_Data(driver):
    html = driver.page_source
    reg_str = '<h3 class="_eYtD2XCVieq6emjKBH3m">(.*?)</h3>'
    res = re.findall(reg_str, html)
    reg_str2 = '<p class="_1qeIAgB0cPwnLhDF9XSiJM">(.*?)</p>'
    res2 = re.findall(reg_str2, html)
    res += res2
    return res


def OpenSite(site):
    driver = webdriver.Chrome("/home/dylan/Downloads/chromedriver")
    driver.get(site)
    driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("return document.body.scrollHeight")
    return driver


def Search_Link_Text(driver, set_time):
    future_time = Future_Time(set_time)
    while Exact_time() != future_time:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("return document.body.scrollHeight")

        try:
            element = driver.find_element_by_link_text("1 day ago")
            if element is not None:
                break
        except NoSuchElementException:
            continue


def Make_Dic(data):
    search = Filter_Words()
    Compile_Dic(search, data)

    return dic


def Test_Print_Value_List(res):
    print("The Strings extracted : " + str(res))


def Compile_Dic(search_words, list_words):
    for item in list_words:
        words = Clean_Data(item)
        for word in words:
            word = word.strip(",.$#%&!?|\/")
            if word in search_words:
                if word in dic:
                    dic[word] = dic[word] + 1
                else:
                    dic[word] = 1


def Filter_Words():
    with open("/home/dylan/Documents/StockBot/Data_collection/Search_words.txt", "r") as f:
        search = f.read().splitlines()
    f.close()
    return search


def Clean_Data(item):
    item = item.lower()
    line = item.strip()
    word = line.split(" ")
    return word


def Get_Date():
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    return dt_string


def Print_Dic(infile, outfile):
    file = open(infile, "w")
    file.write("Date," + Get_Date() + "\n")
    for w in sorted(dic, key=dic.get, reverse=True):
        try:
            file.write(w.strip() + ',' + str(dic[w]).strip() + "\n")
        except UnicodeEncodeError:
            continue
    file.write("\n")
    file.close()
    Combiner()
    Create_New_CSV(infile, outfile)


def Create_New_CSV(infile1, infile2):
    df1 = pd.read_csv(infile1, error_bad_lines=False)
    df2 = pd.read_csv(infile2, error_bad_lines=False)
    merged = df1.merge(df2, on="Date", how="outer").fillna("")
    merged.to_csv(infile2, index=False)


def Driver_Close(driver):
    driver.close()
    Create_Storage()
    
from datetime import date
import pandas as pd

def Get_Current_Date():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    return d1
def Combiner():
    Create_New_CSV("/home/dylan/Documents/StockBot/Data_collection/Single_scrap.csv",
                   "/home/dylan/Documents/StockBot/outfiles/Combiner.csv")
    Create_Final_CSV("/home/dylan/Documents/StockBot/outfiles/Combiner.csv")

def Create_Final_CSV(file):
    word_list = []
    with open(file, "r") as f:
        search = f.read().splitlines()
        for line in search:
            first_line = line.split(",")
            word_list.append(first_line)
        word_list.remove(word_list[0])

        fs = open("/home/dylan/Documents/StockBot/outfiles/Combiner.csv", "r+")
        fs.write("Date," + Get_Current_Date()+ "\n")

        for item in word_list:
            count = 1
            total_val = 0
            while True:
                try:
                    try:
                        total_val += float(item[count])
                        count += 1
                    except ValueError:
                        count += 1
                        continue
                except IndexError:
                    break
            fs.write(item[0] + ",")
            fs.write(str(total_val))
            fs.write("\n")

def Exact_time():
    current_time = time.ctime()
    return current_time

def Future_Time(set_time):
    future = time.time() + set_time
    future = time.ctime(future)
    return future


def main():
        Copy_site('https://www.reddit.com/r/investing/new/', "/home/dylan/Documents/StockBot/Data_collection/Reddit_Investing_output.csv")
        Copy_site('https://www.reddit.com/r/Forex/new/', "/home/dylan/Documents/StockBot/Data_collection/Reddit_Forex_output.csv")
        Copy_site('https://www.reddit.com/r/Daytrading/new/', "/home/dylan/Documents/StockBot/Data_collection/Reddit_DayTrading_output.csv")
        Copy_site(' https://www.reddit.com/r/Trading/new/', "/home/dylan/Documents/StockBot/Data_collection/Reddit_Trading_output.csv")
        Copy_site(' https://www.reddit.com/r/IndiaInvestments/new/', "/home/dylan/Documents/StockBot/Data_collection/Reddit_II_output.csv")

main()
