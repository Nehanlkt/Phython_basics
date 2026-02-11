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
'''*
   **
   ***'''
rows=int(input("enter num"))
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print()   
'''if same pyramid for num'''
rows=int(input("enter num:"))
for i in range(rows):
    for j in range(i+1):
        print(j+1,end=" ")
    print()    
'''if same for printing alphabets'''
rows=int(input("enter num"))
ascii=65
for i in range(rows):
    for j in range(i+1):
        alpha=chr(ascii)
        print(alpha,end=" ")
    ascii+=1 #if not print this only a pyramid vl get    
    print()    
#inverted pyramid
rows=int(input("enter ur rows"))
for i in range(rows,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()    
text=input("enter text")
print(text)
vowels="aeiouAEIOU"
vowel_count=0
for char in text:
    if char in vowels:
        vowel_count+=1
print(vowel_count)       
for i in reversed(range(5)):
    print(i)