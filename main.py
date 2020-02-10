import img2pdf
import os

# uri = input('输入图片路径：')
path = 'D:\wqxtDownload\9699'
# for name in os.listdir(path):
#     file = path + '\\' + name
#     print(file)
#
#
# with open('output.pdf', 'wb') as f:
#     file_list = os.listdir(path)
#     png_list = []

def file_rename(path):
    for name in os.listdir(path):

        print(name)
        # file = path + '\\' + name


file_rename(path)