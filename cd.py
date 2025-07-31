import time

seconds = 5  # countdown from 5 seconds

while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1

print("Time's up!")
