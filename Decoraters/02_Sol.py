
def paraDeco(func):
    def wrapper(*args, **kwargs):
        argsVal=','.join(str(argsItem) for argsItem in args)
        kwargsVal=','.join(f'{key}={val}' for key , val in kwargs.items())
        func(*args,*kwargs)
        return f'{func.__name__} have args {argsVal} and Kwargs {kwargsVal}'
    
    return wrapper

@paraDeco
def call_DB(*args,**kwargs):
    print("Data Fetching from DB")
   
    print("Data is Fetched")

print(call_DB("SLQ", DBMS="SQL Server"))