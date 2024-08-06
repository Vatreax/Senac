n =int( input(" Digite Quantos termos você deseja :"))
t1 = 0
t2 = 1

print("{} . {} .".format(t1,t2), end="")

cont = 0

while cont <= n:
    t3 = t1 + t2
    if t3 > 500:
        print ("  {}.".format(t3),end="")
        break

    print ("  {}.".format(t3),end="")
    t1 = t2
    t2 = t3
    cont +=1
    