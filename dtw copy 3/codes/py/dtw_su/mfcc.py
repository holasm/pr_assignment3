def load_file(filePath):
  ret = []
  f = open(filePath)
  f.readline() # skip first line | ex: 38 400
  fw = open('test.txt', 'w')
  line = f.readline()
  while(line):
    arr = line.strip().split(' ')
    push_array = [float(num_str) for num_str in arr]
    ret.append(push_array)
    line = f.readline()
  return ret

def load_file_to(filePath, mem):
  ret = []
  f = open(filePath)
  f.readline() # skip first line | ex: 38 400
  fw = open('test.txt', 'w')
  line = f.readline()
  while(line):
    arr = line.strip().split(' ')
    push_array = [float(num_str) for num_str in arr]
    ret.append(push_array)
    line = f.readline()
  mem[filePath] = ret
