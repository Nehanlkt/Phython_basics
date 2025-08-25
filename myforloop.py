#loops to print stat certain num of times
#for n while loop two types
#here diff is btw for i n for clr
#for color display all clrs
#for i splits the clr letters
colors=["red","white","green"]
for clrs in colors:
    print(clrs)
    for i in clrs:
        print(i)
  #range: 0 to mentioned num - 1 0 to 4,if k +1 then 0 t0 5
for k in range(5):
    print(k)
for k in range(5):
    print(k+1)
for k in range(1,5):#1 to 4
    print(k)
#3 parameters of range start stop step step never be 0
#step if pstv to increment ,negtv to decrement btw num here 3 tht is 1 to 4 tht is 4 nxt +3=7 nxt +3=10
for k in range(1,12,3):
    print(k)   

