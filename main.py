class Parking:
    """ Car dealer interface starter pack """
    def __init__(self):
        self.cars_amount = 0
        self.car_dealer_cash = 100000
        self.cars_list = []

    def repurchase_car(self, car):
        """ This method allows the car dealer to repurchase a used car """
        if self.car_dealer_cash > car.price:
            self.cars_amount += 1
            self.car_dealer_cash -= car.price
            self.cars_list.append(car.brand)
        else:
            raise TooExpensive("Not enough money to repurchase this car")
