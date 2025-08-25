#cntn:to break iteration at some point n then cntn the other stat
#break:to break loop
for i in range(12):
    print("5 x",i+1,"=",5*(i+1))
    if(i==10):
        break
print("skip loop")    
#here upto 11 that is 5x10+1=5x11
for i in range(12):
    if(i==10):
        break
    print("5 x",i+1,"=",5*(i+1))
print("skip loop")
#here upto 5x9+1=5x10
# placement of break stat matters 
#cntn
for i in range(12):
    if(i==10):
        print("skip iteration")
        continue
    print("5x",i,"=",5*i)
#5x10 vl not execute there vl print skip iteration nxt 5x11 vl execute    


