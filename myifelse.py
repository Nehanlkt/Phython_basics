a=int(input("enter ur age"))
print("ur age is:",a)
if(a>18):
    print("can drive")
else:
    print("cannot drive")#space is neccasary
print("oh")#this vl print for both if n else       
print(a==18)
print (a<18) 
#conditional opr >,<,==,=!,>=,<=  
#elif stat:frst check if,then elif the num of times it present
num=int(input("enter a num:"))
if(num<0):
    print("ngtv num")
elif(num==0):
    print("num is 0")
elif(num==999):
    print("special num")
else:
    print("pstv num")
print("happy")    
#nestedif stat:if elif else stat in other if stat
#here space is imp
num=18
if(num<0):
    print("ngtv")
elif(num>0):
    if(num<=10):
        print("num btw 0 to 10")
    elif(num>0 and num<=20):
        print("num btw 11 n 20")
    else:
        print("num grtr than 20")
else:
    print("num is 0")      
              



