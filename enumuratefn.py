#built i fn allow to loop over sequence(tuple,list,string) and get index,value of each element in sequence at same time
a=[2,3,4,5,6]

index=0
for i in a:
    print(i)
    if(index==3):
        print("hi,oh") 
    index+=1    


a=[2,3,4,5,6]
for index,i in enumerate(a):#(a,start=index value)
    print(i)
    if(index==3):
        print("hi,oh") 
    