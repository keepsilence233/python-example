import pandas as pd

#excel file path
path = '/Users/chinese.youth/Desktop/工作簿1.xlsx'

excel = pd.read_excel(path, sheet_name='Sheet1')

print(excel.columns)
