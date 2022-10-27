import os

dir = "C:\\Users\\Administrator\Desktop\\理正图例文件\\岩土案例处理后jpg"
for root, dirs, files in os.walk(dir):
    for fileName in files:
        print(fileName)
        portion = os.path.split(fileName)
        if portion[1] == ".bmp":
            newName = portion[0]+".jpg"
            os.rename(fileName,newName)