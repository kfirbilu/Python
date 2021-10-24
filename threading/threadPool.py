import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} seconds")
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)
#     print(f1.result())
#     print(f2.result())

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = [executor.submit(do_something, sec) for sec in secs]  # list comprehension instead of for-loop
#
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

with concurrent.futures.ThreadPoolExecutor() as executor:  # instead of list comprehension
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished running in {round(finish - start, 2)} seconds")
