import re
inputPath = 'Day2Input.txt'
def popMap(pathToFile):
    inputFile = open(str(pathToFile), 'r')
    toReturn = {'forward':[], 'up':[], 'down':[]}
    for line in inputFile:
        if 'forward' in line:
            x = re.findall(r'\d+', line)
            toReturn['forward'].append(x[0])
        elif 'up' in line:
            x = re.findall(r'\d+',line)
            toReturn['up'].append(x[0])
        else:
            x = re.findall(r'\d+', line)
            toReturn['down'].append(x[0])
    return toReturn
def taskOne(map):
    downSum = 0
    upSum =0
    forwardSum =0
    for i in map:
        if i == 'forward':
            for element in map[i]:
                forwardSum+=int(element)
        elif i == 'up':
            for element in map[i]:
                upSum+=int(element)
        else:
            for element in map[i]:
                downSum+=int(element)
    vertSum = downSum-upSum
    return (forwardSum*vertSum)
def taskTwo(pathToFile):
    inputFile = open(str(pathToFile), 'r')
    forwardSum = 0
    aim = 0
    subdepth = 0
    for line in inputFile:
        if 'forward' in line:
            x = re.findall(r'\d+', line)
            forwardSum += int(x[0])
            if(aim != 0):
                subdepth += int(x[0]) * aim
        elif 'up' in line:
            x = re.findall(r'\d+',line)
            aim-=int(x[0])
        else:
            x = re.findall(r'\d+', line)
            aim+=int(x[0])
    return (forwardSum*subdepth)     


subMap = popMap(inputPath)
print(taskOne(subMap))
print(taskTwo(inputPath))
