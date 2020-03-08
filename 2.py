cashback = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]

def menu():
    print("\n")
    print("-------menu-------")
    print("[1]. Input money")
    print("[2]. exit")
    print("------------------")

    Menu = input("pilih : ")

    if int(Menu) == 1:
        cash()
    elif int(Menu) == 2:
        exit()

    else:
        print("\n")
        print ("Wrong Choise!")
        print("\n")
        menu()

def cash():
    Cash = input("Money : ")
    print("\n")
    total = int(Cash)
    cashS = len(cashback)-1
    csh = cashS
    qy = 0
    i = 0
    for i in range(i,cashS):
        while(total>=cashback[csh]):
            total = total-cashback[csh]
            qy = qy + 1
        if qy > 0:
            print("> %d x Rp.%d" % (qy, cashback[csh]))
        csh = csh - 1
        qy = 0
    menu()
menu()
