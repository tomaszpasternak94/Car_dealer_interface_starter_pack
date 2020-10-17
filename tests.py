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


