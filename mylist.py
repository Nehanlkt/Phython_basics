#list:collection of data type,mutable
a=[3,4,"ght",True]
print(a)
print(a[0])
print(a[3])
print(a[-2])#4-2=2,4 is len 
#in keyword
if "i" in a:
    print("s")
else:
    print("no")

#if "4"in gives no , if 4 in gives s bcz there it acts as string n here int
if "eh" in "neha":
    print("s")
    #else ntg vl be displayed(false)
    #same thing for string
print(a[:1])#0 t0 1
#start,end,jump 
print(a[0:3:2])  #3 nd ght jumps 2 times
#list comprehension:to create new list from other iteratable like lists,tuples,dictionaries,sets r array
lst=[i for i in range(4)]
print(lst)#print as list
lst=[i*i for i in range(4) if i%2==0]
print(lst)
#list methods
l=[1,2,4,3]
l.append(4)#adds at the end of list
print(l)
l.sort()#ass order of list
print(l)
l.sort(reverse=True)
print(l)#des order of list
l.reverse()#reverse the original list
print(l)
print(l.index(2))#gives index
print(l.count(3))
b=[11,4,3]
print(b)
c=b
c[0]=1
print(c)#herre c list vl have same list values of 1,4,3
b=[11,4,3]
print(b)
c=b.copy()#here v vl get same list
c[0]=1
print(c)
b.insert(1,4)#index,insert value
print(b)
#extend is used to add lists,sets,tuples here is the eg
m=[9,4,3]
n=[2,6]
m.extend(n)#add n list to m
print(m)
k=l+m
print(k)#to create new list by add