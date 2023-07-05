money = 10000
distance= 100
weather = 'rain'
if(money>10000) and (distance >=100) and (weather == 'rain'):
    print('ride taxi')
else:
    print('your walking')
money = 12000
distance= 100
weather = 'rain'
if(money>10000) and (distance >=100) and (weather == 'rain'):
    print('ride taxi')
else:
    print('your walking')

money = int(input("how much money do you have?"))
distance= int(input("how far is your destination?"))
weather= input("what is the weather?")
if(money>10000) and (distance >=100) and (weather =='rain'):
    print('ride taxi')
else:
    print('your walking')

if (money>=10000) or (distance >=100) or (weather =='rain'):
    print('ride taxi')
else:
    print('your walking')
written_test = 75
coding_test = True
if written_test >= 80 and coding_test:
    print('pass')
else:
    print('fail')
rapeokki = 'close'
hamburger = 'open'
tteokbokki = 'close'
ramen ='open'
if hamburger == 'open':
    print('eat the hamburger')
elif tteokbokki == 'open':
    print('eat the tteokbokki')
elif ramen == 'open':
    print('eat the ramen')
elif rapeokki == 'open':
    print('eat rapeokki')
else:
    print('go home')
score = int(input("grade:"))
if 81 <= score:
    print('grade: A')
elif 61<=score:
    print('grade:B')
elif 41<=score:
    print('grade:C')
elif 21<=score:
    print('grade:D')
else:
    print('grade:F')
