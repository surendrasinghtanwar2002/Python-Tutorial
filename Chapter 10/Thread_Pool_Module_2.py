from concurrent.futures import ThreadPoolExecutor
import threading

# Shared resource
shared_counter = 0
lock = threading.Lock()

def increment_counter():
    global shared_counter
    with lock:
        for _ in range(1000):
            shared_counter += 1

def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(increment_counter) for _ in range(10)]
        for future in futures:
            future.result()  # Ensure all tasks complete

    print(f"Final counter value: {shared_counter}")

if __name__ == "__main__":
    main()