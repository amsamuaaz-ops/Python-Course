numn = int(input("Enter the numenator"))
numd = int(input("Enter the denomenater"))

division2 = numn / numd

division1 = numn % numd
if division1 == 0:
    print(f"Your number is divisible and your ans is {division2}")
else :
    print(f"Your number is not divisible but the ans is {division2}")