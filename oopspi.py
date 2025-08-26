'''railywayform-class[blueprint]
neha-infrm abt neha form :object[entity]
tom-infrm abt tom form :object[entity]'''
#class n obj
class Person:
    name="neh"
    age=20
    occupation="se"
    def info(self):#self keyword
        print(f"{self.name} is a {self.age}")
#self parameter is reference to current instance of class and is used to access variables that belongs to class
#it provided as extra parameter inside the method defination
#self means that obj on which method is called        


a=Person()
b=Person()
c=Person() #obj creating obj1=details()
a.name="hh"#these all v changes the value
a.age=21 #obj1.name
a.occupation="dd"

b.name="ss"
b.age=22
b.occupation="dff"
print(a.name,a.age,a.occupation)  
a.info()  
b.info()
c.info() #for c values r not given they take default values


