#read data from multiple mice, connected to Linux computer

from threading import Thread
import os.path

thread0 = None
thread1 = None
thread2 = None
thread3 = None

def run():
    global thread0, thread1, thread2, thread3
    if thread0 is None and os.path.exists('/dev/input/mouse0'):
        print('exists 0')
        thread0 = Thread(target = mouse, args = ('/dev/input/mouse0', "m0"))
        thread0.start()
    if thread1 is None and os.path.exists('/dev/input/mouse1'):
        print('exists 1')
        thread1 = Thread(target = mouse, args = ('/dev/input/mouse1', "m1"))
        thread1.start()
    if thread2 is None and os.path.exists('/dev/input/mouse2'):
        print('exists 2')
        thread2 = Thread(target = mouse, args = ('/dev/input/mouse2', "m2"))
        thread2.start()
    if thread3 is None and os.path.exists('/dev/input/mouse3'):
        print('exists 3')
        thread3 = Thread(target = mouse, args = ('/dev/input/mouse3', "m3"))
        thread3.start()
    print("threads finished...exiting")

def mouse(path, name):
    print(path, name)
    mouse = open(path, 'rb')
    while True:
        try:
            status, dx, dy = tuple(c for c in (mouse.read(3)))
            print("%s: %#02x %d %d" % (name, status, dx, dy))
        except:
            print("turned off %s", name)
            return


if __name__ == '__main__':
    Thread(target = run).start()
    a = input('ok')

