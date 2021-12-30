import csv
import pandas as pd 
path = 'Medium_loading_2_Experiment_2.csv' #要匯入的csv檔案名稱
with open(path, newline='') as csvfile:
  with open('after.csv', 'w', newline='') as f: #data為匯出的檔案名稱
    rows = csv.reader(csvfile)
    writer = csv.writer(csvfile) #建立CSV檔寫入器
    count=0 #設一個計數器
    for row in rows:
        if count<5: #到第六列之前都正常輸出
          del row 
        else: #第六列開始做分割
          w = csv.writer(f)
          w.writerow(row[0].split()) #將list做分割
        #   print(row[0].split())
        count+=1
data = pd.read_csv('after.csv')
# print(data.columns)
data.drop(columns=['Sweep','Date','Time','Milliseconds'],inplace=True, axis=1)
# data=data.columns
# print(data)
data.to_csv("after.csv", header = False,index=False)