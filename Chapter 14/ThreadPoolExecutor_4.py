                            ## Map Method Basic Thread Pool Executor ##

from concurrent.futures import ThreadPoolExecutor
import time

# Function to compute square of a number
def square(n):
    time.sleep(3)  # Simulate a time-consuming task
    return n * n

# Main function
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(square, numbers)
    
    # Output the results
    print("Squared results:")
    for result in results:
        print(result)
