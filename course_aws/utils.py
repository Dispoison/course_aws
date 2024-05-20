"""
Script to generate a specific amount of load for a specific amount of time.
We will check the number of CPU cores and using multiprocessing run the generate load function on all the cores in parallel
To generate a load, we will perform an arithmetic operation for a fraction of a second and then sleep for the rest
So if you want 20% utilization, the script would run the arithmetic operation for 0.2 seconds and then sleep for 0.8 seconds.
"""
import multiprocessing
import time
import math


def generate_cpu_load(interval, utilization):
    """Generate a utilization % for a duration of interval seconds"""
    start_time = time.time()
    for i in range(0, int(interval)):
        print("About to do some arithmetic")
        while time.time() - start_time < utilization / 100.0:
            a = math.sqrt(64 * 64 * 64 * 64 * 64)
        print(str(i) + ". About to sleep")
        time.sleep(1 - utilization / 100.0)
        start_time += 1


def load_cpu(interval=30, utilization=75):
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=generate_cpu_load, kwargs={"interval": interval, "utilization": utilization})
        p.start()
        processes.append(p)
    for process in processes:
        process.join()