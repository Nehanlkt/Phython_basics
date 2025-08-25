#no need of break stat only case
x=int(input("enter value of x:"))
match x:
    case 0:
        print("x is 0")
    case 4:
        print("case is 4")
    case _ if x!=90:
        print("x,is not 90")
    case _:
        print(x)
#- is default case            
