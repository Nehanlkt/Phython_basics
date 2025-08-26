x=4
print(x)

def hello():
    x=5
    print(f"the local x is {x}")
    print("ss")


print(f"the global variable x is {x}")#from here execution starts
hello()    
x=5
print(f"the global x is {x}")#here 4 only but we change by putting x=5 before this statement
#local variables destroyed whereas global variable wont
#but to change inside 
#local variable is defined inside the fn n can be accessed vtin fn n is destroyed when fn returns
#eg
def a():
    x=5
    y=4
    print("kk")
a()
print("hh")
#print(y) shows error bcz y is local variable
#global variable defined outside the fn n accesible from vtin fn
#global keyword used to declare that varibale is global varibale and should be accesed from global scope
#to modify global variable
x=10
def my_fn():
    global x
    x=4
    y=5
    print(y)
my_fn()
print(x)
#now here x vl print as 4     