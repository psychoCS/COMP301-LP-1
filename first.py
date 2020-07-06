a, b, c  = 10, 10, None

A, B, C = 20, 30, 40

print("hello, World!")

print(f"hello a: {a} b: {b}")

if (a < b):
    print("a is less than b")
elif(a > b):
    print("a is greater than b")
else:
    print("a is equal to b")

if(a == A):
    print("a is equal to A")
else:
    print("a is not equal to A")

for i in range(0, 6):
    print(i)

count = 0

while count < 10:
    print(count)
    count+=1

myArray = [1, 3, 5, 7, 9]

for element in myArray:
    print(element)

    weekDays =["Sunday","Monday","Tuesday","Wednesday","Thurday","Friday"]

    for day in weekDays:
        print(day)

    print ()
    print(weekDays[0])



    # functions need to be defined before we use them
    def sayHello():
        print("Hello, World!")

    sayHello()