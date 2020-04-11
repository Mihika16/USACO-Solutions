"""
ID: scarletcoder
LANG: PYTHON3
PROB: teleport

"""

#inputs
f = open("teleport.in", "r")

ans = open("teleport.out", "w")

data = (fin.read()).split('/n')
a = data[0]
b = data[1]
x = data[2]
y = data[3]

a = int(a)
b = int(b)
x = int(x)
y = int(y)


first = abs(a-b)
second = abs(a-x)+abs(b-y)
third = abs(b-x)+abs(a-y)

totallist = []
totallist.append(first)
totallist.append(second)
totallist.append(third)

s = min(totallist)
ans.write(s)

f.close()
ans.close()


