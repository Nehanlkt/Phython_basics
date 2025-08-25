#final vl execute wheteher error occur r not
try:
    l=[1,2,3,4,5]
    i=int(input("enter index:"))
    print(l[i])
except:
    print("some error occured")
finally:
    print("oh")  
#print("oh")  we can print vtout finally also but diff is if we use function
def func1():

    try:
        l=[1,2,3,4,5]
        i=int(input("enter index:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("oh")
#print("oh")
x=func1()
print(x)
#here oh vl not print insted oh oh 2 times it vl print if final key word is not there

