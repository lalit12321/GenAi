#try-except combination
#try-finally combination{if v use this combination v dont give discription of exception} this no recomndate.


#h
try:
    a = int(input("enter first value "))
    b = int(input("enter secound value "))
    if b!=0:
        c = a / b
        print("Div" ,c)
    else:
        raise ZeroDivisionError("Denominator should not be zero")
except ZeroDivisionError as e:
    print(e)
    print("Denominator should not be zero")
except ValueError as e:
    print(e)
    print("value should be an integer")
except:
    print("Exception found")
else:
    print("Except-else block")
finally:
    print("Finally block")   #must executable code
print("bye")
