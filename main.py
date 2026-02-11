from wheel import Wheel
import time
a=Wheel()
print("****Picker Wheel****")
a.getdata()
print(f"{len(a.data)} Datas entered")
print(f"{a.data}")
a.roundy=len(a.data)-1
while True:
        
    input("press Enter to Spin the Wheel")
    print("Spinning....")
    time.sleep(0.5)
    a.levelx()
    for i in a.data:
        print(f"The Winner is {i}")    
        a.roundy-=1
    else:
        break
a.roundy=None
#input("Press enter to see who won...")
#for i in range(2):
    #print("Calculating....")
    #time.sleep(0.5)
#print(f"The Winner is {a.finale_round()}")


