import PIL
from PIL import ImageGrab
from PIL import Image
import sys
import subprocess
import numpy
import time
import datetime

PATH = "G:\\AtomProjects\\dev\\pubg\\data\\inbound\\gameplay\\"
TIME = time.time()
game_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M')
print(PATH)
#automate screen grabs on system timer. ingest to data\gameplay
def set_up():
    mkgdir_command=['mkdir', PATH+"games\\"+game_time+'\\']
    subprocess.call(mkgdir_command)

    subdirs=['gameplay','toInv','toMap']
    for s in subdirs:
        command=['mkdir', PATH+"games\\"+game_time+'\\'+s]
        subprocess.call(command)

    return(1)

def get_data(p):
    return open(p, 'r')

def write_data(path, data):
    #implement writing screen to file at ?path?
    with open(path, 'w') as f:
        f.write(data)
        f.close()

def get_grab():
    img = ImageGrab.grab()
    return img

def save_grab(img, n, t):
    name = n #timestamp accurate to seconds
    st = datetime.datetime.fromtimestamp(n).strftime('%Y%m%dH%HM%MS%S')

    ty = t
    img.save(PATH+"games\\"+game_time+'\\'+st+'.'+ty, ty.upper())
    # Image(img).save(PATH+name,type)

def process():
    # takes image object as input, performs processes
    img = get_grab()
    save_grab(img,time.time(),'png')
    # img.show()

def timer(s):
    time.sleep(s)
    return True

def print_time():
    subprocess.call('clear')
    difftime = time.time() - TIME
    print(difftime)

def controller():
    set_up()
    while(True):
        print_time()
        t = timer(5)
        if(t):
            process()
# process()
controller()

# img = get_grab()
# print ("the size of the Image is: ")
# print(img.format, img.size, img.mode)
#
# write_data(PATH+'stamp.bmp', img)
#
#
