cube=lambda x:x**3
# print(cube(3))

# y=4
# def f1(x):
#     # y=x
#     def f2(y):
#         return x*y
#     return f2(y)

# print(f1(5))
y=10
def f2(x):
    y=x
    def f2(y):
        return x*y
    return f2

# print(f2(5))

# -------------------Even Generator------------------------

def evenGen(limit:int)->any:
    for i in range(0,limit+1,2):
        # print(i)
        # return i
        yield i 

even=evenGen(10)
# for num in even:
#     print(num)

# def add(*args):
#     # sums=sum(args)
#     print(args)
#     sum=0
#     for val in args:
#         sum+=val
#     return sum
# print(add(1,2))
# print(add(1,2,4))

# def dicts(name,hobby):
#     # sums=sum(args)
#     print(f'name isn{name} and hoppy is {hobby} ')
#     # sum=0
#     # for key, val in kwargs:
#     #     print(key, val)
#     # return kwargs
# dicts(name='Awais', hobby='circket')
# dicts(name='Awais')
# print(dicts(1,2,4))

# def dicts(**kwargs):
#    for key, val in kwargs.items():
#        print(f"{key} {val}")
# dicts(name='Awais', hobby='circket')
# dicts(name='Awais')

# x=4
# def f1(z):
#     y=z
#     def f2(y):
#         return x*y
#     return f2(y)
# result=f1(5)
# print(result)

# x=4
#---------------------Closures---------------------------
def upper(num):
   
    def inner(x):
        return x**num
    return inner
sqr=upper(2)
cube=upper(3)

print(sqr(3))
print(cube(3))