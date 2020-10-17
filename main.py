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

    def sell_car(self, car):
        """ This method allows the car dealer to sell a car from his parking lot """
        if self.cars_amount:
            self.car_dealer_cash += car.price + (car.price * 0.2)
            self.cars_amount -= 1
            self.cars_list.remove(car.brand)
        else:
            raise EmptyParking("Empty parking lot - all cars sold")

    def show_cars(self):
        """ This method allows the car dealer to view information
        about vehicles in a parking lot """
        cars_on_parking = ','.join((map(lambda x: x.title(), self.cars_list)))
        return f'The Cracow department has the following cars : {cars_on_parking}'

