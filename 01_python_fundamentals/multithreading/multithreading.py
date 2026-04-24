"""
===========================================================
COMPLETE MULTITHREADING MASTER FILE (PRODUCTION STYLE)
===========================================================

Covers:
- Basic thread creation
- Passing arguments
- Multiple threads
- Thread lifecycle concepts
- Locks & race conditions
- RLock, Semaphore, Event
- Deadlocks
- ThreadPoolExecutor
- as_completed, map
- Queue (Producer-Consumer)
- Daemon threads
- Thread-local storage
- Timeouts & retries
- Performance benchmarking
- Real-world API ingestion
- Log processing pipeline
===========================================================
"""

import threading
import time
import logging
import requests
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, RLock, Semaphore, Event, local

# ===========================================================
# LOGGER SETUP
# ===========================================================

logging.basicConfig(level=logging.INFO, format="%(threadName)s: %(message)s")

# ===========================================================
# 1. BASIC THREAD CREATION
# ===========================================================

def basic_task():
    print("Basic thread running")

def run_basic_thread():
    t = threading.Thread(target=basic_task)
    t.start()
    t.join()

# ===========================================================
# 2. PASSING ARGUMENTS
# ===========================================================

def process_file(file_name):
    print(f"Processing file: {file_name}")

def run_thread_with_args():
    t = threading.Thread(target=process_file, args=("log.txt",))
    t.start()
    t.join()

# ===========================================================
# 3. MULTIPLE THREADS
# ===========================================================

def run_multiple_threads():
    threads = []
    for i in range(5):
        t = threading.Thread(target=basic_task)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

# ===========================================================
# 4. RACE CONDITION (UNSAFE)
# ===========================================================

counter = 0

def unsafe_increment():
    global counter
    for _ in range(100000):
        counter += 1  # NOT SAFE

# ===========================================================
# 5. LOCK (THREAD-SAFE)
# ===========================================================

lock = Lock()

def safe_increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

# ===========================================================
# 6. RLOCK (RECURSIVE LOCK)
# ===========================================================

rlock = RLock()

def recursive_function(n):
    with rlock:
        if n > 0:
            recursive_function(n - 1)

# ===========================================================
# 7. SEMAPHORE (LIMIT CONCURRENCY)
# ===========================================================

semaphore = Semaphore(2)

def limited_resource():
    with semaphore:
        print("Accessing limited resource")
        time.sleep(1)

# ===========================================================
# 8. EVENT (THREAD COMMUNICATION)
# ===========================================================

event = Event()

def waiter():
    print("Waiting for event...")
    event.wait()
    print("Event received!")

def setter():
    time.sleep(2)
    print("Setting event")
    event.set()

# ===========================================================
# 9. DEADLOCK EXAMPLE (DON’T RUN IN PROD)
# ===========================================================

lock1 = Lock()
lock2 = Lock()

def deadlock_task1():
    with lock1:
        time.sleep(1)
        with lock2:
            print("Task1 done")

def deadlock_task2():
    with lock2:
        time.sleep(1)
        with lock1:
            print("Task2 done")

# ===========================================================
# 10. THREAD POOL EXECUTOR
# ===========================================================

def fetch_data(id):
    time.sleep(1)
    return f"Data {id}"

def thread_pool_map():
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_data, range(10)))
    print(results)

# ===========================================================
# 11. AS_COMPLETED (ADVANCED)
# ===========================================================

def thread_pool_as_completed():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_data, i) for i in range(10)]

        for future in as_completed(futures):
            print(future.result())

# ===========================================================
# 12. QUEUE (PRODUCER-CONSUMER)
# ===========================================================

queue = Queue()

def producer():
    for i in range(10):
        queue.put(i)
        print(f"Produced {i}")
    queue.put(None)

def consumer():
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed {item}")
        queue.task_done()

# ===========================================================
# 13. DAEMON THREAD
# ===========================================================

def daemon_task():
    while True:
        print("Daemon running...")
        time.sleep(1)

def run_daemon():
    t = threading.Thread(target=daemon_task, daemon=True)
    t.start()
    time.sleep(3)

# ===========================================================
# 14. THREAD LOCAL STORAGE
# ===========================================================

thread_local = local()

def thread_local_example():
    thread_local.data = threading.current_thread().name
    print(f"Thread-specific data: {thread_local.data}")

# ===========================================================
# 15. TIMEOUT HANDLING
# ===========================================================

def timeout_example():
    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(fetch_data, 1)

        try:
            result = future.result(timeout=2)
            print(result)
        except Exception as e:
            print("Timeout or error:", e)

# ===========================================================
# 16. PERFORMANCE MEASUREMENT
# ===========================================================

def benchmark():
    start = time.time()
    run_multiple_threads()
    print("Execution Time:", time.time() - start)

# ===========================================================
# 17. PRODUCTION: API DATA INGESTION
# ===========================================================

API_URL = "https://jsonplaceholder.typicode.com/posts/{}"

def fetch_post(post_id):
    try:
        response = requests.get(API_URL.format(post_id), timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Error fetching {post_id}: {e}")
        return None

def fetch_all_posts(post_ids):
    results = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_post, pid) for pid in post_ids]

        for future in as_completed(futures):
            data = future.result()
            if data:
                results.append(data)

    return results

# ===========================================================
# 18. PRODUCTION: LOG PROCESSING SYSTEM
# ===========================================================

error_count = 0

def process_log(file):
    global error_count
    try:
        with open(file, "r") as f:
            for line in f:
                if "ERROR" in line:
                    with lock:
                        error_count += 1
    except FileNotFoundError:
        logging.error(f"{file} not found")

def process_logs(files):
    threads = []

    for file in files:
        t = threading.Thread(target=process_log, args=(file,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Total Errors:", error_count)

# ===========================================================
# MAIN RUNNER (UNCOMMENT TO TEST)
# ===========================================================

if __name__ == "__main__":
    run_basic_thread()
    run_thread_with_args()
    run_multiple_threads()

    # Race condition demo
    threads = [threading.Thread(target=safe_increment) for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("Counter:", counter)

    thread_pool_map()
    thread_pool_as_completed()

    # Producer-Consumer
    threading.Thread(target=producer).start()
    threading.Thread(target=consumer).start()

    run_daemon()

    # Thread local demo
    threads = [threading.Thread(target=thread_local_example) for _ in range(3)]
    for t in threads: t.start()
    for t in threads: t.join()

    timeout_example()
    benchmark()

    # API ingestion
    data = fetch_all_posts(range(1, 20))
    print(f"Fetched {len(data)} posts")

    # Log processing
    process_logs(["log1.txt", "log2.txt"])