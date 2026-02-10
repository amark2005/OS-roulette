import random as rand
class Wheel:
    players=3
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
        for i in range(self.players):
            a=rand.choice(self.data)
            print(a)
            self.l3.append(a)
        self.l3_result=max(set(self.l3),key=self.l3.count)
        print(f"The maximum count: {self.l3_result}")
        l3_lose=min(set(self.l3),key=self.l3.count)
        print(f"The minimum count: {l3_lose}")
        print(f"{l3_lose} Removed")
        if l3_lose in self.data:
            self.data.remove(l3_lose)
        print(f"Round {self.roundy} Winner is {self.l3_result}")
        print(self.data)
        if len(self.data) == 1:
            self.finale=self.data
        pass
    
    def finale_round(self):
            return self.data[0]
