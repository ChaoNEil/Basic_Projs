import time 

my_time = int(input("Enter the time in secs: "))

for i in range(my_time,0,-1):
    seconds = i % 60
    mins = i // 60
    hours = i // 3600 #there are 3600 seconds in a hour
    print(f"{hours:02}:{mins:02}:{seconds:02}")
    time.sleep(1)

print("Time's Up.")