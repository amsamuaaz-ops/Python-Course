class parrot:
    species = 'birds'
    def __init__(self,name,age):
            self.name = name
            self.age = age

blue = parrot("p1","1year")
woo = parrot("p2","0.5year")

print("blue is a{}".format(blue.species)) 
print("woo is a{}".format(woo.species)) 


print("{} is {} years old".format(blue.name,blue.age))
print("{} is {} years old".format(woo.name,woo.age))
