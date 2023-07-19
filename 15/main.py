global_var = 'global'

def scope():
    local_var = 'local'
    print(global_var)
    print(local_var)

scope()

print(global_var)
# print(local_var) error

var = 'global'

print(var)#global

def scope():
    var = 'local'
    print(var)#local
    print(var)#local

scope()

print(var)#global

var = 'global'

print('global var: ',var)#global var: global

def scope():
    global var
    var = 'infunction'
    print('global var:', var)#global var:infunction

scope()

print('global var:', var)#global var:infunction

var = 'global'
def scope():
    var = 'local'
    if True:
        print('scope local:',var)#local
    for i in range(3):
            var ='for'
            print('for:',var)#for,for,for

    print('scope local:',var)#for
scope()
print('scope global:',var)#global

try:
    4/0
    print('hi')#doesn't
except ZeroDivisionError as e:
    print(e)#works

print('hello1')#works

try:
    a=1,2
    print(a[3])#doesn't work
    print('hi')#doesn't work
except :
    #pass
    print('index error')#works

print('hello2')#works
