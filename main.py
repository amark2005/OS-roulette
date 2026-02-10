from wheel import Wheel
import time

a=Wheel()
print("****Picker Wheel****")
a.getdata()
print(f"{len(a.data)} Datas entered")
print(f"{a.data}")
a.roundy=len(a.data)+4
while True:
    input("press Enter to Spin the Wheel")
    print("Spinning....")
    time.sleep(0.5)
    a.levelx()
    print(f"Now we have {len(a.data)} choices left")
    print(a.data)
    a.roundy-=1
    if len(a.data) == 1:
        break
print()
input("Press enter to see who won...")
for i in range(2):
    print("Calculating....")
    time.sleep(0.5)
print(f"The Winner is {a.finale_round()}")


