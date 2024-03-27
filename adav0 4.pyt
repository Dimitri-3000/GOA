
def shemaertebeli(word):
    kato = ''
    for i in word:
        if i != ' ':
            kato = kato + i
        else:
            continue

    print(kato)
    

sityva = input('winadadeba : ')

shemaertebeli(sityva)
