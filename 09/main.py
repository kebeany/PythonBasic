scores = [10,50,30,60]
print(scores[1])#50
print(scores[-1])#60
print(scores[2:4])#[30,60]
print(scores[1:3])#[50,30]
print(scores[2:])#[30,60]
print(scores[:2])#[10,50]

a = [1,2,3]
b=[4,5,6]
print(a+b)

a = [1,2,3]
print(a*3)

scores = [10,59,93,76]
scores.append(80)
print(scores)

scores =[10,59,93,76]
scores.insert(2,40)
print(scores)

scores.insert(4, 80)
print(scores)

scores = [10,10,59,93,76]
scores[0] = 100
print(scores)#100,10,59,93,76

del scores[0]
print(scores)#10,59,93,76

scores.remove(10)
print(scores)#59,93,76

t = (1,2,3,4)
# del t[0]
# t[0] = 5

print(t[0])
print(t[3])
print(t[1:])

t1 = (1,2)
t2 = (3,4)
print(t1+t2)
t3 = t1 +t2
print(t3*3)

rainbow = ('red','orange','yellow','green', 'blue','purple')
first = rainbow[0]
print('rainbows first color is {}.'.format(first))
last = rainbow[5]
print('rainbows last color is {}.'.format(last))
