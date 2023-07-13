age = {}
age['tree'] = 12
age['plant'] = 10
print(age)
age[1] = 'a'
print(age)
age['key'] = [1,2,]
print(age)

age['tree'] = 13
print(age)

del age[1]
print(age)

del age['tree']
print(age)

print(age['plant'])

var={1:'a',2:'b'}
print(var[1])
print(var[2])

var = {'a':1,'b' :2}
# print(var[1]) error

print(var['a'])
print(var['b'])

flower = set(['blue','yellow','blue','red'])
print(flower)

s = {}
s1 = set([1,2,3])
s1={1,2,3,'hi'}
print(s1)

l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

s1 = {1,2,3}
s1.add(4)
print(s1)

s1 = {1,2,3}
s1.update([4,5,6])
print(s1)

s1 = {1,2,3}
s1.remove(2)
print(s1)

s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}

print(s1&s2) # {4,5,6}
print(s1|s2) # {1,2,3,4,5,6,7,8,9}
print(s1-s2) # {1,2,3}
print(s2-s1) # {7,8,9}
age = {'tree' : 12, 'plant' : 10, 'seed' : 9, 'plant':10}
print(age.keys())

for key in age.keys():
    print(key,age[key])
