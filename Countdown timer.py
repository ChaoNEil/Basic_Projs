import time 

my_time = int(input("Enter the time in secs: "))

for i in range(0, my_time):
    print(i)
    time.sleep(1)

print("Time's Up")