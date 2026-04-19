d={
    "course": "Python",
    "fees": 5000,
    "duration": "2 months"
}
c=d.get("course")
print(c)
print("***************")
for i in d.keys():
    print(i)
print("***************")
for i in d.values():
    print(i)   
print("***************")
for i in d.items():
    print(i)
print("***************")
for i,j in d.items():
    print(i,j)
print("***************")
del d["fees"] 
print(d) 
print("***************")
d.pop("duration") 
print(d) 
print("***************")
d.update({"duration":"3 months"})
print(d)