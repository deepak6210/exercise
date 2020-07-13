# faulty calculator
# 45*3= 555 , 56+9=77, 56/6= 4
"""design a calculator which will correctly solve all the problems expect
the mentioned above
your program should take operator and the two numbers as input from the user
and then return the results"""
print("enter your number")
n1 = int(input())
print("press + for addition")
print("press * for multiplication")
print("press / for division ")
print(" press - for substraction")
o = input()
print("enter your secound number")
n2 = int(input())
if o=="+":
    if n1==56 and n2==9:
        print("77")
    else:
        print(n1 + n2)
if o=="-":
    print(n1-n2)
if o=="*":
    if n1==45 and n2==3:
        print("555")
    else:
        print(n1*n2)
if o =="/":
    if n1==56 and n2==6:
        print(4)
    else:
        print(n1/n2)



