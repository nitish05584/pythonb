class A:
    def displayA(self):
        print("In A")
class B(A):
    def displayB(self):
        print("In B")        

obj = B()
obj.displayA()
obj.displayB()