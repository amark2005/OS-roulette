import random as rand
class wheel:
    data=list()
    l3=list()
    l3_result=None
    finale=list()
    l2=list()
    l2_result=None
    def getdata(self):
        while True:
            x=input("Enter the datas: ")
            if not x:
                break
            self.data.append(x)
        pass
    def level3(self):
        for i in range(0,rand.randint(30,50)):
            a=rand.choice(self.data)
            print(a)
            self.l3.append(a)
        self.l3_result=max(set(self.l3),key=self.l3.count)
        print(f"The maximum count: {self.l3_result}")
        l3_lose=min(set(self.l3),key=self.l3.count)
        print(f"The minimum count: {l3_lose}")
        print(f"{l3_lose} Removed")
        self.finale.append(self.l3_result)
        self.data.remove(l3_lose)
        print(f"Level 3 Winner is {self.l3_result}")
        print(self.data)
        pass
    def level2(self):
        for i in range(0,rand.randint(7,15)):
            self.l2.append(rand.choice(self.data))
        self.l2_result=max(set(self.l2),key=self.l2.count)
        l2_lose=min(set(self.l2),key=self.l2.count)
        self.data.remove(l2_lose)
        self.finale.append(self.l2_result)
        print(f"Level 2 Winner is {self.l2_result}")
        pass
    
    def finale_round(self):
        fin=rand.choice(self.finale)
        return fin
    
        
        
        

wheel()