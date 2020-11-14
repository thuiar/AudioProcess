from collections import defaultdict
import os
import pandas as pd
import wave
import numpy as np
feature = []
train_file = open(r'C:\Users\93710\Desktop\train.txt','r')
train_file = train_file.read()
train_file = train_file.split(',')
train_file = train_file[:-1]
for i in range(len(train_file)):

    file_path = 'C:\\Users\\93710\\Desktop\\MOSI_datasets\\'+str(train_file[i])+'.wav'
    f = wave.open(file_path, "rb")
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    if nchannels ==1:
        data = []
        path =  'C:\\Users\\93710\\Desktop\\mosi_out_segment\\' + str(train_file[i]) + '-1.txt'
        file = open(path)
        file_data = file.read()
        file_split = file_data.split("'noname',")
        file_feature = file_split[1]
        file_split1 = file_feature.split(',')
        for j in range(1582):
            data.append(file_split1[j])
        feature.append(data)
    else:
        for j in range(2):
            data = []
            path ='C:\\Users\\93710\\Desktop\\mosi_out_segment\\'+str(train_file[i])+'-'+str(j+1)+'.txt'
            file = open(path)
            file_data = file.read()
            file_split = file_data.split("'noname',")
            file_feature = file_split[1]
            file_split1 = file_feature.split(',')
            for j in range(1582):
                data.append(file_split1[j])
            feature.append(data)
feature = np.array(feature)
print(feature.shape)
np.save("C:\\Users\\93710\\Desktop\\feature1582_train_new.npy", feature)



