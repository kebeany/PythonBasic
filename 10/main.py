l1 = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
print(len(l1))

t1 = ( 1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10)
print(len(t1))

s1 = "123456789012345678901234567890"
print(len(s1))

string = "hello"
for i in range(len(string)):
    print(string[i])

list1 = ["l","i","s","t",1,2,3]
for i in range(len(list1)):
    print(list1[i])

tuple1 = ("tu","ple",4,5,6)
for i in range(len(tuple1)):
    print(tuple1[i])

num = 10
scores = [0] * num

for i in range(num):
    scores[i] = int(input('{} student score:'.format(i+1)))

for i in range(num):
    print('{} student score is {}'.format(i+1,scores[i]))

string = "hello"
for c in string:
    print(c)

list1 = ["li","s","t",1,2,3]
for var in list1:
    print(var)

tuple1 = ("tu","ple",4,5,6)
for var in tuple1:
    print(var)

number=0
scores = [90,25,67,45,80,10,60,87,100,40]
for score in scores:
    number = number + 1
    if score >=60:
        print('{} passed'.format(number))
    else:
        print('{} failed'.format(number))

letters = ['A','B','C']

i=0
for letter in letters:
    print(i,letter)
    i +=1

for i in range(len(letters)):
    letter = letters[i]
    print(i,letter)

for i,letter in enumerate(letters):
    print(i,letter)


number=0
scores = [90,25,67,45,80,10,60,87,100,40]
for score in scores:
    number = number + 1
    if score >=60:
        print('{} passed'.format(number))
    else:
        print('{} failed'.format(number))

for i, score in enumerate(scores):
    print(i,score)
