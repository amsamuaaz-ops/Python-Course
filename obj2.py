class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = vehicle(240,20)

print("THE MAX SPEED OF VEHICLE IS",modelX.max_speed,"THE MINIMUM SPEED OF VEICHEL IS",modelX.mileage)