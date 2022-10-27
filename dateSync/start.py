import os

if __name__ == '__main__':
    f = os.popen("ls -l")
    print(f.read())