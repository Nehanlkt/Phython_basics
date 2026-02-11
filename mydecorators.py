

def greet(fx):
    def mfx(*args,**kwargs):
        print("gm")
        fx(*args,*kwargs)
        print("yha") 
    return mfx       

@greet #decorator 

def hello():
    print("hlo")

def add(a,b):
    print(a+b)

hello() #ig not @greet used we can even use like greet(hello)()
greet(add)(1,2)
