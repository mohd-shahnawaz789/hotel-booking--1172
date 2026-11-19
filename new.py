a=int(input("marks of sub 1"))
b=int(input("marks of sub 2"))
c=int(input("marks of sub 3"))
d=int(input("marks of sub 4"))
e=int(input("marks of sub 5"))

total_marks=(a+b+c+d+e)
per=(total_marks*100)/500
if(per>80):
    print("grade A")
    elif(60<per<80):
        print("grade B")
else:
    print("grade C")