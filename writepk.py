import pickle

l=[10,20,30,40,50]
file=open("writedata.text","wb")
pickle.dump(l,file)
file.close()

file=open("writedata.text","rb")
data=pickle.load(file)
print(data)
file.close()