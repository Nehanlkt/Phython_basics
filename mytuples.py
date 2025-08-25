#tuples r immutable
tup=(1,2,1,"frt",1,True)
tuol=(1,)
tupll=(1)#this is int
print(type(tupll))
#tup[0]=90 is not possible that can be done in list
print(tup[0])
if 2 in tup:
    print("ss")#else no op
tup2=tup[1:4] #from here to here
print(tup2)  
#immutable so frst covert into list n back but we can add two tuples
rest=tup.count(2)
print(rest)
#index(elem,start,end) btw this it vl fnd the index of elem
rss=tup.index(1,2,5)
print(rss)


