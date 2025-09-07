import pandas as pd
df=pd.read_csv(r'C:\Users\DELL\code\sales-data.csv')
summary=df.groupby('Region')['Sales'].sum().reset_index()
with pd.ExcelWriter('sales_report.xlsx',engine='openpyxl')as writer:
    df.to_excel(writer,index=False,sheet_name='Raw Data')
    summary.to_excel(writer,index=False,sheet_name='Summary')