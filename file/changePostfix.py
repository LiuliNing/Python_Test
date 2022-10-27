import os
import shutil

root = "C:\\Users\\Administrator\\Desktop\\理正图例文件\\LiZhengPat--jpg"
for root, dirs, files in os.walk(root):
    for f in files:
        fn = os.path.join(root,f)
        nfn = fn.replace('.bmp','.jpg')
        if src in fn and fn != nfn:
            shutil.move(fn,nfn)

