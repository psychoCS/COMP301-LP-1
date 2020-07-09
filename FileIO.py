#step 1 is open a file
fileObject = open("numbers.txt", "r")

#step 2 is read from the file
content = fileObject.read()

#step 3 is close out the file
fileObject.close()

print(content)

#Write

#step 1 is open a file
fileObject = open("numbers2.txt", "w+")

#step 2 create the new variable and write
numbers = [33, 55, 66 , 77, 88, 99]

count =0

for number in numbers:
    count += 1
    if count == len(numbers):
        fileObject.write(str(numbers) + ",")
    else 


#step 3 is close out the file
fileObject.close()

