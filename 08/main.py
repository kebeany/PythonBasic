import random

answer = random.randint(1,100)
print("1~100 is going to be the range.")

min=1
max=100
count=0
s = 'count : {}'
s.format(1) # count : 1
while True:
    user= int(input("whats the number?({}~{})".format(min,max)))

    count=count+1
    print(s.format(count))
    if user<answer:
        print("that is too small.")
        min= user +1
    elif user>answer:
        print("that is too big")
        max= user-1
    else:
        print("correct")
        break
    
    if count>10:
        print("fail")
        print(answer)
        break
