import time 

my_time = int(input("Enter the time in secs: "))

for i in range(my_time,0,-1):
    seconds = i % 60
    print(f"00:00:{seconds}")
    time.sleep(1)

print("Time's Up.")