#set:unorded collection of data items
#immutable like in place 2 we cant place 8
#do not contain duplicate items
s={2,4,2,"car",False,6}
print(s)#op not in order n 2 printed only once
seh={}
print(type(seh))#gives dict
seg=set()
print(type(seg))#give set
for value in s:
    print(value)
s1={1,2,3,4}
s2={2,4,5,6} 
print(s1.union(s2))   #no repeat items in set
print(s1,s2) #s1 n s2 vl not be changed
s1.update(s2)#which values not in s1 of s2 vl add to s1 here 5 n 6 vl add to s2
print(s1,s2)
#intersection n update
s1={1,2,3,4}
s2={2,4,5,6}
#symdiff=(aub)-(ainterb) print which r not common in both
s3=s1.symmetric_difference(s2)
print(s3)
#diff n diff update:print only items present in original set and not in both sets
#diff update method updates existing set from another set
#methods
#isdisjoint() check if they no common elem true
#issuperset() if all elem of some set present in original set returns true
#issubset() if all items of original set r present in some set then true
#add() to add single item
#update() to add more items
#remove() if elem not there then shows error
#discard() no error
#pop() removes last elem vt access also possible
#del() delete entirely it is also a keyword
#clear() delete all elem in set
