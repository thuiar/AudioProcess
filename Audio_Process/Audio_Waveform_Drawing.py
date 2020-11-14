
# -*- coding: utf-8 -*-
import wave
import pylab as pl
import  os
import numpy as np

# 打开WAV文档
path_1 = 'C:\\Users\\ykc\\Desktop\\PG_sentiment\\data\\D'
path_2 = 'C:\\Users\\ykc\\Desktop\\wav波形图\\D'

for file in os.listdir(path_1):
    path_wav = path_1+'\\'+file
    f = wave.open(path_wav)
    # 读取格式信息
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]

    # 读取波形数据
    str_data = f.readframes(nframes)
    f.close()
    # 将波形数据转换为数组
    wave_data = np.fromstring(str_data, dtype=np.short)
    if nchannels == 1:
        wave_data = np.tile(wave_data, 2)
    wave_data.shape = -1, 2
    wave_data = wave_data.T
    time = np.arange(0, nframes) * (1.0 / framerate)
    path_save = path_2+'\\'+file+'.jpg'
    pl.plot(time, wave_data[0])
    pl.axis('off')
    pl.savefig(path_save)
    # pl.show()
    pl.close()
# f = wave.open(r"1.wav", "rb")
# # 读取格式信息
# # (nchannels, sampwidth, framerate, nframes, comptype, compname)
# params = f.getparams()
# nchannels, sampwidth, framerate, nframes = params[:4]
# # 读取波形数据
# str_data = f.readframes(nframes)
# f.close()
# #将波形数据转换为数组
# wave_data = np.fromstring(str_data, dtype=np.short)
# wave_data.shape = -1, 2
# wave_data = wave_data.T
# time = np.arange(0, nframes) * (1.0 / framerate)
# # 绘制波形
# # pl.subplot(211)
# pl.plot(time, wave_data[0])
# # pl.subplot(212)
# # pl.plot(time, wave_data[1], c="g")
# # pl.xlabel("time (seconds)")
# pl.axis('off')
# pl.show()
# pl.save()
