list1 = ["Toy_Car","Paper","Watch"]
stock_count = [1,2,3]
inventory = {i: c for i,c in zip(list1, stock_count)}

in_stock_items = [item for item in list1 if inventory[item] > 1]
print("In stock items are ",in_stock_items)

chosen_item = input("What is your item")

if chosen_item not in inventory or inventory[chosen_item] == 1:
    print(chosen_item,"The chosen item is not availble THANK YOU!!!!")
    exit()

prices = (10,30,50)
markup_price = int(input("what is the markup price"))

markup_prices1 = list(map(lambda p:p + markup_price,prices))
print("Mark up prices",markup_prices1)
