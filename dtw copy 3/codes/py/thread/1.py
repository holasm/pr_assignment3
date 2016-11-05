import threading
import time

def fib(n=100):
  a,b = 1,1
  for i in range(n-1):
    a,b = b,a+b
    print(a)

a = threading.Thread(target=fib, args=(15,))
a.start()
a.join()

print('done')