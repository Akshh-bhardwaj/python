import asyncio
import multiprocessing
import threading
import time

# ----------------------------------------------------
# Helper Functions
# ----------------------------------------------------
def io_bound_task(task_id):
    """Simulates an I/O bound task like a network API request."""
    time.sleep(0.5)  # Blocks thread execution but releases the GIL

def cpu_bound_task(n):
    """Simulates a heavy CPU computational task."""
    count = 0
    for i in range(n):
        count += i
    return count

async def mock_async_fetch(url, delay):
    print(f"Async: starting fetch for {url}")
    await asyncio.sleep(delay)  # Cooperative sleep (releases event loop)
    print(f"Async: completed fetch for {url}")
    return f"Data from {url}"

async def run_async_tasks():
    start = time.perf_counter()
    # Gather runs tasks concurrently in the single-threaded event loop
    results = await asyncio.gather(
        mock_async_fetch("api/users", 0.6),
        mock_async_fetch("api/posts", 0.4),
        mock_async_fetch("api/comments", 0.2)
    )
    duration = time.perf_counter() - start
    print("Async gathered results:", results)
    print(f"Async operations took a total of {duration:.4f} seconds.")

# Protect the execution entrypoint for safe multiprocessing on macOS/Windows spawn
if __name__ == '__main__':
    # ----------------------------------------------------
    # 1. Multi-Threading vs Sequential (I/O Bound)
    # ----------------------------------------------------
    print("--- 1. Multi-Threading (I/O Bound) ---")

    start = time.perf_counter()
    for i in range(5):
        io_bound_task(i)
    sec_duration = time.perf_counter() - start
    print(f"Sequential execution took: {sec_duration:.4f} seconds.")

    start = time.perf_counter()
    threads = []
    for i in range(5):
        t = threading.Thread(target=io_bound_task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    thread_duration = time.perf_counter() - start
    print(f"Multi-threaded execution took: {thread_duration:.4f} seconds.")
    print()

    # ----------------------------------------------------
    # 2. Multiprocessing vs Sequential (CPU Bound)
    # ----------------------------------------------------
    print("--- 2. Multiprocessing (CPU Bound) ---")

    num_calculations = 4
    heavy_limit = 20_000_000

    start = time.perf_counter()
    for _ in range(num_calculations):
        cpu_bound_task(heavy_limit)
    seq_cpu = time.perf_counter() - start
    print(f"Sequential CPU calculations took: {seq_cpu:.4f} seconds.")

    start = time.perf_counter()
    processes = []
    for _ in range(num_calculations):
        p = multiprocessing.Process(target=cpu_bound_task, args=(heavy_limit,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    mp_cpu = time.perf_counter() - start
    print(f"Multiprocessed CPU calculations took: {mp_cpu:.4f} seconds.")
    print()

    # ----------------------------------------------------
    # 3. Asynchronous Programming (asyncio)
    # ----------------------------------------------------
    print("--- 3. Asyncio Event Loop Concurrency ---")
    asyncio.run(run_async_tasks())
