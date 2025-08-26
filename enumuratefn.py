#built i fn allow to loop over sequence(tuple,list,string) and get index,value of each element in sequence at same time
marks=[2,3,4,5,6]

index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("hi,oh") 
    index+=1    


marks=[2,3,4,5,6]
for index,mark in enumerate(marks):#(a,start=index value)
    print(mark)
    if(index==3):
        print("hi,oh") 
    