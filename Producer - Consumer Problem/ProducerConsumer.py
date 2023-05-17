#q1
import threading
import time
items = []
items_cv = threading.Condition()
def producer():
    print ("I'm the producer")
    for i in range(5):
        with items_cv:          
            items.append(i)    
            items_cv.notify()   
        time.sleep(1)
def consumer():
    print ("I'm a consumer", threading.currentThread().name)
    while True:
        with items_cv:           
            while not items:     
                items_cv.wait()  
            x = items.pop(0)     
        print (threading.currentThread().name,"got", x)
        time.sleep(5)
cons = [threading.Thread(target=consumer)
        for i in range(10)]
for c in cons:
    c.setDaemon(True)
    c.start()
producer()
