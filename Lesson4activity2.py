cost = float(input("Enter the actual cost"))
saleprice = float(input("Enter the sales price "))

if(saleprice > cost):
     ammount = saleprice - cost
     print("Total Profit = {0}".format(ammount)) 


else : 
     print("No profit!!!")
     
