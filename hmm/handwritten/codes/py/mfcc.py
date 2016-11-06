import feature
import os
import json

def from_file_to_mfcc(filePath, dir, base):
  jsonFile = "./../../data/processed/paths/" + base + ".json"
  jsonData = []
  f = open(filePath)
  line = f.readline()
  line = f.readline()
  count = 0
  while(line):
    line = f.readline() # get the x, y line
    data = feature.extend(line)

    dataToWrite = ""
    for d1 in data:
      for d2 in d1:
        dataToWrite += str(d2) + " "
      dataToWrite += "\n"

    if not os.path.exists(dir+base):
      os.makedirs(dir+base)

    filePath = dir+base+"/"+str(count)+".mfcc"
    jsonData.append(filePath)

    fo = open(filePath, "w")
    fo.write(dataToWrite)
    fo.close()

    # dir/count++ -> write a new file
    line = f.readline()
    line = f.readline()
    count += 1
  f.close()
  if not os.path.exists(jsonFile):
      os.makedirs(jsonFile)
  fjo = open(jsonFile, "w")
  fjo.write(json.dumps(jsonData))
  fjo.close()
