medicalcause = input("Do you have any medical cause Yes/No").strip().upper()

if medicalcause == "YES":
    print("You are allowed to give exam")
else:
   attend = int(input("Enter your attendence"))
   if attend >=75:
       print("You are allowed")
   else:
       print("You are not allowed")