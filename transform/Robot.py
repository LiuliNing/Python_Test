import time

import win32api


if  __name__ == '__main__':
    time.sleep(3)
    win32api.keybd_event(13, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(13, 0, 0, 0)

