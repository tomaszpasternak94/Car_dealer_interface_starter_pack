import pytest

class TestParking:
    @pytest.fixture
    def audi(self):
        audi = Car('audi', 'a7', 69000)
        return audi

    @pytest.fixture
    def mercedes(self):
        mercedes = Car('mercedes', 'E-class', 20000)
        return mercedes

    @pytest.fixture
    def bentley(self):
        bentley = Car('Bentley', 'Continental GT', 400000)
        return bentley

    def test_create_parking(self):
        """ Test : 'Was the instance created correctly?' """
        parking = Parking()
        assert isinstance(parking, Parking)
        assert parking.car_dealer_cash == 100000
        assert parking.cars_amount == 0

    def test_repurchase_car(self, audi):
        """ Test : 'Can I buy one car?' """
        #given
        parking = Parking()

        #when
        parking.repurchase_car(audi)

        #then
        assert parking.cars_amount == 1
        assert parking.cars_list == ['audi']
        assert parking.car_dealer_cash == 31000

    def test_repurchase_more_cars(self, audi, mercedes):
        """ Test : 'Can I buy more than one car?' """
        # given
        parking = Parking()

        # when
        parking.repurchase_car(audi)
        parking.repurchase_car(mercedes)

        #then
        assert parking.cars_amount == 2
        assert parking.cars_list == ['audi','mercedes']
        assert parking.car_dealer_cash == 11000

    def test_repurchase_too_expensive_car(self, bentley):
        """ Test : 'I have no money - Can I buy this car?' """
        # given
        parking = Parking()

        # when / then
        with pytest.raises(TooExpensive):
            parking.repurchase_car(bentley)

    def test_sell_car(self, audi, mercedes):
        """ Test : 'I have several cars - Can I sell them?' """
        #given
        parking = Parking()
        parking.repurchase_car(audi)
        parking.repurchase_car(mercedes)

        #when
        parking.sell_car(audi)

        #then
        assert parking.cars_list == ['mercedes']
        assert parking.cars_amount == 1
        assert parking.car_dealer_cash == 93800


