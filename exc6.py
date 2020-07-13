# Health managment system
# 3 client - deepak,gaurav,amit
def getdate():
     import datetime
     return datetime.datetime.now()
# print([getdate()],"chicken Roti\n")
# total 6 files
# write a function that when executed take as input client name
# one more function to retrieve exercise or food for any client
print("You Want To\n","1.LOCK (press 1 for lock) \n","2.RETRIEVE(press 2 for retrieve)\n")
inp1 = int(input())
if inp1 == 1:
    print("you want to excess\n","1.Deepak(press 1 for deepak file)\n","2.gourav(press 2 for gourav file)\n",
          "3.amit(press 3 for amit file\n)")
    inp2 = int(input())
    if inp2 == 1:
        print("1.exercise\n","2.food\n")
        inp4 = int(input())
        if inp4 == 1:
            value = input("type here\n")
            with open("deepakexc.txt","r") as op:
             op.write(str([str(getdate())])+": "+value+"\n")
            print("succesfully written")


            print("what you want to write\n")
            f.close()
        elif inp4 == 2:
            f = open("deepakfood.txt", "a")
            b = f.write("\n")
            print("what you want to write","b")
            f.close()
    elif inp2 == 2:
        print("1.exercise\n", "2.food\n")
        inp5 = int(input())
        if inp5 == 1:
            f = open("gauravexc.txt.txt", "a")
            c = f.write("\n")
            print("what you want to write",c)
            f.close()
        elif inp5 == 2:
            f = open("gauravfood.txt", "a")
            d = f.write("i am learning python\n")
            print("what you want to write",d)
            f.close()
    elif inp2 == 3:
        print("1.exercise\n", "2.food\n")
        inp6 = int(input())
        if inp6 == 1:
            f = open("amitexc.txt", "a")
            e = f.write("\n")
            print("what you want to write", e)
            f.close()
        elif inp6 == 2:
            f = open("amitfood.txt", "a")
            d = f.write("\n")
            print("what you want to write", d)
            f.close()
    else:
        print("you chosse invalid input please try again")
if inp1 == 2:
    print("you want to excess\n", "1.Deepak(press 1 for deepak file)\n", "2.gourav(press 2 for gourav file)\n",
          "3.amit(press 3 for amit file\n)")
    inp7 = int(input())
    if inp7 == 1:
        print("1.exercise\n", "2.food\n")
        inp8 = int(input())
        if inp8 == 1:
            f = open("deepakexc.txt", "rt")
            print([getdate()],f.readlines(), end="")
            f.close()
        elif inp8 == 2:
            f = open("deepakfood.txt", "rt")
            print([getdate()],f.readlines(), end="")
            f.close()
    elif inp7 == 2:
        print("1.exercise\n", "2.food\n")
        inp9 = int(input())
        if inp9 == 1:
            f = open("gauravexc.txt", "rt")
            print([getdate()],f.readlines(), end="")
            f.close()
        elif inp9 == 2:
            f = open("gauravfood.txt", "rt")
            print([getdate()],f.readlines(), end="")
            f.close()
    elif inp7 == 3:
        print("1.exercise\n", "2.food\n")
        inp10 = int(input())
        if inp10 == 1:
            f = open("amitexc.txt", "rt")
            print([getdate()],f.readlines(), end="")
            f.close()
        elif inp10 == 2:
            f = open("amitfood.txt", "rt")
            print([getdate()],f.readlines(), end="")
            f.close()
    else:
        print("you chosse invalid input please try again")
