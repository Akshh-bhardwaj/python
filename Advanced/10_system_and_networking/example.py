import os
import socket
import subprocess
import sys
import threading
import time

# ----------------------------------------------------
# 1. System & OS Introspection
# ----------------------------------------------------
print("--- 1. System & OS Introspection ---")
print("Python Executable Path:", sys.executable)
print("Current OS Platform:", sys.platform)
print("Process ID (PID):", os.getpid())
print("Current Directory:", os.getcwd())
print()


# ----------------------------------------------------
# 2. Spawning Subprocesses
# ----------------------------------------------------
print("--- 2. Spawning Subprocesses ---")
try:
    # Run a simple shell command and capture its output
    # Using 'python3 --version' to ensure cross-platform availability
    result = subprocess.run(
        [sys.executable, "--version"], 
        capture_output=True, 
        text=True, 
        check=True
    )
    print("Subprocess command executed successfully.")
    print("Stdout:", result.stdout.strip())
except subprocess.CalledProcessError as e:
    print(f"Subprocess failed: {e}")
print()


# ----------------------------------------------------
# 3. Network Sockets: TCP Echo Server & Client
# ----------------------------------------------------
print("--- 3. TCP Echo Server & Client (Concurrent Networking) ---")

HOST = '127.0.0.1'
PORT = 65432  # Non-privileged port

def run_echo_server():
    """Runs a TCP Echo Server on a background thread."""
    # Create an IPv4 TCP socket
    # socket.SO_REUSEADDR allows instant socket rebinding without waiting for OS timeout
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        # print("  [Server] Listening for connection...")
        
        conn, addr = server_socket.accept()
        with conn:
            # print(f"  [Server] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                # Echo received bytes back to client
                conn.sendall(data)
    # print("  [Server] Shutting down.")

# Spawn and start the Echo Server in the background
server_thread = threading.Thread(target=run_echo_server, daemon=True)
server_thread.start()

# Wait 0.1s for server socket binding to complete
time.sleep(0.1)

# Main thread acting as the TCP Client
def run_client():
    """Connects to the background TCP Echo Server and sends data."""
    message = "Hello Advanced Python Network Socket!"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        print(f"  [Client] Connecting to {HOST}:{PORT}...")
        client_socket.connect((HOST, PORT))
        
        print(f"  [Client] Sending: '{message}'")
        client_socket.sendall(message.encode('utf-8'))
        
        response_bytes = client_socket.recv(1024)
        response = response_bytes.decode('utf-8')
        print(f"  [Client] Received Echo: '{response}'")

# Run client connection
run_client()

# Join server thread (will exit since server socket closed and thread is daemonized)
server_thread.join(timeout=1.0)
