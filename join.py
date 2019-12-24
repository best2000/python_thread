import threading, time


def func(i):
    print('thread :', i, ': start')
    #
    time.sleep(2)
    #
    print('thread :', i, ': finish')


t1 = threading.Thread(target=func, args=(1,)) #create threat
print('start thread') 

t1.start() #start thread

t1.join() #.join() will make main thread wait for this t1.join()
          #to finish first before continue through main thread 
          #so t2 is not exist at this time 
          # python is stuck here at thread1 and wait for it finish

#*python iterpreter is = main thread

t2 = threading.Thread(target=func, args=(2,)) #t2 is born after t1 because t1.join() is called
t2.start()                                    #so main thread is not working so it cant reach this line of code at that time
t2.join()

print('wait')
time.sleep(1)


print('main fin: ', time.perf_counter()) 