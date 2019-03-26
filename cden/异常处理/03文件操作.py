import os
import shutil

# -----操作文件和目录
print(os.path.exists('itany.txt'))  # 判断是否存在
print(os.path.abspath('itany.txt'))  # 获取文件的绝对路径
print(os.path.isfile('itany.txt'))  # 判断是否是文件
print(os.path.isdir('itany.txt'))  # 判断是否为目录
print(os.listdir('.'))

dirs = [f for f in os.listdir('.') if os.path.isdir(f)]
print(dirs)


#创建/删除目录
# os.mkdir('word')
if os.path.exists('word'):
    os.rmdir('word')

#重命名文件或目录
# os.rename('itany.txt','aaa.txt')
# os.remove('aaa.txt')

#拷贝文件
shutil.copy('x.png','bbb.png')