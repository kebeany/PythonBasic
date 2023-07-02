name = input('whats your name')
print(name)
age = input('whats your age?')
print(age)
age = int(age)
print('I am {} years old.'.format(age))
print('I am going to be {} years old next year.'.format(age + 1))
def eatingCerial():
    print("getting cerial in the bowl")
    print("getting milk in the bowl")
    print("getting spoon in the bowl")
    print("eat the cerial")
eatingCerial()
eatingCerial()
def eatingCerial(milk,cerial,bowl,spoon):
    print(f"getting {cerial} in the {bowl}")
    print(f"getting {milk} in the {bowl}")
    print(f"getting {spoon} in the {bowl}")
    print(f"eat the cerial")
eatingCerial('milk','cerial','bowl','spoon')
eatingCerial('whole milk','fruitloops cerial','glass bowl','metal spoon')
def eatingCerial(milk,cerial,bowl,spoon):
    print(f"getting {cerial} in the {bowl}")
    print(f"getting {milk} in the {bowl}")
    print(f"getting {spoon} in the {bowl}")
    print(f"eat the cerial")
    return "{} 1return, {}500 cheese.".format(milk,cerial) 
s =eatingCerial('whole milk','fruitloops cerial','glass bowl','metal spoon')
print(s)
def add(num1,num2):
    return num1+num2

a = 3
b = 4
c = add(a,b)
print(c)
print(add(10,15))
print(add(2345889,194943))
print(add (3, 10000000000))

def hello():
    print("hello")

hello()
