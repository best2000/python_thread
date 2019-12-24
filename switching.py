import threading, time


def func(i):
    print('thread :', i, ': start')
    time.sleep(0.1)
    print('waitin')
    time.sleep(3)
    print('thread :', i, ': finish') 



t1 = threading.Thread(target=func, args=(1,)) 
print('start thread') 

t1.start() 
time.sleep(1)                                                  
t1.join()
print('wait') 
time.sleep(0.1) 

print('main fin: ', time.perf_counter()) 