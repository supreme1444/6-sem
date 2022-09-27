b = '6+6/3'
lst = re.split(r'((?:[+-]?\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)',b)
d3 = list(filter(None, lst))
print(d3)
summa = 0
for i in d3:
    if '*' in d3:
        index = d3.index('*')
        left = d3[index - 1]
        right = d3[index + 1]
        result = int(left) * int(right)
        del d3[index]
        del d3[index]
        d3[index - 1] = str(result)

    elif '/' in d3:
        index = d3.index('/')
        left = d3[index - 1]
        right = d3[index + 1]
        result = int(left) / int(right)
        del d3[index]
        del d3[index]
        d3[index - 1] = str(result)
print (d3)
for j in d3:
    summa += float(j)

print(summa)
