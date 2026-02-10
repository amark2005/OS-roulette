from wheel import wheel
import time

a=wheel()
print("****Picker Wheel****")
a.getdata()
print(f"{len(a.data)} Datas entered")
print(f"{a.data}")
input("press Enter to run Round 3")
print("Starting Round 3")
time.sleep(0.5)
a.level3()
input("Press enter to run Round 2")
print("Starting Round 2")
time.sleep(0.5)
a.level2()
print()
print(f"Now we have {len(a.data)} choices left")
print(a.finale)
input("Press enter to run finale round")
for i in range(2):
    print("Calculating....")
    time.sleep(1.5)
print(f"The Winner is {a.finale_round()}")

