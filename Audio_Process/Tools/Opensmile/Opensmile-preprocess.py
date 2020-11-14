from collections import defaultdict
import os
import pandas as pd
path = 'C:\\Users\\93710\\Desktop\\MOSI_out'
file_list = os.listdir(path)
data_unifile = []
file_feature_data = []
for i in range(len(file_list)):
    file_path = path+'\\'+file_list[i]
    file = open(file_path)
    file_data = file.read()
    file_split = file_data.split("'noname',")
    file_feature = file_split[1]
    file_split1 = file_feature.split(',')
    for j in range(1582):
        data_unifile.append(file_split1[j])
    file_feature_data.append(data_unifile)
dict = {}
column = []
for i in range(2199):
    column.append(i)
    dict[i] = file_feature_data[i]
df = pd.DataFrame(dict, columns=column)
print(df)
