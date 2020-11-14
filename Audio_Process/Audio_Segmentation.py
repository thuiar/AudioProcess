import os
import wave
import numpy as np
import pandas as pd
train_file = open(r'C:\Users\93710\Desktop\train.txt','r')
train_file = train_file.read()
train_file = train_file.split(',')
train_file = train_file[:-1]

label_path = 'C:\\Users\\93710\\Desktop\\mosi_label.csv'
label = pd.read_csv(label_path)
label = label['label']
label_new = []#按照train.txt的顺序
for i in range(len(train_file)):
    a = train_file[i]
    a = int(a)-1
    label_ = label[a]#单文件label
    file_path = 'C:\\Users\\93710\\Desktop\\MOSI_datasets\\'+str(train_file[i])+'.wav'
    f = wave.open(file_path, "rb")
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = f.readframes(nframes)
    wave_data = np.fromstring(str_data, dtype=np.int16)
    if nchannels ==2:
        wave_data = wave_data.reshape(-1, 2).T
        for j in range(2):
            save_file  = 'C:\\Users\\93710\\Desktop\\切分audio\\'+str(train_file[i])+'-'+str(j+1)+'.wav'
            f = wave.open(save_file, "wb")  #
            # 配置声道数、量化位数和取样频率
            f.setnchannels(1)
            f.setsampwidth(sampwidth)
            f.setframerate(framerate)
            # 将wav_data转换为二进制数据写入文件
            f.writeframes(wave_data[j].tostring())
            label_new.append(label_)
            f.close()
    else:
        save_file = 'C:\\Users\\93710\\Desktop\\切分audio\\' + str(train_file[i]) + '-1.wav'
        f = wave.open(save_file, "wb")  #
        # 配置声道数、量化位数和取样频率
        f.setnchannels(1)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        # 将wav_data转换为二进制数据写入文件
        f.writeframes(wave_data.tostring())
        label_new.append(label_)
        f.close()
np.save("C:\\Users\\93710\\Desktop\\label_train_new.npy", label_new)


# file_path =r'C:\Users\93710\Desktop\MOSI_datasets\2199.wav'

