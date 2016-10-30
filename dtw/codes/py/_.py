from numpy import array, zeros, argmin, inf
from numpy.linalg import norm
from dtw import dtw
import numpy as np
import os
import operator
import random

def find_max(database):
  maxVal = max(database.iteritems(), key=operator.itemgetter(1))[0]
  for city in database:
    if(city == maxVal):
      print('---####### ' + city + ' -> ' + str(database[city]) + ' #######')
    else:
      print('---' + city + ' -> ' + str(database[city]))
  print(maxVal)
 
# Set the directory you want to start from
rootDir = './../../data/processed'

# calculate dtw distance for all files and do average
database = {}
for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Found directory: %s' % dirName)
    dirName = os.path.basename(os.path.normpath(dirName))
    database[dirName] = []
    for fname in fileList:
      # print('\t%s' % fname)

      # 
      # READ THE FILE AND CALCULATE THE DTW DISTANCE
      # SAVE THE DTW DISTANCE
      #

      # call dtw
      (database[dirName]).append(random.randint(0, 100))


    # take average of the total dtw distace from all cities
    database[dirName] = np.mean(np.array(database[dirName]))

find_max(database)





