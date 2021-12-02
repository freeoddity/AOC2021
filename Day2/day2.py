import re
downSum = 0
upSum = 0
forwardSum = 0
file = open('Day2Input.txt', 'r')
#file_content = file.readline()
subMap = {"forward":[], "up":[], "down":[]}
#print(file_content)
#x = re.findall(r'\d+', file_content)
#print(x[0])

for line in file:
    if 'forward' in line:
        x = re.findall(r'\d+', line)
        subMap['forward'].append(x[0])
    elif 'up' in line:
        x = re.findall(r'\d+', line)
        subMap['up'].append(x[0])
    else:
        x = re.findall(r'\d+', line)
        subMap['down'].append(x[0])
for i in subMap:
    if i == 'forward':
        for element in subMap[i]:
            forwardSum+= int(element)
    elif i =='up':
        for element in subMap[i]:
            upSum+=int(element)
    else:
        for element in subMap[i]:
            downSum+=int(element)
print(forwardSum)
print(upSum)
print(downSum)

vertSum = downSum-upSum

print(forwardSum * vertSum)
