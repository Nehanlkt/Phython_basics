#strings
apple='''husjusjsms
sjsusjsns
sjsjsjsjmsksk'''#multiline string
print(apple)
print(apple[3])
for character in apple:
    print(character)
app="abcded"
print(len(app))
nm="harry"
print(nm[-4:-2])
#5-4,5-2->1:3 last value always not taken ans is ar
a="!n e h a!!!!"
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))#remove char only after word not before the word
print(a.replace("ne","NE"))
print(a.split("e"))
print(a.split(" "))
jam="intro to python python"
print(jam.capitalize())#only frst char capital
print(len(a))
print(len(a.center(50))) #just to understand
print(a.center(50,","))
print(a.count("python"))
print(jam.count("python"))
print(a.endswith("!"))
print(a.endswith("j"))#true r false
print(a.endswith("h",4,6))#middle value can also be checked
print(a.find("h"))
print(a.find("@"))#-1 if not found if present return index value
#index method raises exception valueerror
print(jam.isalnum())#true if only alp n num if any other char ,returns false
print(a.islower())#true r false
print(jam.isprintable())#true if all char printable .not printable if eg \n is present returns false
print(jam.isspace())#true only when whitespace by tab n space bar here false
bb="  "
print(bb.isspace())#true
print(jam.istitle())#true only if all words frst ltr is capital,here false
print(jam.startswith("int"))#true here starts with given value
print(jam.swapcase())#covert up to low case vise versa
print(jam.title())#capitalise each frst letter of word