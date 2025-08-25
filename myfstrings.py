#fstrings for formatting
letter="hey my name is {0} and i am from {1}"
name="neha"
country="India"
print(letter.format(name,country))
'''if country = india
name=neha
then hey name is india and i am frm neha vl print'''
#in order to avoid this give num in {}
#num r given based on the below values order
#f string
print(f"hey my name is {name} and i am from {country}")
price=44.90750
txt=f"for only {price:2f}"#2f is 2 floating points
print(txt)
print(f"hey my name is {{name}} and i am from {{country}}")
#print as name n country only