secret_number = 8
attemps  = 5
count = 0

while count < attemps:
    print("Attemps left",end="")
    
    for i in range(attemps - count):
            print(i + 1, end=" ")

guess =  int(input("GUESS YOUR NUMBER"))
count += 1

if guess == secret_number:
      print("You Won Well Done")
elif guess >secret_number:
      print("Its low")
elif guess  <secret_number:
      print("Its High")
elif guess >secret_number:
      print("Its the second number of virats jersey")
elif guess < secret_number:
      print("CHECK IN 10S")
else:
      print("You lose")
   