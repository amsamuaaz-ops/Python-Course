mylist = ["House","Mansion"]
number = [1,2]
inventory = {item: count for item,count in zip(mylist, number)}
print(inventory)