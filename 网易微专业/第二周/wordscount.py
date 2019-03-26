import jieba
f=open('E:\x.txt','rt')
txt=f.read()
ls=jieba.lcut(txt)
d={}
