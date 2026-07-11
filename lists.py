print("Method 1\n")
myname1 = [1,2,3,4]
myname2 = [5,6,7]

myname3 = myname1 + myname2
print(myname3)

print("Method 2\n")

myname1.extend(myname2)
print(myname1)