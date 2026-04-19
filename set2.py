s={10,20,30,40,50}
print(s)

for i in s:
    print(i)
l=[10,20,30,40,50]
s1=set(l)
print(s1)
s.remove(30)
print(s)
s.discard(40)
print(s)   

s.clear()
print(s)
