import pandas as pd
#read data from csv
csv_data=pd.read_csv("data.csv")
print("CSV Data:")
print(csv_data)
#write to excel
csv_data.to_excel("data_output.xlsx",index=False)
#read back from excel
excel_data=pd.read_excel("data_output.xlsx")
print("\nExcel Data:")
print(excel_data)


