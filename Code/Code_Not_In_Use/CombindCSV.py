from datetime import date
import pandas as pd

def Get_Date():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    return d1
def Combiner():
        Create_New_CSV("testcsv1.csv", "Combiner.csv")
        Create_Final_CSV("Combiner.csv")
        #Clear_File("Combiner.csv")

def Create_Final_CSV(file):
    word_list = []
    with open(file, "r") as f:
        search = f.read().splitlines()
        for line in search:
            first_line = line.split(",")
            word_list.append(first_line)
        word_list.remove(word_list[0])

        fs = open("Combiner.csv", "w")
        fs.write("Date," + Get_Date()+ "\n")

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
            print(total_val)
            fs.write(item[0] + ",")
            fs.write(str(total_val))
            fs.write("\n")


def Clear_File(file):
    file = open(file, 'w')
    file.write("Date,")
    file.close()
def Create_New_CSV(infile1, infile2):
    df1 = pd.read_csv(infile1, error_bad_lines=False)
    df2 = pd.read_csv(infile2, error_bad_lines=False)
    merged = df1.merge(df2, on="Date", how="outer").fillna("")
    merged.to_csv(infile2, index=False)

def main():
    Combiner()

main()