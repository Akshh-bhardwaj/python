# Topic 4: Concurrency, Parallelism & Asyncio in Python

Python provides multiple concurrency models to execute code concurrently. Depending on whether your task is CPU-bound or I/O-bound, you must choose between threading, multiprocessing, or asynchronous programming.

---

## 1. Threading, Multiprocessing, and the GIL

### The Global Interpreter Lock (GIL)
CPython contains a mutex known as the Global Interpreter Lock (GIL). It allows only one OS thread to execute Python bytecodes at a time.
- **Why it exists**: CPython's memory management is not thread-safe.
- **Implication**: Multi-threaded Python code cannot run code across multiple CPU cores in parallel for CPU-bound computations.

### Threading (`threading`)
- Best for **I/O-bound tasks** (waiting for files, network sockets, databases).
- During I/O calls, the Python interpreter releases the GIL, allowing other threads to run.
- Lightweight compared to processes.

### Multiprocessing (`multiprocessing`)
- Best for **CPU-bound tasks** (data analysis, matrix math, image processing).
- Spawns entirely new Python interpreter instances as processes, bypassing the GIL.
- Each process has its own private memory space, requiring IPC (Inter-Process Communication) to share objects.

---

## 2. Asynchronous Programming (`asyncio`)

Asynchronous programming is a single-threaded concurrent execution model. Rather than switching OS contexts, `asyncio` uses cooperative multitasking controlled by an **Event Loop**.

### Core Concepts:
- **Coroutine**: A function defined with `async def`. It can suspend its execution using the `await` statement.
- **Event Loop**: Runs tasks, coordinates timeouts, and handles I/O operations asynchronously.
- **Future/Task**: Tasks wrap coroutines and allow them to run concurrently within the event loop.

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)  # Releases control to the event loop
    return {"data": 123}
```

### When to use Asyncio:
- Extremely high concurrency of network I/O connections (e.g., chat apps, API gateways, web crawlers).
- Avoids the overhead of spawning hundreds of OS threads.
