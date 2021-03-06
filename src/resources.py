
##Import heappush
from heapq import heappush, heappop
import operator

def getTop10Resources(filename): ##define filename
  heap = []
  hashSet = {}
  with open(filename,'r') as f: ### runs when 
    for line in f: ###Initiate a for loop
      splitLine = line.split() ###split lines to ensure consistency
      totalBytes = splitLine[-1]
      resource = splitLine[6]
      if len(resource) <= 1: ### initiate if else to check if the resource is less than or equal to 1
        continue
      else:
        if resource not in hashSet:
          hashSet[resource] = 1
        else:
          hashSet[resource] += 1
      # if totalBytes == "-":
      #   totalBytes = 0
      # else:
      #   totalBytes = int(totalBytes)
      # heappush(heap, (-totalBytes, resource))
  sorted_x = sorted(hashSet.items(), key=operator.itemgetter(1))
  sorted_x = sorted_x[::-1]
  keys = [x[0] for x in sorted_x[:10]] 
  # for x in sorted_x:
  #   print hashSet[x]
  return keys

def writeFile(tuplesOfHostFreq, filename):
  fileHandler = open(filename, 'w')
  for item in tuplesOfHostFreq:
    # print item
    fileHandler.write(item+'\n')
  fileHandler.close()

if __name__ == "__main__":  ###write the output to file
  topIPAddress = getTop10Resources("log.txt")
  writeFile(topIPAddress, "resources.txt")
