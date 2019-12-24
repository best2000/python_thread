PYTHON MULTITHREADING 

*PYTHON PROGRAM CAN ONLY RUN ONE THREAD AT A TIME so it need to be switching

*Thread switching - thread will switch when a I/O bound task occure (for example reading files, waiting for network respond, 
time.sleep(), when waiting around, etc) thread will switching in ann order of thread created and IT WILL NOT SWITCH BACK UNTIL
ANOTHER I/O BOUND TASK OCCURE. if all thread are all doing I/O task it will switching back and fourth in order

t1 = threading.Thread(target=func, args=(1,))

t1.start() ==> t1 will start immedieatly in this line it mean that current thread will switch from main thread to t1 

t1.join() ==> it will switch from current thread to t1 and will run until it finish and then it can be switch to another thread

t1.daemon = True ==> daemon thread will kill itself automatically after main thread finished so it can be background thread