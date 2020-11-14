import os
audio_path=r'C:\Users\93710\Desktop\切分audio'
output_path=r'C:\Users\93710\Desktop\mosi_out_segment'
audio_list=os.listdir(audio_path)
for audio in audio_list:
    if audio[-4:]=='.wav':
        this_path_input=os.path.join(audio_path,audio)
        this_path_output=os.path.join(output_path,audio[:-4]+'.txt')
        cmd='cd /d C:/Users/93710/Desktop/opensmile-2.3.0/opensmile-2.3.0/bin/Win32 && SMILExtract_Release -C C:/Users/93710/Desktop/opensmile-2.3.0/opensmile-2.3.0/config/emobase2010.conf -I '+this_path_input+' -O '+this_path_output
        # cmd = 'cd /d C:/Users/93710/Desktop/opensmile-2.3.0/opensmile-2.3.0/bin/Win32 && SMILExtract_Release -C C:/Users/93710/Desktop/opensmile-2.3.0/opensmile-2.3.0/config/IS13_ComParE_Voc.conf -I ' + this_path_input + ' -O ' + this_path_output
        # cmd = 'cd /d C:/Users/93710/Desktop/opensmile-2.3.0/opensmile-2.3.0/bin/Win32 && SMILExtract_Release -C C:/Users/93710/Desktop/opensmile-2.3.0/opensmile-2.3.0/config/IS13_ComParE.conf -I ' + this_path_input + ' -O ' + this_path_output
    os.system(cmd)