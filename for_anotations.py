import time


rows = int(input("enter rows:"))
columns = int(input("enter columns:"))
symbol = int(input("enter symbol:")) 

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")