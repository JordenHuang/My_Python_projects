lusername = input('Enter your username: ')


with open('UserPassword.txt') as fh:
    text = fh.readlines()
    for line in text:
        lineSplit = line.replace('[', '').replace(']', '').replace(',', '').split()
        wrongUsername = True
#        print(lineSplit[0])
        if lusername == lineSplit[0]:
            wrongUsername = False
            lpassword = input('Enter your password: ')
            if lpassword == lineSplit[1]:
                print('Login successfully, Welcome')
                break
            else:
                print('Wrong password !!')
                break

    if wrongUsername:
        print('Wrong username !!')
