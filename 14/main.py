import myMath

print(myMath.add(3,4))
print(myMath.sub(4,2))

from myMath import add,sub
print(add(3,4))
print(sub(4,2))

from myMath import *
print(add(3,4))
print(sub(4,2))
hi~~there is 1 row/rows.
there is 2 row/rows.
there is 3 row/rows.
there is 4 row/rows.
there is 5 row/rows.
there is 6 row/rows.
there is 7 row/rows.
there is 8 row/rows.
there is 9 row/rows.
there is 10 row/rows.

f = open("newfile.txt",'r')

lines = f.readlines()
for line in lines:
    # print(line, end='')
    line = line.rstrip('\n')
    print(line)

f.close()
