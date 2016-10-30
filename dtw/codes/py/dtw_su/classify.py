import os
import operator
import random
from dtw_su import mfcc, dtw
import numpy as np
import datetime
import threading

def do_file(testFilePath):
  # Set the directory you want to start from
  fos = open('test.txt', 'w')
  database = {}
  rootDir = '../../data/processed'
  
  # *****************************
  # LOAD TEST FILE DATA
  # *****************************
  testFileData = mfcc.load_file(testFilePath)

  # ****************************************************
  # calculate dtw distance for all files and take the average
  # ****************************************************
  for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Found directory: %s' % dirName)
    cDirName = os.path.basename(os.path.normpath(dirName))
    database[cDirName] = []
    for fname in fileList:
      # basePath = cpath[:(-len(__file__)-1)]
      basePath = os.path.join(rootDir, cDirName)
      basePath = os.path.join(basePath, fname)
      
      # print basePath
      # fos.write(basePath + '\n')
      # print(dirName)

      # 
      # READ THE FILE AND CALCULATE THE DTW DISTANCE
      # SAVE THE DTW DISTANCE
      #
      # call dtw.from_file
      dtw_distance = dtw.from_file(testFileData, basePath)
      (database[cDirName]).append(dtw_distance)

    # take average of the total dtw distace from all cities
    database[cDirName] = np.mean(np.array(database[cDirName]))

  maxVal = min(database.iteritems(), key=operator.itemgetter(1))[0]
  fos.write(str(database))
  return {testFilePath:maxVal}
# end_do_file

def singleCityClassify(testCityFilePath, mem, testResult={}):
  database = {}
  # *****************************
  # LOAD TEST FILE DATA
  # *****************************
  testFileData = mfcc.load_file(testCityFilePath)
  # count = 1
  for dirName in mem:
    cityName_mfcc = os.path.basename(os.path.normpath(dirName))
    cityName_ = dirName[1:-len(cityName_mfcc)-1]
    cityName = os.path.basename(os.path.normpath(cityName_))

    if not cityName in database: # if empty
      # print(str(count) + ' -> ' +cityName + ' not in database')
      # count = count+1
      database[cityName] = []

    # calculate dtw.from_mem b/w testFileData and mem
    dtw_distance = dtw.from_mem(testFileData, mem[dirName])
    (database[cityName]).append(dtw_distance)

  for city in database:
    # take average of the total dtw distace from all cities
    database[city] = np.mean(np.array(database[city]))

  maxVal = max(database.iteritems(), key=operator.itemgetter(1))[0]

  cityName_mfcc = os.path.basename(os.path.normpath(testCityFilePath))
  cityName_ = dirName[1:-len(cityName_mfcc)-1]
  cityName = os.path.basename(os.path.normpath(cityName_))
  # return maxVal or 
  testResult[testCityFilePath] = maxVal

# end_singleCityClassify

def do_mem(testCityFilePaths):
  # Set the directory you want to start from
  # fos = open('test.txt', 'wa')
  rootDir = '../../data/processed/'
  mem = {}
  testResult = {}

  # ****************************************************
  # calculate dtw distance for all files and take the average
  # ****************************************************
  for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Found directory: %s' % dirName)
    cDirName = os.path.basename(os.path.normpath(dirName))
    for fname in fileList:
      filePath = os.path.join(rootDir, cDirName)
      filePath = os.path.join(filePath, fname)

      # 
      # READ THE FILES AND SAVE ON mem DICTIONARY
      #
      # mem[filePath] = mfcc.load_file(filePath)
      # mfcc.load_file_to(filePath, mem)
      t = threading.Thread(target=mfcc.load_file_to, args=(filePath, mem))
      t.start()
      t.join()

  # *************************************************
  # NOW REUSE mem TO DO CLASSIFICATION MULTIPLE TIMES
  # *************************************************
  for testCityFilePath in testCityFilePaths:
    # 
    # USE threading here for multiple classification parallesism
    # 
    # singleCityClassify(testCityFilePath, mem, testResult)
    t = threading.Thread(target=singleCityClassify, args=(testCityFilePath, mem, testResult))
    t.start()
    t.join()
    print datetime.datetime.now()

  # end for testFiles
  return testResult
