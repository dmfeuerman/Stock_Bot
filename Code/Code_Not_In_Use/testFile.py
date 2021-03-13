

test_str = '/home/dylan/Documents/StockBot/outfiles/Graphs/out_graphs_data/data_number1.csv'

# printing original string
print("The original string is : " + str(test_str))

# initializing sub string
sub_str = "out_graphs_data/"

# slicing off after length computation
res = test_str[test_str.index(sub_str) + len(sub_str):]
res = res.replace(".csv", ".pdf")
# printing result
print("The string after removal : " + str(res))