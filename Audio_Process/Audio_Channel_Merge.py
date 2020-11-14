import wave
import numpy as np
import struct
import matplotlib.pyplot as plt

import rawutil


def check_sys():
    val = 0x12345678
    pk = struct.pack('i', val)
    hex_pk = hex(ord(pk[0]))
    if hex_pk == '0x78':
        return 0 # '小端‘
    elif hex_pk == '0x12':
        return 1 # '大端'

# flag = check_sys()
# if(flag):
#     print('big')
# else:
#     print('small')
# 只读方式打开WAV文件
wf = wave.open(r'Ses01F_impro01_F000_S1.wav', 'rb')

fp=open(r'1.wav','rb')
nframes = wf.getnframes()
framerate = wf.getframerate()
str_data = wf.readframes(nframes)
sample_width = wf.getsampwidth()
channel = wf.getnchannels()
bytesPerSample = int(len(str_data) / nframes / channel)
# chunk=fp.read(bytesPerSample*nframes)
a=[]
for i in range(nframes):
    j = i * channel
    bytess = str_data[j * bytesPerSample:j * bytesPerSample + bytesPerSample]
    # value = struct.unpack('<h',bytess)[0]
    value = rawutil.unpack('<1u', bytess)[0]
    a.append(value)
    # print(value)
a2 = np.array(a, dtype='int32')
mean = np.mean(a2)
std = np.std(a2)
a2 = (a2 - mean) / std
a2 = a2.astype(np.float16)
print(a2.dtype)
wf.close()
time = np.arange(0, nframes)*(1.0/framerate)
plt.subplot(311)
plt.plot(time, a2, c='r')
plt.show()
#
# print("channel:",channel)
# print("framerate:",framerate)
# print("nframe:",nframes)
# # 将波形数据转换成数组
# wave_data = np.fromstring(str_data, dtype=np.int16)
# print("wave_data:",wave_data.shape)
# wave_data.shape = (-1, 2)
# wave_data = wave_data.T
# mono_wave = (wave_data[0]+wave_data[1])/2
# print(mono_wave)
#
# time = np.arange(0, nframes)*(1.0/framerate)
# print("time:",time.shape)
# plt.subplot(311)
# plt.plot(time, wave_data[0], c='r')
# plt.subplot(312)
# plt.plot(time, wave_data[1], c='r')
# plt.subplot(313)
# plt.plot(time, mono_wave, c='r')
# # plt.plot(time, wave_data, c='r')
# plt.show()
#
# #save wav file
# wf_mono = wave.open("mono.wav",'wb')
# wf_mono.setnchannels(1)
# wf_mono.setframerate(framerate)
# wf_mono.setsampwidth(sample_width)
# for i in mono_wave:
#     data = struct.pack('<h', int(i))
#     wf_mono.writeframesraw( data )
# wf_mono.close()
