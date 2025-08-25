a=input("eneter number:")
print(f"multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e:
    print("e")#prints error u can write anything inside this print
print("some imp")
print("end")
#here we need to enter num if enter string error vl occur in order to avoid the error try and expect is used the error inside try vl not show error and next other statements vl print

