class veichel:
    def __init__(self,brand,max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def show_details(self):
        print("THE BRAND AND THE MAX_SPEED OF THE CAR IS",self.max_speed, "and",self.brand)

class car(veichel):
    def __init__(self,model,lanched_year,brand,max_speed):
        self.model = model
        self.lanched_year = lanched_year
        super().__init__(brand,max_speed)

    def show_details(self):
        print(self.model,"and",self.lanched_year,"these are the details of car")
        return super().show_details()

    def fuel_type(self):
        print ("petrol")


obj1 = car("E18","1971","BMW",150)


obj1.show_details()
obj1.fuel_type()

print("is car an issubclass of veical ",issubclass(car,veichel))