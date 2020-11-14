import os
import os.path
from PIL import Image
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''
def ResizeImage(filein, fileout, width, height, type):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS) #resize image with high-quality
  out.save(fileout, type)
# if __name__ == "__main__":
#   file_path ='C:\\Users\\93710\\Desktop\\11'
#   for i in os.listdir(file_path):
#       path = "C:\\Users\\93710\\Desktop\\111"
#       filein =file_path + "\\"+i
#       name = i.split('.')
#       name1 = name[0]
#       fileout = path+"\\"+name1+'.jpg'
#       width = 224
#       height = 224
#       type = 'png'
#       ResizeImage(filein, fileout, width, height, type)
if __name__ == "__main__":
  mel_path = 'C:\\Users\\93710\\Desktop\\MOUD_mel'
  output_path = 'C:\\Users\\93710\\Desktop\\MOUD_mel224'
  file_path = 'C:\\Users\\93710\\Desktop\\Audio\\cats.txt'
  label = open(file_path, 'rb')
  label_ = label.readlines()
  for i in range(len(label_)):
      line_ = label_[i]
      line_ = str(line_)
      label_s = line_.split('\\t')[1]
      name_s = line_.split('\\t')[0]
      filein = mel_path + '\\' + name_s[2:] + '.jpg'
      fileout = output_path+'\\'+ name_s[2:] + '.jpg'
      width = 224
      height = 224
      type = 'png'
      ResizeImage(filein, fileout, width, height, type)