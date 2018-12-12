# def func1


# def func2 

# func1()
# func2()


# .py process


# .py 

# process 
# t1
# t2 
import threading
import time
def sqr(num1):
	global count
	print("Inside square fun")
	# time.sleep(5)	
	# print(num1 * num1)
	lock.acquire()
	for value in range(5):
		count = count + 10
		print(count) 
		time.sleep(1)
	lock.release()


def multiply(num1,num2):
	global count
	# print("Inside multiply ")
	# print(num1 * num2)
	lock.acquire()
	for value in range(5):
		count = count + 2
		print(count) 
		time.sleep(2)
	lock.release()


# sqr(10)
# multiply(10,20)
count = 100 
lock = threading.Lock()
t1 = threading.Thread(target = sqr,args= (10,))
t2 = threading.Thread(target = multiply,args = (10,20))

t1.start()
# t1.join(2)
t2.start()

# race condition 
# deadlock 
