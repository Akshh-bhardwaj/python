# Topic 10: System Programming & Networking in Python

System programming handles hardware, file systems, operating system processes, and network communication. Python provides simple, robust standard libraries for OS and TCP/IP networking interactions.

---

## 1. Operating System Interactions (`os`, `sys`, `shutil`)

- **`sys` module**: Provides access to variables and functions that interact closely with the interpreter (e.g. `sys.argv` for CLI arguments, `sys.path` for module search paths, `sys.exit()` to terminate scripts).
- **`os` module**: Multiplatform interface to OS services (e.g., path operations via `os.path`, directory management, permissions, running subshells).
- **`shutil` module**: High-level file operations (copying, moving, archiving, recursive directory deletions).

---

## 2. Process Management (`subprocess`)

The `subprocess` module allows you to spawn new OS processes, connect to their input/output/error pipes, and obtain their return codes.

- **`subprocess.run()`**: The recommended way to run commands. It blocks until the command completes and returns a `CompletedProcess` instance.
- **Pipe redirection**: Capture command output via `stdout=subprocess.PIPE`.

```python
import subprocess
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
```

---

## 3. Network Socket Programming (`socket`)

Network programming in Python is built on top of BSD Sockets, using the `socket` module. Sockets enable communication between processes across a network or locally.

### Key Socket API Methods:
- **`socket.socket(family, type)`**: Create socket object (e.g., IPv4 `AF_INET`, TCP `SOCK_STREAM`).
- **`bind(address)`**: Associate socket with specific IP and port (Server-side).
- **`listen(backlog)`**: Listen for incoming connections (Server-side).
- **`accept()`**: Block and accept incoming connection (returns new socket and address).
- **`connect(address)`**: Connect to server socket (Client-side).
- **`send()`, `recv()`**: Send and receive raw byte packets.
