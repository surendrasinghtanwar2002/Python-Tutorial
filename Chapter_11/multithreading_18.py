                        ##In this section we will practise the code with using the join method ##

from threading import Thread
from time import sleep

##Creting the target function
def video_upload():
    try:
        print("Video is being uploading please wait")
        sleep(6)                    ##delay for 6 second
        print("Wait we are adding your script in the video")
        sleep(2)
    except Exception as e:
        print(f"This is the exception of video upload{e}")

##Creating the notification menu
def notification():
    try:
        print("Your video have been uploaded")
    except Exception as e:
        print(f"This is the exception of the function {e}")

##Creating the thread for each task
t1 = Thread(target=video_upload)
t2 = Thread(target=notification)
t1.start()
t1.join()
t2.start()
t2.join()



