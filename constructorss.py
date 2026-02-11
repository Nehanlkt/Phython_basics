#constructors:special method in class used to create and intialize obj of class
class Person:
    def __init__(self,n,o):
       print("i am person")#this stat vl print everytime for every obj creation
       self.name = n #name also can be written r n
       self.occ = o
    #name="neh"
    #occ="cc"


    def info(self):
     print(f"{self.name} is a {self.occ}")


a=Person("neh","cc")
b=Person("hh","kk")
#c=Person() show error n even if c=Person(1,2,3) shows error that it has 4 arguments which includes self also
#print(a.name)
#or a.info
#a.name="hh"
#a.occ="kk"
a.info()
b.info()