import threading

con = threading.Condition()         ##Created the object of the condition


#First Trigger Function
def write_data():
    try:
        con.acquire()               ##Lock the mechanism
        print(f"This is the current thread of the function {threading.current_thread()}")
        print("In this section we will take all the days temperature".center(120))
        with open("Temperature.txt","w") as file:
            days_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
            for day in days_list:
                user_temp = input(f"Enter your temperature for {day}:- ")
                file.write(user_temp+"\n")
        con.notify_all()            ##In this step it will first notify to all other thread that they can execute the task after my completion
        con.release()               ##It will release the lock
    except Exception as e:
        print(f"This is the common exception of the function",e)

#Second Trigger Function
def max_temperature():
    try:
        con.acquire()
        con.wait(timeout=0)
        with open("Temperature.txt","r") as f:
            data = f.readlines()
            max1 = float(data[0].strip("\n"))
            for temp in data[1:]:
                temp = float(temp.strip('\n'))
                if temp > max1:
                    max1 = temp
        print(f"This is your max temperature:- {max1}")

        print("In this section we will find the max temperatur")
        con.release()
    except Exception as e:
        print(f"This is the exception of the function",e)
        

##Third Trigger Function
def min_temperature():
    try:
        con.acquire()
        con.wait(timeout=0)
        print('In thi section we will find the min temperature')
        with open("Temperature.txt","r") as f:
            data = f.readlines()
            min1 = data[0].strip("\n")
            for temp in data:
                temp = temp.strip("\n")
                if temp < min1:
                    min1 = temp
        print(f"This is your minimum value {min1}")
        con.release()
    except Exception as e:
        print(f"This is the exception of the function",e)

##Creating the thread object for each target function
thread1 = threading.Thread(target=write_data,name="write_temperature_data")
thread2 = threading.Thread(target=min_temperature,name="max_temperature_thread")
thread3 = threading.Thread(target=max_temperature,name="min_temperature_thread")

##Starting all the threads
thread1.start()
thread2.start()
thread3.start()

##Waiting for all the threads to be completed
thread1.join()
thread2.join()
thread3.join()

##After all the child thread completed the parent thread will print its current value
# print(f"After the all completion Main thread will be executed {threading.main_thread()}")
