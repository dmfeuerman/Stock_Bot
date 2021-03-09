import pandas as pd


def Orginize_Data():
     df = pd.read_csv("/home/dylan/Documents/StockBot/outfiles/Stock_data.csv", error_bad_lines=False)
     sorted_df_points = df.sort_values(by=['Points'], ascending=False)
     sorted_df_count = df.sort_values(by=['Count'], ascending=False)
     sorted_df_percent = df.sort_values(by=['Percentage'], ascending=False)
     sorted_df_price = df.sort_values(by=['Price'], ascending=False)


     #open("/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_points.csv","w").close()
     #open("/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_count.csv","w").close()
     #open("/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_percentage.csv","w").close()
     #open("/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_cost.csv","w").close()

     print(sorted_df_count)
     sorted_df_points.to_csv("/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_points.csv", index_label=False)
     sorted_df_count.to_csv("/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_count.csv", index_label=False)
     sorted_df_percent.to_csv("/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_percentage.csv", index_label=False)
     sorted_df_price.to_csv("/home/dylan/Documents/StockBot/outfiles/Sorted_data/Sorted_by_cost.csv", index_label=False)

def main():
     Orginize_Data()
     
     
     
     
     
     
#main()
    
    
