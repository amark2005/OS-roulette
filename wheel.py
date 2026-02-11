import random as rand
import time
class Wheel:
    data=[]
    l3=list()
    roundy=3
    finale=str()
    def getdata(self):
        while True:
            x=input("Enter choice (blank to stop):")
            if not x:
                break
            self.data.append(x)
        pass
    def levelx(self):
        self.l3.clear()
        for i in range(rand.randint(6,10)):
            a=rand.choice(self.data)
            if not self.data == 2:
                print(a)
            time.sleep(0.3)
            self.l3.append(a)
        self.l3_result=max(set(self.l3),key=self.l3.count)
        l3_lose=min(set(self.l3),key=self.l3.count)
        if not self.data == 1:
            print(f"The maximum count: {self.l3_result}")
            print(f"The minimum count: {l3_lose}")
            print(f"{l3_lose} Removed")
            print(f"Round {self.roundy} Winner is {self.l3_result}")
        if l3_lose in self.data:
            self.data.remove(l3_lose)
        #print(self.data)
        if len(self.data) == 1:
            self.finale=self.data
        pass
    
    def finale_round(self):
            return self.data[0]
