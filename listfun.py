l=[10,20,30,40,50,60,70,80,90,100]

del l[1]
print(l)

print(l.pop(3))
l.remove(70)
print(l)
# l.clear()
# print(l)

l[2]=300
print(l)

l.insert(2,200)
print(l)

l.append(110)
print(l)

l.extend([120,130,140])
print(l)

l.pop(3)
print(l)

l.sort()
print(l)