b = '6+6/3'
d2 = re.split(r'((?:[+-]?\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)',b)
d3 = list(filter(None, d2))
print(d3)
summa = int('0')
for i in d3:
    if '*' in d3:
        superindex = d3.index('*')
        left = d3[(superindex - 1)]
        right = d3[(superindex + 1)]
        result = int(left) * int(right)
        del d3[superindex]
        del d3[superindex]
        d3[(superindex - 1)] = str(result)

    elif '/' in d3:
        superindex = d3.index('/')
        left = d3[(superindex - 1)]
        right = d3[(superindex + 1)]
        result = int(left) / int(right)
        del d3[superindex]
        del d3[superindex]
        d3[(superindex - 1)] = str(result)
print (d3)
for j in d3:
    summa += float(j)

print('summarizer',summa)

