#read data from multiple mice, connected to Linux computer

from threading import Thread
import os.path

def run():
    thread0 = None
    thread1 = None
    thread2 = None
    if os.path.exists('/dev/input/mouse0'):
        print('exists 0')
        thread0 = Thread(target = mouse, args = ('/dev/input/mouse0', "m0"))
        thread0.start()
    if os.path.exists('/dev/input/mouse1'):
        print('exists 1')
        thread0 = Thread(target = mouse, args = ('/dev/input/mouse1', "m1"))
        thread0.start()
    if os.path.exists('/dev/input/mouse2'):
        print('exists 2')
        thread2 = Thread(target = mouse, args = ('/dev/input/mouse2', "m2"))
        thread2.start()
    if thread0 is not None:
        thread0.join()
    if thread1 is not None:
        thread1.join()
    if thread2 is not None:
        thread2.join()
    print("threads finished...exiting")

def mouse(path, name):
    print(path, name)
    mouse = open(path, 'rb')
    while True:
        status, dx, dy = tuple(c for c in (mouse.read(3)))
        print("%s: %#02x %d %d" % (name, status, dx, dy))


if __name__ == '__main__':
    run()

