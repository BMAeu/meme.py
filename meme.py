#!/usr/env/python

import sys
import os
import time
import random

path = sys.argv[1]

fileList = os.listdir(path)

for f in fileList:  
    name, extension = os.path.splitext(path + f)
    file_creation = time.gmtime(os.path.getctime(path + f))

    try:
        os.rename(path + f, path + "meme_" + time.strftime('%Y-%m-%d', file_creation) + "{}".format(extension) )
    except:
        os.rename(path + f, path + "meme_" + time.strftime('%Y-%m-%d', file_creation)+ "({})".format(round(random.random(), 5)) + "{}".format(extension) )
