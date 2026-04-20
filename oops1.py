class DemoClass:
    a=10
    def showvalue(self):
        print("Value of a is ",self.a)

    def showvalue1(self,a,b):
        print(a+b)    

odj=DemoClass()
odj.showvalue()

odj.showvalue1(10,20)
