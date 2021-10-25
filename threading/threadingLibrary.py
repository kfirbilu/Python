# Threading using "threading" library - less efficient, a lot of code

import threading
import time

start = time.perf_counter()

secs = [5,4,3,2,1]

threads = []

def do_something(seconds):
    print(f"Sleeping {seconds} seconds")
    time.sleep(seconds)
    print("Done sleeping")


for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    threads.append(t)
    t.start()

for t in threads:
    t.join()

finish = time.perf_counter()

print(f"Finished running in {round(finish-start,2)} seconds")