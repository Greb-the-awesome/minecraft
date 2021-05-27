import threading
import time

def blocking_function(a):
	print("blocking function started")
	time.sleep(10)
	print("blocking function ended")

print("before thread")
x = threading.Thread(target=blocking_function, args=(1,))
x.start()
print("x started")