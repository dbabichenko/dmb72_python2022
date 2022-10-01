class Car:
    def __init__(self, make, model, color, license_plate, year, mileage):
        self.__states = {
            "off" : 0,
            "idle" : 1,
            "accelerating" : 2
        }

        self.__make = make
        self.__model = model
        self.__color = color
        self.__license_plate = license_plate
        self.__mileage = mileage
        self.__year = year

        self.__state = self.__states["off"]
        self.__speed = 0


    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, car_mileage):
        self.__mileage = car_mileage

    def start(self):
        self.__state = self.__states["idle"]
        self.__speed = 0

    def stop(self):
        self.__state = self.__states["off"]
        self.__speed = 0

    def accelerate(self, delta_speed):
        self.__state = self.__state["accelerating"]
        self.__speed += delta_speed




car = Car("Ford", "Fiesta", "blue", "XYZ123", 2022, 16)
print(car.get_make())
car.start()

car2 = Car("Toyota", "Camry", "green", "KGB123", 2012, 200000)
print(car2.get_mileage())
