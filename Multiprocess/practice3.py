import thread
 
def hello(id = 0, interval = 2):
    for i in filter(lambda x: x % interval == 0, range(10)):
        print "Thread id : %d, time is %d\n" % (id, i) 
if __name__ == "__main__": 
  '''
    #thread.start_new_thread(hello, (2,4))
  '''  
    thread.start_new_thread(hello, (), {"id": 1})
    thread.start_new_thread(hello, (), {"id": 2})
