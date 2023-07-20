capitals = {
    'south korea': 'seoul',
    'massachusetts':'boston',
}

# print('what is the capital of {}'.format('south korea'))
# print('what is the capital of {}'.format('massachusetts'))

# print(capitals.keys())
while True:
    count = 0
    for country in capitals.keys():
        print('what is the capital of {}'.format(country))
        
        answer = input('{}?'.format (country))
        
        if answer == capitals[country]:
            print('correct next one')
            count += 1
        else:
            print('wrong next one')
    print('count',count)
    if count == 2:
        print("congratulations for getting them right")
        break
    else:
        print("you'll get it next time ") 
        break       

# while True:
#     for keys in capitals.keys():
#         answer = input(keys)
#         print(answer)

#     if True:
#         for i in answer():
#             print('you\'ve run out of guesses')
#             break
