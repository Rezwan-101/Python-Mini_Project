import time

count_for_time = int(input("Enter the time in second(S): "))

for x in reversed(range(1, count_for_time)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x/3600) % 24 

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is Up!")
