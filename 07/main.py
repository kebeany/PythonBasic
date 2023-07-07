# for i in range(1,10,1):
#     s ='{}*{}={}'.format(2 ,i,2*i)
#     print(s)

# for i in range(1,10,1):
#     s ='{}*{}={}'.format(3 ,i,3*i)
#     print(s)

# for i in range(1,10,1):
#     s ='{}*{}={}'.format(4,i,4*i)
#     print(s)

# multi =int(input("what multiplication table do you want to learn?"))
# for i in range(1,10,1):
#     s ='{}*{}={}'.format(multi ,i,multi*i)
#     print(s)

# for multi in range(3,7):
#     for i in range(1,10):
#         s ='{}*{}={}'.format(multi ,i,multi*i)
#         print(s)

start = int(input("multiplication starting from 1~9"))
end = int(input("multiplication ending from 1~9"))
for multi in range(start,end+1):
    for i in range(1,10):
        s ='{}*{}={}'.format(multi ,i,multi*i)
        print(s)
