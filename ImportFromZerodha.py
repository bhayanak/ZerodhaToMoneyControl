# Can’t figure out Date of purchase so its todays.
# Input a csv file downloaded from zerodha(kite), run program like:
#   python ImportFromZerodha.py zerodha.csv
# Output will be a csv file which can be imported to moneycontrol
import sys
import csv
import time
import os

fileName = 'moneycontrol.csv'
try:
    os.remove(fileName)
except OSError:
    pass

csv_list = [["BSE/NSE/ISIN Code", "Buy Date", "Buy Quantity", "Buy Price", ]]

# "Instrument","Qty.","Avg cost.","LTP","Current value","P&L","Net chg.","Day's chg."
with open(sys.argv[1]) as csvfile:
    with open(fileName, "w") as f:
        writer = csv.writer(f)
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['Instrument'], row['Qty.'], row['Avg cost.'])
            data = []
            data.append(row['Instrument'])
            data.append(time.strftime("%d-%m-%Y"))
            data.append(row['Qty.'])
            data.append(format(float(row['Avg cost.']),'.2f'))
            print(data)
            csv_list.append(data)
        writer.writerows(csv_list)
