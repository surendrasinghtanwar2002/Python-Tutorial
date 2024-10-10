                                    ## Keyword argument Thread ##

from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

def greet(name, greeting="Hello"):
    sleep(5)  # Delay for 5 seconds
    return f"{greeting} {name}"

def main():
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = [
            executor.submit(greet, name="Alice", greeting="Hi"),
            executor.submit(greet, name="Surendra", greeting="Hello"),
            executor.submit(greet, name="Rocky", greeting="Good Morning"),
            executor.submit(greet, name="Jammine", greeting="Good Afternoon"),
            executor.submit(greet, name="Alex", greeting="Good Evening"),
        ]
        
        # Process results as they complete
        for future in as_completed(futures):
            result = future.result()
            print(f"This is the final result: {result}")

# Call the main function
if __name__ == "__main__":
    main()
