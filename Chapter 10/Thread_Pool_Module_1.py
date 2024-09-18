from concurrent.futures import ThreadPoolExecutor, as_completed
import time

##Task Function
def task_function(number):
    time.sleep(1)  # Simulate a delay
    return f"Result of task {number}"

# Using ThreadPoolExecutor to manage tasks


devices = [
    {"device_type":"cisco_ios",
     "host":"192.168.1.100",
     "username":"admin",
     "password":"hackerzone"
     },
     {"device_type":"cisco_ios",
     "host":"192.168.1.105",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.110",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.115",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.120",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.125",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.130",
     "username":"admin",
     "password":"hackerzone"
     },
     {"device_type":"cisco_ios",
     "host":"192.168.1.115",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.120",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.125",
     "username":"admin",
     "password":"hackerzone"
     },
     {"device_type":"cisco_ios",
     "host":"192.168.1.115",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.120",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.125",
     "username":"admin",
     "password":"hackerzone"
     },
     {"device_type":"cisco_ios",
     "host":"192.168.1.115",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.120",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.125",
     "username":"admin",
     "password":"hackerzone"
     },
     {"device_type":"cisco_ios",
     "host":"192.168.1.115",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.120",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.125",
     "username":"admin",
     "password":"hackerzone"
     },
     {"device_type":"cisco_ios",
     "host":"192.168.1.115",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.120",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.125",
     "username":"admin",
     "password":"hackerzone"
     },
     {"device_type":"cisco_ios",
     "host":"192.168.1.115",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.120",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.125",
     "username":"admin",
     "password":"hackerzone"
     },
     {"device_type":"cisco_ios",
     "host":"192.168.1.115",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.120",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.125",
     "username":"admin",
     "password":"hackerzone"
     },
     {"device_type":"cisco_ios",
     "host":"192.168.1.115",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.120",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.125",
     "username":"admin",
     "password":"hackerzone"
     },
     {"device_type":"cisco_ios",
     "host":"192.168.1.115",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.120",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.125",
     "username":"admin",
     "password":"hackerzone"
     },
     {"device_type":"cisco_ios",
     "host":"192.168.1.115",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.120",
     "username":"admin",
     "password":"hackerzone"
     },
      {"device_type":"cisco_ios",
     "host":"192.168.1.125",
     "username":"admin",
     "password":"hackerzone"
     },
    ]
def main():
    results = []
    with ThreadPoolExecutor(max_workers=7) as executor:
        # Submit tasks to the executor
        future_to_number = {executor.submit(task_function, i): i for i in devices}

        # Retrieve results as tasks complete
        for future in as_completed(future_to_number):
            result = future.result()
            results.append(result)
            print(result)

    print("All tasks completed.")

if __name__ == "__main__":
    main()