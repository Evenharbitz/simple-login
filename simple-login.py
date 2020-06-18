###################
user = 'jabban'   #
password = 'Even' #
###################


def feilmelding():
    print('Wrong username or passwsord!')
    print('         Try Again          ')
    for i in range (3):
        print('')
    ask()


def acces_Granted(linjerover, linjerunder, ganger):
     
    for i in range (linjerover):
        print(' ')
    for i in range (ganger):
       print("##################   Acces Granted   ##################")
    for i in range (linjerunder):
        print(' ')

def ask():
    print('Username: ')
    userin = input()
    if userin == user:
        print('password:')
        passin = input()
        if passin == password:
           acces_Granted(5, 2, 10)
    else:
        feilmelding()




ask()
