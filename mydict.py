#dict is collection of data ordered set
#key value pair
dic={
    "abc": "hss",
    "def": "aa"
}
print(dic["abc"]) #op is hss
dicc={
    34:"neha",
    1:"nn",
    }
print(dicc[34])
dictt={'nn':'ab','age':20,'elg':True}
print(dictt)
print(dictt.get('age'))
#print(dictt['age2'])#shows error
print(dictt.get('age2')) # none vl print
print(dictt.keys())#get all items
for key in dictt.keys():
    print(dictt[key])#get all keys ab 20 true
print(dictt.values())#get all items
for key in dictt.keys():
    print(f"the value corresponding to key {key} is {dictt[key]}")
#methods
#update()method updates value of key provided to it if item already exists in dict,else it creatyes new key value pair
ep1={122:24,44:23}
ep2={22:35,66:79}
ep1.update(ep2)
print(ep1) # add both ep1 n ep2 to ep1
ep1.clear()# empty dict
print(ep1)
#pop to rempove one value pair
#popitem remove last key value pair
#del to remove dict item  we can pass key also 
del ep2[22] #if "22" key value error
print(ep2)
