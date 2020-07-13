# a = int(input("enter number of rows you want to print\n"))
# b = int(input("type 0 or 1\n"))
# c = bool(b)
# if c == True:
#     for i in range(1,a+1):
#         for j in range(1,i+1):
#             print("*\n")
#
# elif c ==False:
#   for i in range(a,0,-1):
#    for j in range(1,i+1):
#       print("*\n")

# inp = int(input("enter your number"))
# print("*\n"*inp)
print("how many rows you want to print")
one = int(input())
print("type 1 or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(i,i+1):
            print("*",end=" ")
            print()
elif new == False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
            print()



