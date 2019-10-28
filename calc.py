import random

yesList = ['yes','yup','okay','sure','ok']

name = input('what is your name?\n')

print ('hello,',name)
#'if a rare coincidence happens, use shift command 4'
if name.lower() == 'burt':
    ask = input('do you want to play a game?')

    while ask.lower() in yesList:
        randomNumber = random.randint(1,100)


        guess = input('guess my random number')

        while int(guess) != randomNumber:
            if int(guess)>randomNumber:
                print ('too high!')
            elif int(guess)<randomNumber:
                print ('too low!')

            guess = input('wrong! guess my random number again!')
        print ('Correct!')

        ask = input('do you want to play another game?')
else:
    ask = input('do you want to use a calculator?')

    while ask.lower() in yesList:
        num1 = int(input('enter a number'))
        sign = input('enter the sign')
        num2 = int(input('enter the 2nd number'))
        result = 'ERROR'

        if sign == '+':
            result = (num1+num2)
        elif sign == '-':
            result = (num1-num2)
        elif sign == '*':
            result = (num1*num2)
        elif sign == '/':
            result = (num1/num2)

        else:
            print('what sign have you typed? I am very confused.')

        print(num1,sign ,num2,'=',result)


        ask = input('do you want to use another calculator?')
