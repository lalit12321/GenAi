#

# a = 23

# if not type(a) is int:
#     raise TypeError("Only integers are allowed")
# print("bye")

#custom exception
try:
    a=-145
    if a>100:
        raise Exception("value is > 100 Exception")
    elif a<0:
        raise Exception("value is < 0 Exception")
except Exception as e:
    print(e)
else:
    print("value",a)
