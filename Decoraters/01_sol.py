import time

def timmer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        func(*args,**kwargs)
        end=time.time()
        return f"Function {func.__name__} takes time {end-start}"
    return wrapper

@timmer
def call_DB():
    print("Data Fetching from DB")
    time.sleep(4)
    print("Data is Fetched")

print(call_DB())