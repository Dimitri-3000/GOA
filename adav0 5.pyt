

def blabla(listi):
    uaryofitebi = []
    dadebitebbi = []
    for i in listi:
        if i < 0:
            uaryofitebi.append(i)
        elif i > 0:
            dadebitebbi.append(i)
        else:
            continue
    print(len(uaryofitebi))
    print(sum(dadebitebbi))
            

mymylist = [1,3,5,-9,-8,0,7,8,-5,-8,6,0,6,]

blabla(mymylist)

