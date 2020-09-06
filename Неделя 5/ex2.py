import time
import os


if __name__=="__main__":
    pid = os.fork()
    if pid == 0:
        #дочерний процесс
        while True:
            print("child:", os.getpid())
            time.sleep(5)
        else:
            #родительский процесс
            print("parent:", os.getpid())
            os.wait()
