units = int(input("Enter the unites"))

if (units < 50):
    amount = units * 4.5
    surcharge = 25
elif (units <= 100):
    amount = 225 + ((units-50)*6.5)
    surcharge = 35
elif (units <= 200):
    amount = 225 + 325 + ((units - 100)*8.5)
    surcharge = 45
elif (units <=300):
    amount = 225 + 325 + 850 + ((units - 200)*9.5)
    surcharge = 55
else :
    amount = 225 + 325 + 850 + ((units - 200)*11.5)
    surcharge = 75

total = amount + surcharge
print("\nElectricity Bill = %.1f" %total)
