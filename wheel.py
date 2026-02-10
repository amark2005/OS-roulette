import random as rand
class wheel:
    data=[1,2,3,4]
    l3=list()
    l3_result=None
    finale=list()
    def __init__(self):
        #self.getdata()
        self.level3()
        pass
    def getdata(self):
        while True:
            a=1
            x=input("Enter the datas: ")
            if a == 1:
                self.data.append(x)
            elif x == None:
                a=0
                pass
    def getdata(self):
        while True:
            x=input("Enter the datas: ")
            if not x:
                break
            self.data.append(x)
        pass
    def level3(self):
        for i in range(0,rand.randint(30,50)):
            self.l3.append(rand.choice(self.data))
        print(self.l3)
        self.l3_result=max(set(self.l3),key=self.l3.count)
        self.l3_lose=min(set(self.l3),key=self.l3.count)
        self.finale.append(self.l3_result)
        self.
        print(f"Level 3 Winner is {self.l3_result}")
        
        
        

wheel()