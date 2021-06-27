#read data from multiple mice, connected to Linux computer

from threading import Thread
import os.path

thread0 = None
thread1 = None
thread2 = None
thread3 = None

def run():
    global thread0, thread1, thread2, thread3
    if thread0 is None:
        thread0 = run_one('/dev/input/mouse0', "m0")
    if thread1 is None:
        thread1 = run_one('/dev/input/mouse1', "m1")
    if thread2 is None:
        thread2 = run_one('/dev/input/mouse2', "m2")
    if thread3 is None:
        thread3 = run_one('/dev/input/mouse3', "m3")

def run_one(path, name):
    if os.path.exists(path):
        print('exists %s' % name)
        thread = Thread(target = read_mouse, args = (path, name))
        thread.start()
        return thread
    

def read_mouse(path, name):
    print(path, name)
    mouse_file = open(path, 'rb')
    while True:
        try:
            status, dx, dy = tuple(c for c in (mouse_file.read(3)))
            #next line consumes a lot of CPU, because it prints number of events
            print("%s: %#02x %d %d" % (name, status, dx, dy))
        except:
            print("turned off %s" % name)
            return


if __name__ == '__main__':
    Thread(target = run).start()
    try:
        a = input('')
    except:
        print("stop")
        exit

