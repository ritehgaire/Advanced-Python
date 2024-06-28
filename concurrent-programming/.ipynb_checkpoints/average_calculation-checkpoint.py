import time
import threading
import asyncio
from multiprocessing import Process, Queue

def cal_average(num):
    """Calculate average of a list and simulate a delay."""
    try:
        sum_num = sum(num)
        avg = sum_num / len(num)
        time.sleep(1)  # Simulate a delay to mimic a time-consuming task
        return avg
    except Exception as e:
        print(f"Error calculating average: {e}")

def main_sequential(list1, list2, list3):
    """Sequential calculation of averages."""
    s = time.perf_counter()  # Start timer
    avg1 = cal_average(list1)
    avg2 = cal_average(list2)
    avg3 = cal_average(list3)
    elapsed = time.perf_counter() - s  # Calculate elapsed time
    print(f"Sequential Averages: {avg1}, {avg2}, {avg3}")
    print(f"Sequential Programming Elapsed Time: {elapsed:.2f} seconds")

async def cal_average_async(num):
    """Asynchronously calculate average of a list."""
    try:
        sum_num = sum(num)
        avg = sum_num / len(num)
        await asyncio.sleep(1)  # Simulate a non-blocking delay
        return avg
    except Exception as e:
        print(f"Error calculating average: {e}")

async def main_async(list1, list2, list3):
    """Asynchronous calculation of averages."""
    s = time.perf_counter()  # Start timer
    tasks = [
        cal_average_async(list1),
        cal_average_async(list2),
        cal_average_async(list3)
    ]
    results = await asyncio.gather(*tasks)  # Run tasks concurrently and wait for completion
    elapsed = time.perf_counter() - s  # Calculate elapsed time
    print(f"Asynchronous Averages: {results}")
    print(f"Asynchronous Programming Elapsed Time: {elapsed:.2f} seconds")

def main_threading(list1, list2, list3):
    """Threaded calculation of averages."""
    s = time.perf_counter()  # Start timer
    lists = [list1, list2, list3]
    threads = []
    results = []

    def thread_target(num):
        results.append(cal_average(num))

    for lst in lists:
        thread = threading.Thread(target=thread_target, args=(lst,))
        threads.append(thread)  # Create and start a thread for each list
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to finish

    elapsed = time.perf_counter() - s  # Calculate elapsed time
    print(f"Threading Averages: {results}")
    print(f"Threading Elapsed Time: {elapsed:.2f} seconds")

def cal_average_process(num, q):
    """Calculate average in a separate process and put result in queue."""
    avg = cal_average(num)
    q.put(avg)  # Put result in queue to retrieve later

def main_multiprocessing(list1, list2, list3):
    """Multiprocessing calculation of averages."""
    s = time.perf_counter()  # Start timer
    lists = [list1, list2, list3]
    processes = []
    q = Queue()

    for lst in lists:
        p = Process(target=cal_average_process, args=(lst, q))
        processes.append(p)  # Create and start a process for each list
        p.start()

    results = [q.get() for _ in processes]  # Collect results from queue

    for p in processes:
        p.join()  # Wait for all processes to finish

    elapsed = time.perf_counter() - s  # Calculate elapsed time
    print(f"Multiprocessing Averages: {results}")
    print(f"Multiprocessing Elapsed Time: {elapsed:.2f} seconds")

if __name__ == '__main__':
    # Lists of numbers to calculate averages
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l2 = [2, 4, 6, 8, 10]
    l3 = [1, 3, 5, 7, 9, 11]
    
    # Run sequential example
    main_sequential(l1, l2, l3)
    
    # Run asynchronous example
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_async(l1, l2, l3))
    
    # Run threading example
    main_threading(l1, l2, l3)
    
    # Run multiprocessing example
    main_multiprocessing(l1, l2, l3)
