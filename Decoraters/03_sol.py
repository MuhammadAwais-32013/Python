import time

def cache(func):
    cache_val={}
    print(cache_val)
    def wrapper(*args):
       if args in cache_val:
           return cache_val[args]
       result=func(*args)
       cache_val[args]=result
       return result
    return wrapper

@cache
def call_DB(a,b):
    # print("Data Fetching from DB")
    time.sleep(3)
    # sum=0
    # for val in args:
    #     sum+=val
    # time.sleep(4)
    # print("Data is Fetched")
    return a + b
print(call_DB(2,3))
print(call_DB(2,3))
print(call_DB(3,3))
