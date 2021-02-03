def follow(lines):
    from random import random
    for data in lines:
        if random() < 0.5:
            yield data
        
def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line
        
filedata = ['abc','xyz','abd','bcd','axy']*5

lines = follow(filedata)
mint = filematch(lines, 'a')
for line in mint:
    print(line)
